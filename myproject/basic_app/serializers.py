from basic_app.models import ContactModel
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta():
        model = ContactModel
        fields = ('id','name','contact','address')
