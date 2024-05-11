from django.shortcuts import render
from app.models import student
def abc(request):
    data=student.objects.all()
    context={"data":data}
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")