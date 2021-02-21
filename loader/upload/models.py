from django.db import models
from django.core.exceptions import ValidationError
import uuid
import os

class Image(models.Model):
	def validate_image(fieldfile_obj):
		filesize = fieldfile_obj.file.size
		kilobyte_limit = 200
		if filesize > kilobyte_limit*1024:
			raise ValidationError('Один или несколько файлов слишком большие!\
			 Максимальный размер - 200кб')

	def get_file_path(instance, filename):
		ext = filename.split('.')[-1]
		filename = "%s.%s" % (uuid.uuid4(), ext)
		return os.path.join('images', filename)

	
	image = models.ImageField(upload_to=get_file_path, validators=[validate_image])