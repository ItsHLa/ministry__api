from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from django.utils import timezone
from accounts.decorators import allow_user
from .models import OwnershipDocumentRequest, OwnershipDocumentResponse
from .serializers import OwnershipDocumentRequestSerializer, OwnershipDocumentResponseSerializer \



# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_request(request):
    data = request.data
    user = request.user
    serializer = OwnershipDocumentRequestSerializer(data=data)
    if serializer.is_valid():
        serializer.save(refugee = user)
        return Response({'msg': 'your request has been added successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@allow_user(allow_role=['employee'])
def get_requests(request):
    request = OwnershipDocumentRequest.get_ownership_requests()
    serializer = OwnershipDocumentRequestSerializer(request, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@allow_user(allow_role=['employee'])
def add_response(request,pk):
    data = request.data
    user = request.user
    req = OwnershipDocumentRequest.get_ownership_request(pk=pk)
    serializer = OwnershipDocumentResponseSerializer(data=data)
    if serializer.is_valid():
            serializer.save(request = req,employee=user , response_date = timezone.now())
            return Response({'msg': 'your response has been added successfully',}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_response(request):
    orequest = get_object_or_404(OwnershipDocumentRequest , refugee = request.user )
    if not hasattr(orequest, 'ownershipdocumentresponse'):
        return Response({'msg':'your request is not approved yet'},status=status.HTTP_200_OK)
    responses = orequest.ownershipdocumentresponse
    serialized_response = OwnershipDocumentResponseSerializer(instance=responses)
    return Response(serialized_response.data, status=status.HTTP_200_OK)

