from django.shortcuts import render
from awareness.models import AwarenessTable
import datetime
# Create your views here.
def aware(request):
    if request.method=="POST":
        eid = str(request.session["uid"])
        ob=AwarenessTable()
        ob.awareness=request.POST.get('awarnesspost')
        ob.date=datetime.date.today()
        ob.po_id=eid
        ob.save()
    return render(request,"awareness/3. Post Awarness.html")
def view_aware(request):
    objlist=AwarenessTable.objects.all()
    context={
        'obval':objlist,
    }
    return render(request,"awareness/12. user_view_awarness.html",context)
