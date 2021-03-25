from rest_framework import serializers
from . models import *

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=Category
		fields="__all__"

class Category_detailSerializer(serializers.ModelSerializer):
	class Meta:
		model=Category_details
		fields=['category_name','event_name','start_date','end_date','create_date','event_image']
		#fields="__all__	"

