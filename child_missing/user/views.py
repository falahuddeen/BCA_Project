from django.shortcuts import render
from user.models import UserTable
from login.models import LoginTable
# Create your views here.
def user_register(request):
    ok=request.POST.get('userphone')
    if request.method=="POST":
        if UserTable.objects.filter(phone_number=ok).exists():
            msg="already Registered!!!!!!!!!!!!"
            context={
                'okk':msg
            }
            return render(request, "user/6. User Register.html",context)
        else :

            ob=UserTable()
            ob.username=request.POST.get('username')
            ob.e_mail=request.POST.get('useremail')
            ob.phone_number=request.POST.get('userphone')
            ob.gender=request.POST.get('gender')
            ob.password=request.POST.get('userpassword')
            ob.confirm_password=request.POST.get('userpassword')
            ob.adhaar_number=request.POST.get('adhaarnum')
            ob.save()
        return render(request,"user/6. User Register.html")
    return render(request, "user/6. User Register.html")

def admin_verify(request):
    objlist = UserTable.objects.exclude(verification="verify")
    context1 = {
        'obval1': objlist,
    }
    return render(request,"user/usermanage.html",context1)
def approve(req,idd):
    object=UserTable.objects.get(u_id=idd)
    object.verification="verify"
    object.save()
    obj=LoginTable()
    obj.username=object.username
    obj.password=object.password
    obj.type="user"
    obj.u_id=object.u_id
    obj.save()
    return admin_verify(req)

def reject(req,idd):
    object = UserTable.objects.get(u_id=idd).delete()
    return admin_verify(req)
