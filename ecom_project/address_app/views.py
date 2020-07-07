from django.shortcuts import render
from .models import District


# Create your views here.
def districts(request):
    districts = District.objects.all()
    context = {'districts': districts}
    return render(request, 'address_app/districts.html', context)


def district_details(request, id):
    district = District.objects.get(id=id)
    context = {'district': district}
    return render(request, 'address_app/district_details.html', context)
