from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import forms

# Create your views here.
def register(request):
	form = forms.CreateUserForm()

	if(request.method == 'POST'):
		form = forms.CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,'Account was created for '+user)
			return redirect('login')

	context={'form':form}
	return render(request,'register.html',context)