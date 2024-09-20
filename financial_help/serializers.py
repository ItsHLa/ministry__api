from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer
from accounts.models import User
from .models import FinancialAssistanceRequest, FinancialAssistanceResponse

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email',)

class FinancialAssistanceRequestSerializer(ModelSerializer):
    refugee = UserSerializer(read_only=True)
    class Meta:
        model = FinancialAssistanceRequest
        fields = ('id','social_status','family_members',
            'personal_card','proof_of_residence',
            'income','request_date','status_of_request','refugee')
        
    def create(self, validated_data):
        request = FinancialAssistanceRequest.create_financial_request(data =validated_data)
        return request
    

class FinancialAssistanceResponseSerializer(ModelSerializer):
    employee = UserSerializer(read_only=True)
    class Meta:
        model = FinancialAssistanceResponse
        fields = ('id','status_of_request','financial_assistance_help','employee','response_date')

    def create(self, validated_data):
        return FinancialAssistanceResponse.create_response(data = validated_data)

