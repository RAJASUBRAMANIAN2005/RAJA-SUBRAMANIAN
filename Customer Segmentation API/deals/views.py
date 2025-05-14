import re
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DealSerializer
import smtplib
import pandas as pd
from config import *

# Create your views here.
@api_view(['POST'])
def AddDeal(request):
    response = {"status":1 ,"message":""}
    serializer = DealSerializer(data=request.data)
    try:
        if serializer.is_valid():
          serializer.save()
          response['message'] = "Deal Added success and email notifications sent to respective customers"
          # creates SMTP session
          s = smtplib.SMTP('smtp.gmail.com', 587)
          # start TLS for security
          s.starttls()
          # Authentication
          s.login(LOGIN_EMAIL, LOGIN_EMAIL_PASSWORD)
          # message to be sent
          message = f"""
          New Deals from DMart
          prodcut name : {request.data['product_name']}
          original price : {request.data['original_price']}
          discount price : {request.data['discount_price']}          
          """ 
  
          # sending the mail
          s.sendmail(FROM_EMAIL, TO_EMAIL, message)
          # terminating the session
          s.quit()

        else:
            response['status'] = 0
            print(serializer.errors)
            response['message'] = "something went wrong check parameters in data"
    except Exception as e:
          print(e)
          response['status'] = 0
          response['message'] = str(e)

    finally:
        return Response(response)          
            
