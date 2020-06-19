from django.shortcuts import render
from django.contrib.auth  import authenticate, login,logout

# Create your views here.

# Create your views here.
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect('dashboard')

	context={}
	return render(request,'login.html',context)