from django.shortcuts import render
from . import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from online_quiz.models import new_quiz_register
from online_quiz.models import quiz_question_bank
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator,EmptyPage,InvalidPage
import time


lst=[]
anslist=[]
answers=quiz_question_bank.objects.all()
for i in answers:
    anslist.append(i.quiz_answer)


# Create your views here.


class homepage(ListView):
    model=new_quiz_register
    template_name='online_quiz/homepage.html'
    context_object_name='temp'


class exam_ready_page(DetailView):
    model=new_quiz_register
    template_name='online_quiz/exam_homepage.html'

    context_object_name='aaa'



@login_required
def staff_login(inn):
    return render(inn,'online_quiz/homepage.html')

@login_required
def thank_you(request):
    return render(request,'online_quiz/thank_you.html')


@login_required
def create_quiz(request):
    form=forms.new_quiz_register()
    if request.method=='POST':
        form=forms.new_quiz_register(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
    return render(request,'online_quiz/create_quiz_final.html',{'form':form})


total_time=[]
def quiz(request):
    total_time.append(time.perf_counter())
    obj=quiz_question_bank.objects.all()[:10]
    paginator=Paginator(obj,1)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        questions=paginator.page(page)
    except(EmptyPage,InvalidPage):
        questions=paginator.page(paginator.num_pages)

    dict={'obj':obj,'questions':questions}
    return render(request,'online_quiz/exam_homepage1.html',context=dict)





def result(request):

    score=0;
    temp="result status"
    percentage=0;
    for i in range(len(lst)):
        if lst[i]==anslist[i]:
            score+=1
    percentage=((int(score))/10)*100
    if percentage<33:
        temp="Fail"
    else:
        temp="Pass"
    time_update=int(total_time[9]-total_time[0])
    return render(request,'online_quiz/results.html',{"score":score,"percentage":percentage,"temp":temp,"time_update":time_update})



def saveans(request):
    ans=request.GET['ans']
    lst.append(ans)



