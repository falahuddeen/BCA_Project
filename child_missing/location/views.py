from django.shortcuts import render
from missing_case.models import MissingCaseTable
from missing_person.models import MissingPersionTable
from location.models import RfidChildLocation

# Create your views here.
def police_view(request):
    objlist = MissingCaseTable.objects.all()
    context1 = {
        'obval1': objlist,
    }
    return render(request,"location/6. police_view_childlocation.html",context1)
def user_view(request):
    objlist1 = MissingCaseTable.objects.exclude(status="found").exclude(status="informed")
    context = {
        'obval': objlist1,
    }
    return render(request,"location/9. user_view_child_location.html",context)
def police_view_rfid(request):
    objlist = RfidChildLocation.objects.all()
    context1 = {
        'obval1': objlist,
    }
    return render(request,"location/police_view_child_rfid_location.html",context1)
