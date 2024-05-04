from django.shortcuts import render,HttpResponse
from app1 import views
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from app1.models import Song
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



def index(request):
    song=Song.objects.all()
    return render(request,'index.html',{'song':song})

def register(request):
    if request.method=="GET":
        return render(request,'register.html')
    else:
        u=request.POST['uname']
        p=request.POST['upass']
        c=request.POST['ucpass']
        uobj=User.objects.create(username=u,email=u)
        uobj.set_password(p)
        uobj.save()
        return redirect('/register')
    
def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        u=request.POST['uname']
        p=request.POST['upass']
        a=authenticate(username=u,password=p)
        if a is not None:
            print(a)
            print(a.password,a.id)
            #login(request,a)
            return redirect('/')
       
        else:
            print(a)
            return HttpResponse("Login Fail ")
    



def user_logout(request):
    logout(request)
    return redirect("/")

 
def audio_list(request):
    audio_files = Song.objects.all()
    return render(request, 'audio_list.html', {'audio_files': audio_files})

def add_audio(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        audio_file = request.FILES.get('audio_file')

        Song.objects.create(name=name, audio_file=audio_file)
        return redirect('/audio_list')

    return render(request, 'add_audio.html')

def delete_audio(request, pk):
    audio_file = get_object_or_404(Song, pk=pk)

    if request.method == 'POST':
        audio_file.delete()
        return redirect('/audio_list')

    return render(request, 'delete_audio.html', {'audio_file': audio_file})

def songpost(request, id):
    song=Song.objects.filter(song_id=id).first()
    return render(request,'songpost.html',{'song':song})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def search(request):
    query = request.GET.get("query")
    song= Song.objects.all()
    qs=song.filter(name__icontains=query)
    return render(request,'search.html',{'song':qs})

def forgetpass(request):
    if request.method=='GET':
        return render(request,'forgetpass.html')
    else:
        username=request.POST['uname']
        password=request.POST['upass']
        obj=User.objects.filter(username=username)
        obj.update(password=password)
        return render(request,'login.html')
    
@login_required
def like_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    user = request.user

    if user in song.likes.all():
        song.likes.remove(user)
    else:
        song.likes.add(user)

    return redirect('song_detail', song_id=song_id)

def playlist(request):
    return render(request,'playlist.html')







