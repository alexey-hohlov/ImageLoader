from django.shortcuts import render
from .forms import ImageForm
from .models import Image

def image_upload_view(request):
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		files = request.FILES.getlist('image')
		if form.is_valid():
			for f in files:
				file_instance = Image(image=f)
				file_instance.save()
			return render(request, 'index.html', {'form': form, 'file_instance': file_instance})
	else:
		form = ImageForm()
	return render(request, 'index.html', {'form': form})
