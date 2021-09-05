from django.shortcuts import render

# Create your views here.

def addPhoto(request):
  return render(request, 'photos/add.html')

def gallery(request):
  return render(request, 'photos/gallery.html')

def viewPhoto(request, cn):
  return render(request, 'photos/photos.html')
