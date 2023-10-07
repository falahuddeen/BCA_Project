from django.shortcuts import render

# Create your views here.
def admin_home(request):
    return render(request,'temp/Admin home page.html')
def main_home(request):
    return render(request,'temp/main home page.html')
def police_station_home(request):
    return render(request,'temp/Police Station home page.html')
def user_home(request):
    return render(request,'temp/User home page.html')