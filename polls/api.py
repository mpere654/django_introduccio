
from django.http import JsonResponse
from polls.models import *
 



#...
 
def get_questions(request):
    #obtenemos todas las Question
    jsonData = list( Question.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "questions": jsonData,
        }, safe=False)

#proteger api
from django.contrib.auth.decorators import login_required
 #proteger api con decorador, si logueas panel admin funciona ya el login
#@login_required
def get_choices(request, question_id):
    print(request.user)
    jsonData = list( Choice.objects.filter(question_id=question_id).values() )
    return JsonResponse({
            "status": "OK",
            "choices": jsonData,
        }, safe=False)
