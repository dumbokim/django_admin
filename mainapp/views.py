from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# from django.http import HttpResponse
from .models import Table2

# Create your views here.

'''
def index(request):
    """
    question 목록 출력
    """
    question_list = Table2.objects.order_by('-id')
    context = {'question_list': question_list}
    return render(request, 'mainapp/question_list.html', context)


def detail(request, question_id):
    """
    내용 출력
    """
    question = get_object_or_404(Table2, id=question_id)
    context = {'question': question}
    return render(request, 'mainapp/question_detail.html', context)


def answer_create(request, question_id):
    """
    답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('mainapp:detail', question_id=question.id)

'''