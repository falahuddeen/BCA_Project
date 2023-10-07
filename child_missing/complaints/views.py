from django.shortcuts import render
from complaints.models import ComplaintsTable
from user.models import UserTable
import datetime
# Create your views here.
def post_replay(request,idd):
    # print(idd)
    if request.method=="POST":
        # print('ee')
        ob=ComplaintsTable.objects.get(c_id=idd)
        ob.replay=request.POST.get('postreplay')
        ob.save()
    return render(request,"complaints/5. Post Replay.html")

def police_view(request):
    objlist = ComplaintsTable.objects.all()
    object=UserTable.objects.all()
    context = {
        'obval': objlist,
    }
    return render(request,"complaints/7. police_view_complaint_and_replay.html",context)
def post_complaint(request,idd):
    c=idd#request.session["uid"]
    if request.method=="POST":
        ob=ComplaintsTable()
        ob.complaint=request.POST.get('postcomplaint')
        ob.date = datetime.date.today()
        ob.time = datetime.datetime.now().time()
        ob.u_id = c
        ob.replay ='pending'
        ob.save()
    return render(request,"complaints/8. Post Complaint.html")
def user_view(request,idd):
    objlist1 = ComplaintsTable.objects.filter(u_id=idd)
    context1 = {
        'obval': objlist1,
    }
    return render(request,"complaints/14. user_view_replay.html",context1)



