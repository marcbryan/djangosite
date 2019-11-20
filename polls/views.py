from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Question, Answer

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# /exampleList/
def exampleList(request):
    list = Question.objects.all()
    return render(request, "example.html",
        {
            "type":"cosas",
            "elements":list
        }
    )

def llista(request):
    items = None
    if request.GET.get("qid"):
        items = Answer.objects.filter(question_id__id = request.GET["qid"])
    else:
        items = Answer.objects.all()
    return render( request, "example.html",
                    {
                        "type":"cosas",
                        "elements":items
                    }
                )
