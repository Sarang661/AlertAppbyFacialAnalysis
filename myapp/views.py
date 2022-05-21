from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import FaceEmotionForm
from myapp.machinelearning import pipeline_model
from django.conf import settings
from myapp.models import FaceEmotion
import os
# Create your views here.

def index(request):
    form = FaceEmotionForm()
    if request.method == 'POST':
         form =FaceEmotionForm(request.POST or None, request.FILES or None)
         if form.is_valid():
             save=   form.save(commit=True)
             primary_key = save.pk
             imgobj =FaceEmotion.objects.get(pk=primary_key)
             fileroot= str(imgobj.image)
             filepath =os.path.join(settings.MEDIA_ROOT,fileroot)
             results =pipeline_model(filepath)
             print(results)
             flag1= False
             flag2= False
             return render(request,'index.html',{'form':form,'upload':True,'results':results,'flag1':flag1,'flag2':flag2})

    return render(request,'index.html',{'form':form,'upload':False})