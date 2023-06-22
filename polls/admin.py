from django.contrib import admin

from .models import *


#clase para hace inline del modelo Choice
class ChoiceInline(admin. TabularInline): # StackedInline): #formato de vision en admin
    model = Choice #diem el model
    extra = 1 #numero de opciones de la clase choice para editar nuevas


#permite editar en el admin los campos concretos, ModelAdmin visualiza el modelo
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    #exclude = []
    readonly_fields = ["pub_date"]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_editable = ["pub_date"]
    #busqueda de campos
    search_fields = ["question_text","pub_date"]

    #inlines veure els registres relacionats Foreing key (question - N choice)
    inlines = [ChoiceInline]


#registrar edición clase BD
admin.site.register(Question, QuestionAdmin) #marcamos las condiciones de acceso 
admin.site.register(Choice)
admin.site.register(Vote)