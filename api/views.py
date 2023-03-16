from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, Http404
from medicine.models import Medicine
from medicine.serializers import MedicineSerializer
from django.db.models import Q
from rest_framework.views import APIView

# Create your views here.


@api_view(['GET'])
def getEndpoints(request):
    routes = [
        {
            'url' : 'api/medicines/',
            'methods' : ['GET', 'POST'],
        },
        {
            'url' : 'api/medicine/:id/',
            'methods' : ['GET', 'PUT', 'DELETE']
        },
        {
            'url' : 'login/',
            'methods' : ['POST']
        },
        {
            'url' : 'logout/',
            'methods' : ['GET']
        },
        {
            'url' : 'get-user/',
            'methods' : ['GET']
        },
        {
            'url' : 'register/',
            'methods' : ['POST']
        }
    ]
    return Response(routes)



class MedicineList(APIView):
    def get(self, request):
        try:
            query = request.GET.get('query')
            if query == None:
                query = ''
            medicines = Medicine.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
            serializer = MedicineSerializer(medicines, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({
                "success" : "false",
                "error" : str(e)
            })
    def post(self, request):
        try:
            medicine = Medicine.objects.create(
                name = request.data['name'],
                image = request.data['image'],
                description = request.data['description'],
                price = request.data['price'],
                manufacturer = request.data['manufacturer'],
                type = request.data['type'],
                quantity = request.data['quantity'],
                dosage = request.data['dosage'],
                substance = request.data['substance'],
                therauptic_category = request.data['therauptic_category'],
                disease = request.data['disease']
            )
            return Response({"success" : "true"})
        except Exception as e:
            return Response({
                "success" : "false",
                "error" : str(e)
            })


class MedicineDetail(APIView):
    def get_object(self, id):
        try:
            return Medicine.objects.get(id=id)
        except Medicine.DoesNotExist:
            return Http404
    def get(self, request, id):
        try:
            medicine = self.get_object(id)
            serializer = MedicineSerializer(medicine, many=False)
            return Response(serializer.data)
        except Exception as e:
            return Response({
                "success" : "false",
                "error" : str(e)
            })
    def post(self, request, id):
        try:
            medicine = self.get_object(id)
            medicine.save()
            return Response({"success" : "true"})
        except Exception as e:
            return Response({
                "success" : "false",
                "error" : str(e)
            })
    def delete(self, request, id):
        try:
            medicine = self.get_object(id)
            medicine.delete()
            return Response({"success" : "true"})
        except Exception as e:
            return Response({
                "success" : "false",
                "error" : str(e)
            })