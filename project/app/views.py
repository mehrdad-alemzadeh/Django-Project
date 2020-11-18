from django.shortcuts import render
from first_app import forms

def index(request):
	return render(request, 'first_app/index.html')

def form_name_view(request):
	form = forms.NewUserForm()
	if request.method == 'POST':
				form = NewUserForm(request.POST)
				if form.is_valid():
					form.save()
					return index(request)
				else:
					print("Form Error")

	return render(request, 'first_app/formpage.html', {'form' : form})


			

