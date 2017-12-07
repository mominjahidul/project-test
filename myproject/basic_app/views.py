from django.shortcuts import render
from django.http import HttpResponse,Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from basic_app.models import ContactModel
from basic_app.serializers import ContactSerializer
from basic_app.permissions import IsAdminOrReadOnly
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here.

class ContactList(generics.ListCreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer


class ContactDetial(generics.RetrieveUpdateDestroyAPIView):

    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer

    # def get_object(self,pk):
    #     try:
    #         return ContactModel.objects.get(pk=pk)
    #     except ContactModel.DoesNotExist:
    #         raise Http404
    #
    # def get(self,request,pk,format=None):
    #     contacts = self.get_object(pk)
    #     serializer = ContactSerializer(contacts)
    #     return Response(serializer.data)
    #
    # def put(self,request,pk,format=None):
    #     contacts = self.get_object(pk)
    #     serializer = ContactSerializer(contacts, data=request.data)
    #     if(serializer.is_valid()):
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self,request, pk, format=None):
    #     contacts = self.get_object(pk)
    #     contacts.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
