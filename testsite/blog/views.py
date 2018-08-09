from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, Http404
from .forms import SignUpForm
import hashlib

# Create your views here.


def main(request):
    return HttpResponse("Main page!")


def signup(request):
    """
    유저가 sign up 페이지에서 텍스트 박스에 글을(form) 써서 서버로 보내면
    서버는 UserCreationForm 으로 부터 각 내용들을 받아서 처리한다
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            uid = hashlib.md5((new_user.username + new_user.email).encode()).hexdigest()
            new_user.uid = uid
            new_user.save()
            messages.success(request, 'Your account is created successfully!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

