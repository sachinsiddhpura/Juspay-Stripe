from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponseRedirect
#from django.core.context_processors import csrf
from django.conf import settings
import datetime
import stripe
from .forms import PayForm
from django.template.context_processors import csrf

stripe.api_key=settings.STRIPE_SECRET

def reg(request):
	if request.method=="POST":
		form=PayForm(request.POST or None)
		if form.is_valid():
			try:
				customer=stripe.Change.create(
					amount=499,
					currency='USD',
					description=form.cleaned_data.get('email'),
					card	=form.cleaned_data.get('stripe_id'),
					)
				form.save()
				return HttpResponseRedirect('/regsuc.html')
			except stripe.CardError:
				form.add_error("Not Card Valid")
	else:
		form=PayForm()

	args={}
	args.update(csrf(request))
	args['form']=form
	args['publishable']=settings.STRIPE_PUBLISHABLE
	args['months']=range(1,12)
	args['years']=range(2011,2022)
	args['soon']=datetime.date.today()+datetime.timedelta(days=30)
	return render_to_response('reg.html',args)
