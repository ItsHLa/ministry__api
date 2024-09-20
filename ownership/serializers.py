from rest_framework.serializers import ModelSerializer
from accounts.models import User
from .models import OwnershipDocumentRequest, OwnershipDocumentResponse



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')



class OwnershipDocumentRequestSerializer(ModelSerializer):
    refugee = UserSerializer(read_only=True)
    class Meta:
        model = OwnershipDocumentRequest
        fields = (
            'id','proof_of_identity',
            'lease_agreement','housing_certificate','purchase_contract',
            'title_deed','refugee','request_status')
        
    def create(self, validated_data):
        return OwnershipDocumentRequest.create_requset(data = validated_data)




class OwnershipDocumentResponseSerializer(ModelSerializer):
    employee = UserSerializer(read_only=True)
    class Meta:
        model = OwnershipDocumentResponse
        fields = ('id','employee','response_status','document_ownership')
    
    def create(self , validated_data):
        return OwnershipDocumentResponse.create_response(validated_data)

