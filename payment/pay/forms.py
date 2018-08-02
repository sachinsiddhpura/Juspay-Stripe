from django.forms import ModelForm
from .models import Pay
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

class PayForm(forms.ModelForm):
	class Meta:
		model 	=Pay
		fields	=('full_name','email','stripe_id')

	def add_error(self,message):
		self._error[NON_FIELD_ERRORS]=self.error_class([message])