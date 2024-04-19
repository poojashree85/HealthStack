from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .serializer import dataserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST', 'DELETE'])
def getdetails(request):
    if request.method == 'GET':
        # This retrieves all hospital details
        hospital_Details = hospitaldetails.objects.all()
        serializer = dataserializer(hospital_Details, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # This creates a new hospital detail
        serializer = dataserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # This block should handle deleting a specific hospital detail
        try:
            # Retrieve the hospital detail to delete
            hospital_detail = hospitaldetails.objects.get(pk=request.data.get('id'))
        except hospitaldetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        hospital_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






def hospital(request):
	list_of_hospital = hospitaldetails.objects.all().values()
	return render(request, 'h.html', {
    'hospitalname': hospitaldetails.objects.all().values()[0]['Hospital_Name'],
    'address': hospitaldetails.objects.all().values()[0]['Address'],
    'list_of': list_of_hospital
})
