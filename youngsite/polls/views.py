from django.http import HttpResponse, Http404
from .models import Question
from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Questions does not exist")
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


"""
Question “인덱스” 페이지 – 최신 몇개의 질문들을 보여주는 페이지.
Question “디테일” 페이지 – 투표를 할 수 있는 유저폼과 함께 하나의 질문을 보여주는 페이지.
Question “결과” 페이지 – 특정 질문에 대한 결과를 보여주는 페이지.
투표 액션 – 특정 질문에 대해 투표를 핸들링.
"""