from django.shortcuts import render
from missing_case.models import MissingCaseTable
import  datetime
from solved_case.models import SolvedCaseTable
from child_missing import settings
from django.http import HttpResponseRedirect
from PIL import Image
from io import BytesIO
import base64
from django.views.decorators.csrf import csrf_exempt

import string
from django.http import JsonResponse
from django.db import connection
from django.core.files.storage import FileSystemStorage
from PIL import Image
from io import BytesIO
import base64


from MySQLdb._mysql import result
from luxand import luxand

class facedata:
    import requests

    url = "https://api.luxand.cloud/subject"

    payload = {}
    headers = {'token': "36f0a9d16c554e87bd09d024842e1b50"}

    response = requests.request("DELETE", url, data=payload, headers=headers)

    print(response.text)

    client = luxand("36f0a9d16c554e87bd09d024842e1b50")

    obj = MissingCaseTable.objects.filter(status='pending')

    for x in obj:
        # imgpath = settings.BASE_DIR + settings.STATIC_URL + "faces/"+ str(x) +".jpg"
        img = x.image
        nm = x.name
        idd = x.mi_id
        i = str(idd)


        # print(img+"#"+nm+"#"+i+"#")

        imgpath = settings.BASE_DIR + settings.STATIC_URL + img
        print(imgpath)
        client.add_person(name=i, photos=[imgpath])
    #





# def solve(request,idd):
#     if request.method == "POST":
#
#         myfile = request.FILES['img']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         image = myfile.name
#         print(image)
#
#         imgpath = settings.BASE_DIR + settings.STATIC_URL + image
#         result = facedata.client.recognize(photo=imgpath)
#
#         print(len(result))
#         if len(result) > 0:
#
#             try:
#                 print(result)
#                 print(type(result))
#                 res = result[0]
#                 print('hello')
#                 print(res)
#                 print(type(res))
#                 c = res['name']
#                 c = int(c)
#                 print('dddddd')
#                 print(c)
#
#                 staa = str(
#                     'Solved, Child Found at ' + str(request.session['loc']) + " on " + str(request.session['da']))
#                 print(staa)
#                 print(c)
#                 print(type(c))
#
#                 oooo = MissingCaseTable.objects.get(mi_id=c)
#                 oooo.status = staa
#                 print('hiii')
#                 img1 = oooo.image
#                 oooo.save()
#
#                 # return HttpResponse(result)
#                 context = {
#                     'objval': result,
#                     'img': image,
#                     "case": img1,
#                 }
#                 return render(request, 'missing_case/solve.html', context)
#             except:
#                 context = {
#                     "case": "No match Found",
#                 }
#                 return render(request, 'missing_case/solve.html', context)
#                 # /return HttpResponse("No Matching Found")
#         else:
#             context = {
#                 "res": "No match Found",
#             }
#             return render(request, 'missing_case/solve.html', context)
#     return render(request, 'missing_case/solve.html')
#
#     # ob=MissingCaseTable.objects.get(mi_id=idd)
#     # ob.status="solved"
#     # ob.save()
#     #
#     # obb=SolvedCaseTable()
#     # obb.mi_id=idd
#     # obb.case=ob.name
#     # obb.status=ob.status
#     # obb.save()
#     # return police_view(request)
#




def solve(request,idd):
    # # client.add_person(name="Brad Pitt", photos=["https://dashboard.luxand.cloud/img/brad-pitt.jpg"])
    if request.method == "POST":
        # imgpath = settings.BASE_DIR + settings.STATIC_URL + "/faces/4.jpg"

        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        image = myfile.name

        imgpath = settings.BASE_DIR + settings.STATIC_URL + image
        result = facedata.client.recognize(photo=imgpath)

        print(len(result))
        if len(result)>0:
            try:
                print(result)
                print(type(result))
                res=result[0]
                print('hello')
                print(res)
                print(type(res))
                c=res['name']
                c=int(c)
                print('dddddd')
                print(c)
                # p = '"'+result+'"'
                # print(result)
                # res = result.replace("[", "")
                # res = res.replace("]", "")
                # res=result[0]

                # print(res[0])
                # res = res.replace("'", '"')
                # dt = json.loads(res)
                # a = dt['name']
                # print(a)
                # b = a.replace("'", "")
                # c = int(b)
                # print(c)
                # c=4

                o = MissingCaseTable.objects.get(mi_id=c)
                img1 = o.image
                o.status = 'found'
                o.save()

                # return HttpResponse(result)
                context = {
                    'objval':result,
                    'img':image,
                    "case":img1,
                }
                return render(request, 'missing_case/solve.html',context)
            except:
                context = {
                    "case": "No match Found",
                }
                return render(request, 'missing_case/solve.html', context)
                # /return HttpResponse("No Matching Found")
        else:
            context = {
                "res": "No match Found",
            }
            return render(request, 'missing_case/solve.html', context)
    return render(request,'missing_case/solve.html')








