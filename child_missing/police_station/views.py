from django.shortcuts import render
from police_station.models import PoliceStationTable
from login.models import LoginTable
# Create your views here.
def admin_verify(request):
    objlist = PoliceStationTable.objects.filter(status="pending")
    context = {
        'obval': objlist,
    }
    return render(request,"police_station/1. admin_verify_police_station.html",context)
def police_register(request):
    ok = request.POST.get('policecontact')
    if request.method == "POST":
        if PoliceStationTable.objects.filter(contact_number=ok).exists():
            msg = "already Registered!!!!!!!!!!!!"
            context = {
                'okk': msg
            }
            return render(request, "police_station/2. Police Register.html", context)
        else :
            ob = PoliceStationTable()
            ob.name = request.POST.get('policename')
            ob.location	 = request.POST.get('policelocation')
            ob.contact_number = request.POST.get('policecontact')
            ob.e_mail = request.POST.get('policeemail')
            ob.password = request.POST.get('policepassword')
            ob.status = 'pending'
            ob.save()

            obj=LoginTable()
            obj.username=request.POST.get('policeemail')
            obj.password=request.POST.get('policepassword')
            obj.type="policep"
            obj.u_id=ob.po_id
            obj.save()


    return render(request,"police_station/2. Police Register.html")

def accept(request,idd):
    ob=PoliceStationTable.objects.get(po_id=idd)
    ob.status="approved"
    ob.save()
    obj=LoginTable.objects.get(u_id=idd,type="policep")
    obj.type="police"
    obj.save()

    return admin_verify(request)
def reject(request,idd):
    ob=PoliceStationTable.objects.get(po_id=idd)
    ob.status="rejected"
    ob.save()

    return admin_verify(request)
