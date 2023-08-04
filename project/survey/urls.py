from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions', views.questions, name='view_questions_list'),
    path('add', views.add_question_form, name='view_add_question'),
    path('add/success', views.add_question, name='add_question'),
    
    
    path('api/get_survey_list', views.api_get_survey_list, name='api_get_survey_list'),
    path('api/survey', views.SurveyClass.as_view(), name='api_survey'),
    
    path('api/create_survey', views.CreateSurveyClass.as_view(), name='api_create_survey'),
    # path('api/questions', views.api_questions, name='api_questions'),
    # path('api/add_question', views.api_add_question, name='api_add_question'),
    path('api/add_question', views.AddQuestion.as_view(), name='api_add_question'),
    path('api/get_response', views.GetResponse.as_view(), name='api_get_survey_response'),
    path('api/rename_survey', views.RenameSurvey.as_view(), name='api_rename_survey'),
    path('api/open_survey', views.OpenSurvey.as_view(), name='api_open_survey'),
    path('api/close_survey', views.CloseSurvey.as_view(), name='api_close_survey'),
]