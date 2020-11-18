from django import forms
from django.core import validators
from first_app.models import Topic


#custom validator
def check_if_small(value):
	if len(value) < 3:
		raise forms.ValidationError("Name Cannot Be Less Than 3 Chars!")

class NewUser(forms.ModelForm):
	#form fields goes here	
	class Meta:
		model = Topic
		fields = ('top_name')



class FormName(forms.Form):
	name = forms.CharField(validators=[check_if_small])
	email = forms.EmailField()
	text = forms.CharField(widget=forms.Textarea)

	#add a botCatcher to the params to see if a bot is manupulating the html
	#you can add in other type of validators too, here we added one which looks into html and if value inputed raises err
	botCatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

	#clear form


	'''

	#if html was manupulated to add content to yout form we'll catch it
	#other moethods are found by clean_
	def clean_botCatcher(self):
		botCatcher = self.cleaned_data['botCatcher']
		if len(botCatcher) > 0:
			#prints above the form "(Hidden field botCatcher) Gotcha BOT!"
			raise forms.ValidationError("Gotcha BOT!")
		return botCatcher

	'''