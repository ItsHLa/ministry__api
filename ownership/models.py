from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from accounts.models import User


def get_ownership_image(self , filename):
    return f'{self.pk}.png'


# Create your models here.
class OwnershipDocumentRequest(models.Model):
    proof_of_identity = models.ImageField(upload_to=f'OwnershipDocumentRequest/proof_of_identity/')
    lease_agreement = models.ImageField(upload_to=f'OwnershipDocumentRequest/lease_agreement/',null=True,blank=True)
    housing_certificate = models.ImageField(upload_to=f'OwnershipDocumentRequest/housing_certificate/',null=True,blank=True)
    purchase_contract = models.ImageField(upload_to=f'OwnershipDocumentRequest/purchase_contract/',null=True,blank=True)
    title_deed = models.ImageField(upload_to=f'OwnershipDocumentRequest/title_deed/', null=True, blank=True)
    refugee = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    request_status = models.CharField(max_length=100,default='pending')
    
    @staticmethod
    def create_requset(data):
        return OwnershipDocumentRequest.objects.create(**data)
    
    @staticmethod
    def get_ownership_request(pk):
        return get_object_or_404(OwnershipDocumentRequest , pk=pk)
    
    @staticmethod
    def get_ownership_requests():
        return OwnershipDocumentRequest.objects.all()


class OwnershipDocumentResponse(models.Model):
    request = models.OneToOneField(OwnershipDocumentRequest,on_delete=models.CASCADE)
    response_date = models.DateField(auto_now_add=True )
    employee = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)
    response_status = models.CharField(max_length=100 , null=True,blank=True)
    document_ownership = models.ImageField(upload_to='OwnershipDocumentResponse/document_ownership/',null=True,blank=True)
    
    @staticmethod
    def create_response(data):
        return OwnershipDocumentResponse.objects.create(**data )
    
    @staticmethod
    def get_ownership_response(pk):
        return get_object_or_404(OwnershipDocumentResponse,pk=pk)
    
    
@receiver(post_save , sender = OwnershipDocumentResponse)
def update_request(sender ,instance , created , **kwargs):
    if created:
        request = get_object_or_404(OwnershipDocumentRequest,pk =instance.pk)
        request.request_status = 'done'
        request.save()