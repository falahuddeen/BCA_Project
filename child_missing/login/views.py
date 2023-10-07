from django.shortcuts import render
from login.models import LoginTable
import datetime
# Create your views here.
def login(request):
    if request.method == "POST":
        uname = request.POST.get("loginusername")
        passw = request.POST.get("loginpassword")
        obj = LoginTable.objects.filter(username=uname, password=passw)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "admin":
                request.session["uid"] = uid
                return render(request, 'temp/Admin home page.html')
            elif tp == "police":
                request.session["uid"] = uid
                return render(request, 'temp/Police Station home page.html')
            # elif tp == "user":
            #     request.session["uid"] = uid
            #     return render(request, 'login/s_subhome.html')
            # # else:
        objlist = "Username or Password incorrect... Please try again...!"
        context = {
            'msg': objlist,
        }
        return render(request, 'login/1. Login.html', context)
    return render(request,"login/1. Login.html")
from django.http import HttpResponse
from rest_framework.views import APIView,Response
from login.serializer import android
class log_view(APIView):
    def get(self, request):
        ob = LoginTable.objects.all()
        ser = android(ob, many=True)
        return Response(ser.data)

    def post(self, request):
        unm = request.data['username']
        pwd = request.data['password']
        ob = LoginTable.objects.filter(username=unm, password=pwd)

        ser = android(ob, many=True)
        return Response(ser.data)