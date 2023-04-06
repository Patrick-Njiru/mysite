from django.shortcuts import get_object_or_404, render
from .models import Question

def index(request):
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    return render(request, 'polls/index.html', {'latest_questions_list': latest_questions_list}) 

def detail(request, question_id):
        # pk - primary key / alternative for id
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/vote.html', {'question': question})