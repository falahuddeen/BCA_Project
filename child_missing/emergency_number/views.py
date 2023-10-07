from django.shortcuts import render
from emergency_number.models import EmergencyNumberTable
# Create your views here.
def emergency(request):
    if request.method=="POST":
        eid=str(request.session["uid"])
        ob=EmergencyNumberTable()
        ob.em_number = request.POST.get('em')
        print(ob.em_number)
        print(request.POST.get('em'))
        # ob.number="1213"
        ob.po_id = eid
        ob.save()
    return render(request,"emergency_number/4. Emergency Number.html")
def user_view(request):
    objlist = EmergencyNumberTable.objects.all()
    context = {
        'obval': objlist,
    }
    return render(request,"emergency_number/13. user_view_emergency_number_and_call.html",context)
from django.http import HttpResponse
from rest_framework.views import APIView,Response
from emergency_number.serializer import android
class emg_view(APIView):
    def get(self, request):
        ob = EmergencyNumberTable.objects.all()
        ser = android(ob, many=True)
        return Response(ser.data)

    def post(self, request):
        ob=EmergencyNumberTable()
        ob.po_id=request.data['po_id']
        ob.number=request.data['em_number']
        ob.save()
        return HttpResponse("ok")



