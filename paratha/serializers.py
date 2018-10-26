from rest_framework import serializers
from .models import camp

class campSerializer(serializers.ModelSerializer):

	class Meta:
		model = camp
		fields = '__all__'