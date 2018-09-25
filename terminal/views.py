"""
For validation see - http://www.django-rest-framework.org/api-guide/serializers/

curl --header "Content-Type: application/json" --request POST --data '{"1": 1}' http://localhost:8000/bank/set
curl --header "Content-Type: application/json" --request POST --data '{"amount": 100}' http://localhost:8000/bank/withdraw
"""

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


from .service import Bank
from .exception import BankError

bank_service = Bank()


@api_view(['GET'])
def bank_status(request):
    return Response(bank_service.status())


@api_view(['POST'])
def bank_withdraw(request):
    try:
        return Response(bank_service.withdraw(request.data['amount']))
    except BankError as error:
        return Response({
            'status': 'error',
            'message': str(error),
        })


@api_view(['POST'])
def bank_set(request):
    return Response(bank_service.set(request.data))


@api_view(['GET'])
def bank_reset(request):
    return Response(bank_service.reset())


