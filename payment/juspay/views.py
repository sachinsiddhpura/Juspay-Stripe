from django.shortcuts import render

# Create your views here.
from random import randint
import juspayp3
import requests
from django.http import HttpResponseRedirect

juspayp3.api_key = 'D304CC61928C4E67A6519D2CD4639D51'
juspayp3.environment = 'sandbox'

def juspay(request):
	ordered_id=randint(5000,7000)
	context=dict()

	new_order=juspayp3.Orders.create(
		order_id='999999',
		amount=100,
		currency='INR',
		customer_id='guest_user_101',
    	customer_email='customer@gmail.com',
    	customer_phone='9988665522',
		)
	context=vars(new_order)
	context['links']=vars(new_order.payment_links)
	template='payments.html'
	return render(request,template,context)