# Create your views here.
def admin_missing(request):
    objlist = MissingCaseTable.objects.all()
    context = {
        'obval': objlist,
    }
    return render(request,"missing_case/2. admin_missing_child_case.html",context)
def admin_view(request):
    objlist1 = MissingCaseTable.objects.filter(Verification='verified').exclude(status="found").exclude(status="informed")
    context1 = {
        'obval1': objlist1,
    }
    return render(request,"missing_case/2. admin_view_missing_child_case.html",context1)
def police_verify(request):
    objlist2 = MissingCaseTable.objects.filter(Verification='').exclude(status='found')
    context2 = {
        'obval2': objlist2,
    }
    return render(request,"missing_case/4. police_verify_missing_case.html",context2)
def police_view(request):
    objlist3 = MissingCaseTable.objects.filter(Verification='verified').exclude(status='found')
    context3 = {
        'obval3': objlist3,
    }
    return render(request,"missing_case/5. police_view_missing_case.html",context3)
def register_missing(request):
    if request.method=="POST":
        ob=MissingCaseTable()
        ob.name = request.POST.get('missingname')
        ob.location = request.POST.get('missinglocation')
        ob.phone_number = request.POST.get('missingphone')
        ob.image = request.POST.get('missingimage')
        ob.status ='pending'
        ob.Verification ='pending'
        ob.date=datetime.date.today()
        ob.time=datetime.datetime.now()
        ob.save()
    return render(request,"missing_case/7. Register missing case.html")
def user_view_case(request):
    objlist4 = MissingCaseTable.objects.all()
    context4 = {
        'obval4': objlist4,
    }
    return render(request,"missing_case/8. user_view_case_status.html",context4)
def user_view_missing(request):
    objlist5 = MissingCaseTable.objects.all()
    context5 = {
        'obval5': objlist5,
    }
    return render(request,"missing_case/10. user_view_missing_case.html",context5)
def verify(request,idd):
    ob=MissingCaseTable.objects.get(mi_id=idd)
    ob.Verification="verified"
    ob.save()
    return police_verify(request)
def decline(request,idd):
    ob=MissingCaseTable.objects.get(mi_id=idd).delete()

    return police_verify(request)
def solved(request,idd):
    ob=MissingCaseTable.objects.get(mi_id=idd)
    ob.status="found"
    ob.save()

    obb=SolvedCaseTable()
    obb.mi_id=idd
    obb.case=ob.name
    obb.status=ob.status
    obb.save()
    return police_view(request)
def ongoing(request,idd):
    ob=MissingCaseTable.objects.get(mi_id=idd)
    ob.status="ongoing"
    ob.save()
    return police_view(request)


from django.http import HttpResponse
from rest_framework.views import APIView,Response
from missing_case.serializer import android
class emg_view(APIView):
    def get(self, request):
        ob = MissingCaseTable.objects.all()
        ser = android(ob, many=True)
        return Response(ser.data)

    def post(self, request):
        ob=MissingCaseTable()
        ob.name=request.data['name']
        ob.location=request.data['location']
        ob.phone_number = request.data['phone_number']
        ob.date=datetime.datetime.today()
        ob.time=datetime.datetime.now()
        ob.status="pending"
        ob.image = ""
        ob.save()
        return HttpResponse(str(ob.mi_id))


from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.db.models import Max

@csrf_exempt
def simple_upload(request):
    if request.method == 'POST' and request.FILES['uploadedfile']:
        myfile = request.FILES['uploadedfile']
        fs = FileSystemStorage()
        fpath = settings.BASE_DIR + settings.STATIC_URL +myfile.name
        filename = fs.save(fpath, myfile)
        id = MissingCaseTable.objects.aggregate(Max('mi_id'))['mi_id__max']
        print(id)
        obj=MissingCaseTable.objects.get(mi_id=id)

        # Max(ob.image)
        obj.image=myfile
        obj.save()
        return HttpResponse("uploaded")
    return HttpResponse("hello")


def Police_view_and_solve(request):
    ob=MissingCaseTable.objects.exclude(status="found").exclude(status="informed").filter(Verification="verified")
    context={
        'obval3':ob
    }
    return render(request,'missing_case/police_view.html',context)