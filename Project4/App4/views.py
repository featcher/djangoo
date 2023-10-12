from django.shortcuts import render
from App4.models import upload
from App4.forms import user

# Create your views here.
def cll(request):
    if request.method=='POST':
        form=user(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            form=user()
    return render(request,'form.html')

def viw(request):
    a= upload.objects.all()
    context={'key':a}
    return render(request,'view.html',context)