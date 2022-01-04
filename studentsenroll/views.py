from django.shortcuts import render,HttpResponseRedirect

import studentsenroll
from .forms import StudentDetil
from .models import Student

# Create your views here.
# functon for delete data
def deletedata(request,id):
    if request.method=='POST':
        sd=Student.objects.get(pk=id)
        sd.delete()
        return HttpResponseRedirect('/')


# functon for udate data
def updatedata(request,id):
    if request.method=="POST":
        ud=Student.objects.get(pk=id)
        formupd=StudentDetil(request.POST,instance=ud)
        if formupd.is_valid():
            formupd.save()
        formupd=StudentDetil()
    else:
        ud=Student.objects.get(pk=id)
        formupd=StudentDetil(instance=ud)

    return render(request,'studentsenroll/update.html',{'upform':formupd})

def show(request):
    if request.method=="POST":
        stform=StudentDetil(request.POST)
        if stform.is_valid():
            # stform.save()
            Nm=stform.cleaned_data['name']
            Em=stform.cleaned_data['email']
            Ps=stform.cleaned_data['password']
            reg=Student(name=Nm,email=Em,password=Ps)
            reg.save()
            stform=StudentDetil()
    else:
        stform=StudentDetil()
    stud=Student.objects.all()
    return render(request,'studentsenroll/show.html',{'sform':stform,'stu':stud})

   

            

