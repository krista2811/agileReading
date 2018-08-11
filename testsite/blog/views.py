from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .forms import *

# Create your views here.


def main(request):
    books = Book.objects.order_by('-created_date')
    return render(request, 'core/book_list.html', {'books': books})


def signup(request):
    """
    유저가 sign up 페이지에서 텍스트 박스에 글을(form) 써서 서버로 보내면
    서버는 UserCreationForm 으로 부터 각 내용들을 받아서 처리한다
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is created successfully!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def book_list(request):
    books = Book.objects.order_by('-created_date')
    return render(request, 'core/book_list.html', {'books': books})


def report_list(request, slug):
    book = Book.objects.get(slug=slug)
    reports = book.report_set.all()
    return render(request, 'core/report_list.html', {'reports': reports, 'book': book})


def report_contents(request, slug):
    report = Report.objects.get(slug=slug)

    author = User.objects.get(uid=report.uid)
    author_full_name = author.first_name + author.last_name
    context = {'report': report,
               'author': author_full_name, }
    return render(request, 'core/report_contents.html', context)


def report_edit(request, slug):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.uid = request.user.uid
            report.book = Book.objects.get(slug=slug)
            report.save()

            author = User.objects.get(uid=report.uid)
            author_full_name = author.first_name + author.last_name

            context = {'report': report,
                       'author': author_full_name, }
            return render(request, 'core/report_contents.html', context)
    else:
        form = ReportForm()
    return render(request, 'core/report_edit.html', {'form': form})
