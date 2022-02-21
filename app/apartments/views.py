from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from apartments.models import Apartment
from apartments.serializers import ApartmentSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "apartments/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Apartment.objects.all()
    return render(request, "apartments/index.html", {'apartments': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'apartments/index.html'

    def get(self, request):
        queryset = Apartment.objects.all()
        return Response({'apartments': queryset})


class list_all_apartments(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'apartments/apartment_list.html'

    def get(self, request):
        queryset = Apartment.objects.all()
        return Response({'apartments': queryset})


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def apartment_list(request):
    if request.method == 'GET':
        tutorials = Apartment.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            apartments = apartments.filter(title__icontains=title)

        apartments_serializer = ApartmentSerializer(apartments, many=True)
        return JsonResponse(apartments_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        apartment_data = JSONParser().parse(request)
        apartment_serializer = ApartmentSerializer(data=apartment_data)
        if apartment_serializer.is_valid():
            apartment_serializer.save()
            return JsonResponse(apartment_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(apartment_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Apartment.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Apartments were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def apartment_detail(request, pk):
    try:
        apartment = Apartment.objects.get(pk=pk)
    except Apartment.DoesNotExist:
        return JsonResponse({'message': 'The apartment does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        apartment_serializer = ApartmentSerializer(apartment)
        return JsonResponse(apartment_serializer.data)

    elif request.method == 'PUT':
        apartment_data = JSONParser().parse(request)
        apartment_serializer = ApartmentSerializer(apartment, data=apartment_data)
        if apartment_serializer.is_valid():
            apartment_serializer.save()
            return JsonResponse(apartment_serializer.data)
        return JsonResponse(apartment_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def apartment_list_published(request):
    apartments = Apartment.objects.filter(published=True)

    if request.method == 'GET':
        apartments_serializer = ApartmentSerializer(apartments, many=True)
        return JsonResponse(apartments_serializer.data, safe=False)