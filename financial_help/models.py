from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from accounts.models import User


# Create your models here.

class FinancialAssistanceRequest(models.Model):
    social_status = models.CharField(max_length=100)
    family_members = models.IntegerField(default=0)
    personal_card = models.ImageField(upload_to='FinancialAssistanceRequest/personal_cards/')
    proof_of_residence = models.ImageField(upload_to='FinancialAssistanceRequest/proof_of_residence/')
    income = models.ImageField(upload_to='FinancialAssistanceRequest/income/',null=True,blank=True)
    refugee = models.ForeignKey(User,on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    status_of_request = models.CharField(max_length=100, default='pending') 
    
    
    
    @staticmethod
    def create_financial_request(data):
        return FinancialAssistanceRequest.objects.create(**data)
    
    @staticmethod
    def get_request_by(pk):
        return get_object_or_404(FinancialAssistanceRequest,pk=pk)
    
    @staticmethod
    def get_financial_requests():
        return FinancialAssistanceRequest.objects.all()

class FinancialAssistanceResponse(models.Model):
    request = models.OneToOneField(FinancialAssistanceRequest,on_delete=models.CASCADE)
    status_of_request = models.CharField(max_length=100,null=True)
    employee = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    financial_assistance_help = models.IntegerField(default=0)
    response_date = models.DateField(auto_now_add=True)
    
    
    @staticmethod
    def create_response(data):
        return FinancialAssistanceResponse.objects.create(**data)
    
    @staticmethod
    def get_response_by(pk):
        return get_object_or_404(FinancialAssistanceResponse ,pk = pk)
    
    @staticmethod
    def get_response_for(refugee):
        req = get_object_or_404(FinancialAssistanceRequest,refugee =refugee)
        return req.financialassistanceresponse



@receiver(post_save , sender = FinancialAssistanceResponse)
def update_request(sender ,instance , created , **kwargs):
    if created:
        request = get_object_or_404(FinancialAssistanceRequest,pk =instance.pk)
        request.status_of_request = 'done'
        request.save()