from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import fileeuploadform
from .models import File
from django.db.models import Sum
from django.contrib import messages
# Create your views here.
def home(request):
    allfile = File.objects.all()
    if request.user.is_authenticated:
        sum = File.objects.filter(user = request.user).aggregate(Sum('sizef'))
    else:
        sum = 0
    return render(request, 'home/home.html',{'allfile': allfile,'sum': sum})
def about(request):
    return render(request, 'home/about.html')
#def uploadform(request):
    #return render(request, 'home/uploadform.html')
def upload(request):
    sum = File.objects.filter(user = request.user).aggregate(Sum('sizef'))
    if request.method == 'POST':
        uploaded_file = request.FILES['documents']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'home/upload.html',{'sum': sum})
def file_list (request):
    allfile = File.objects.all()
    return render(request, 'home/file_list.html', {'allfile': allfile})
def upload_file (request):
    if request.method == 'POST':
        form = fileeuploadform(request.POST, request.FILES, initial={'author':request.user.id})
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.sizef = (instance.files.size / 1000)+1
            instance.save()
            return redirect('../file_list')
    else:
        form = fileeuploadform()
    return render(request, 'home/upload_file.html', {'form':form})
def deletefile (request, pk):
    messages.warning(request, f'deleted')
    File.objects.filter(id=pk).delete()
    return redirect('../../file_list')
    """
    for count, x in enumerate(request.FILES.getlist("documents")):
        def process(f):
            with open('/home/towsif/Documents/AmarCloud/src/amarcloud/media/file_'+ str(count), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
    return HttpResponse("File(s) uploaded!")
    """