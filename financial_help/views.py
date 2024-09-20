from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_200_OK
from django.utils import timezone
from accounts.decorators import allow_user
from .models import FinancialAssistanceRequest, \
    FinancialAssistanceResponse
from .serializers import FinancialAssistanceRequestSerializer, \
    FinancialAssistanceResponseSerializer,  UserSerializer


# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_request(request):
   user = request.user
   data = request.data
   serializer = FinancialAssistanceRequestSerializer(data=data)
   if serializer.is_valid():
       serializer.save(refugee = user)
       return Response({'msg': 'your request has been added successfully', }, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@allow_user(allow_role=('employee',))
def get_requests(request):
    requests = FinancialAssistanceRequest.get_financial_requests()
    serialized_requests = FinancialAssistanceRequestSerializer(requests, many=True)
    return Response(serialized_requests.data,status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_response(request):
    frequest = get_object_or_404(FinancialAssistanceRequest , refugee = request.user )
    if not hasattr(frequest, 'financialassistanceresponse'):
        return Response({'msg':'your request is not approved yet'},status=HTTP_200_OK)
    response = frequest.financialassistanceresponse
    serializer = FinancialAssistanceResponseSerializer(instance=response)
    return Response(serializer.data,status=HTTP_200_OK)
   

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allow_user(allow_role=['employee'])
def add_response(request,pk):
    user = request.user
    data = request.data
    frequest = FinancialAssistanceRequest.get_request_by(pk = pk)
    serializer = FinancialAssistanceResponseSerializer(data=data , partial = True)
    if serializer.is_valid():
        serializer.save(request = frequest,employee= user,response_date= timezone.now())
        return Response({'msg': 'your response has been added successfully',}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)