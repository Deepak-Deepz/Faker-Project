from django.shortcuts import render
from myApp.models import Student
# Create your views here.
def View1(request):
    s = Student.objects.all()
    d = {'stud': s}
    return render(request,'myApp/1.html',d)
