from django.shortcuts import render
from missing_person.models import MissingPersionTable
from missing_case.models import MissingCaseTable
# Create your views here.
def user_inform(request):
    objlist = MissingCaseTable.objects.exclude(status="informed").exclude(status="found")
    context = {
        'obval': objlist,
    }
    return render(request,"missing_person/11. user_inform_missing_person.html",context)



def inform(request,idd):
    objlist=MissingCaseTable.objects.filter(mi_id=idd)
    context={
        'obval':objlist
    }
    if request.method=="POST":
        obj=MissingCaseTable.objects.get(mi_id=idd)
        obj.location=request.POST.get('missinglocation')
        obj.status="informed"
        obj.save()
        return user_inform(request)
    return render(request,'missing_person/update location.html',context)
