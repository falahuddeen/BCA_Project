from django.shortcuts import render
from solved_case.models import SolvedCaseTable
from missing_case.models import MissingCaseTable

# Create your views here.
def admin_view(request):
    objlist = MissingCaseTable.objects.exclude(status="pending")
    context = {
        'obval': objlist,
    }
    return render(request,"solved_case/3. admin_view_solved_missing_case.html",context)