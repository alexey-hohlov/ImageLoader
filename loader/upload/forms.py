from django import forms
from .models import Image
from django.forms import ClearableFileInput

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['image']
		widgets = {
		'image': ClearableFileInput(attrs={'multiple': True}),
		}