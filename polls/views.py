from django.http import HttpResponse, HttpResponseRedirect

from .models import *

#clase para poder cargar plantillas
from django.template import loader

#para editar mensaje error 404
from django.http import Http404

from django.shortcuts import get_object_or_404, render


from django.urls import reverse
from .models import Choice, Question, Vote





# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    #obtener la lista con los 5 primeros
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #abrir template index.html
    template = loader.get_template("polls/index.html")
    #pasar los datos  con diccionario context
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

#evitar error al acceder un objeto
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        #tenemos la question, tenemos la pk, accedemos al voto (puede existir o no)
        #selected_vote = Vote.objects.get(pk = 1)
        print("clave del objeto ",selected_choice.pk)
        #selected_vote = Vote.objects.get(id = selected_choice.pk)
        try: 
            selected_vote = Vote.objects.get(id = selected_choice.pk)
        except ObjectDoesNotExist:
            selected_vote = Vote.objects.create(choice = selected_choice, votes= 0, vote_date = timezone.now(), ip = "test")
        print(selected_vote)
        selected_vote.votes += 1
        selected_vote.save()
        print("votado", selected_vote)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))    


from django import forms





class QuestionForm(forms.Form):

    question_text = forms.CharField(label="Pregunta:", max_length=100)
    #para que el campo date salga como selector fecha
    date = forms.DateTimeField(label="Data:")

def new_question(request):
    myform = QuestionForm()
    return render(request, "polls/new_question.html", {"form":myform})


def new_question_add(request):
    if request.method == "POST":
        #crear Question 
        form = QuestionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["question_text"]
            question = Question(question_text =text)
            question.pub_date =form.cleaned_data["date"]
            #salvamos el registro, deberia ir un try catch
            question.save()
            message = "Pregunta enregistrada correctament"
        return render(request,"polls/new_question_add.html", {"message":message})
    #ERROR: retorn a form
    return HttpResponseRedirect(reverse("polls:add_question"))




class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        #decimos que no excluya ningun campo
        exclude = () #("votes") #campo votes ejemplo inicial

def new_choice(request):
    #renderizamos
    form = ChoiceForm()
    #guardar los datos al enviar el formulario
    if request.method== "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"polls/new_choice_add.html", {"form":form})


def dynamic(request):
    #return HttpResponse("Form  dynamic")
    return render(request,"polls/dynamic.html")