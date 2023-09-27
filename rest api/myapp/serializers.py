from rest_framework import serializers
from .models import Book


class lanSerializer(serializers.ModelSerializer):
	class Meta:
		model=Book
		fields=('id','title','author','isbn','publisher')
