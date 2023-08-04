from django.contrib import admin

# Register your models here.

from .models import Survey, Question, SurveyResponse, MultipleChoice, Answer

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(SurveyResponse)

admin.site.register(MultipleChoice)
admin.site.register(Answer)