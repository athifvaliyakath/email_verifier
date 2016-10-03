from django.shortcuts import render
from django.http import JsonResponse
from validate_email_address import validate_email
import re
import socket
import smtplib
import dns.resolver

# Create your views here.
def home(request):
    return render(request, 'email_verifier/home.html', {})


def email_verifier(request, inputAddress):
	response_data = {}
	if request.method == 'GET':
		output = validate_email(inputAddress, verify=True)
		if output == True:
			status = 200
		else:
			status = 550

		response_data['status'] = status
		return JsonResponse(response_data)
