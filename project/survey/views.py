from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404
from django.views import View
from django.core.validators import RegexValidator

from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import json
import string
import random

from .models import Survey
from .models import Question
from .models import SurveyResponse
from .models import MultipleChoice
from .models import Answer

from .permissions import CanManageAdmin, CanManageUser, CanManageSurvey, CanViewResponses, Anyone

myname = 'Egnaro'


def index(request):
    questions = [
        'This is the first question.',
        'This is the second question.',
        'This is the third question.',
        'This is the fourth question.',
        'This is the fifth question.',
    ]

    context = {'name': myname, 'questions_list': questions}
    return render(request, 'survey/index.html', context)


def questions(request):
    questions = Question.objects.all()

    context = {'questions_list': questions, 'name': myname}
    return render(request, 'survey/questions.html', context)


def view_detail_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context = {'name': myname, 'question': question}
    return render(request, 'survey/detail_question.html', context)


def add_question_form(request):
    return render(request, 'survey/add_question_form.html')


def add_question(request):
    question_text = request.POST['question_text']
    question = Question()
    question.text = question_text
    question.save()

    context = {'question_text': question_text}
    return render(request, 'survey/add_question_success.html', context)


# User

class GetSurveyListClass(APIView):
    pass


class GetSurveyDetailClass(APIView):
    pass


def api_get_survey_list(request):
    survey_list = Survey.objects.filter(active=True).all()
    json_date = list(survey_list.values('id', 'title', 'description', 'url'))
    return JsonResponse(json_date, safe=False)


# def api_get_survey_detail(request):
#     survey_id = request.GET['survey_id']

#     survey = get_object_or_404(Survey, pk=survey_id)
#     if survey.active:
#         survey_data = {
#             'id': survey.id,
#             'title': survey.title,
#             'description': survey.description,
#         }

#         questions = Question.objects.filter(survey_id = survey.id)

#         questions_list = []

#         for question in questions:
#             question_data = {
#                     'id': question.id,
#                     'text': question.text,
#                     'type': question.type,
#                 }

#             if question.type == 'multiple_choice':
#                 choices_list = []

#                 choices = MultipleChoice.objects.filter(question_id = question.id)
#                 for choice in choices:
#                     choice_data = {
#                         'id': choice.id,
#                         'text': choice.text,
#                         'multi_choice': choice.multi_choice,
#                     }
#                     choices_list.append(choice_data)

#                 question_data['choices'] = choices_list

#             if question.type == 'text':
#                 pass

#             questions_list.append(question_data)

#         survey_data['questions'] = questions_list

#         return JsonResponse(survey_data, safe=False)
#     return HttpResponse('This survey is not recieving responses.') 

# def api_response(request):
#     json_data = json.loads(request.body)
#     survey_id = json_data['survey_id']
#     response_data = json_data['data']


#     if Survey.objects.filter(id = survey_id).exists():
#         survey = get_object_or_404(Survey, id=survey_id)
#         if survey.active == True:
#             response_id = ''
#             while True:
#                 random_string = ''.join((random.choice(string.ascii_lowercase) for x in range(10)))
#                 response_id = survey_id + '_' + random_string
#                 if SurveyResponse.objects.filter(response_id = response_id).exists():
#                     continue
#                 else:
#                     break

#             response = SurveyResponse()
#             response.survey_id = survey_id
#             response.response_id = response_id

#             response_valid = True
#             for answer in response_data:
#                 if Question.objects.filter(id = answer['question_id']).exists():
#                     continue
#                 else :
#                     response_valid = False
#                     break

#             if response_valid == True:
#                 response.save()
#                 for answer in response_data:
#                     answer_data = Answer()

#                     answer_data.survey_repsonse_id = get_object_or_404(SurveyResponse, response_id = response_id).id
#                     answer_data.question_id = answer['question_id']
#                     answer_data.value = answer['value']
#                     answer_data.save()

#                 return HttpResponse('Your response ID is ' + response_id + '.')
#             else:
#                 return HttpResponse('Response Invalid')

#         else:
#             return HttpResponse('This survey is not recieving responses.')

#     else:
#         return HttpResponse('Response Invalid')

class SurveyClass(APIView):
    permission_classes = (Anyone,)

    def get(self, request):
        survey_id = request.GET['survey_id']
        survey = get_object_or_404(Survey, pk=survey_id)
        if survey.active:
            survey_data = {
                'id': survey.id,
                'title': survey.title,
                'description': survey.description,
            }

            questions = Question.objects.filter(survey_id=survey.id).order_by('order').all()

            questions_list = []

            for question in questions:
                question_data = {
                    'order': question.order,
                    'id': question.id,
                    'text': question.text,
                    'type': question.type,
                }

                if question.type == 'multi' or question.type == 'single':
                    choices_list = []

                    choices = MultipleChoice.objects.filter(question_id=question.id)
                    for choice in choices:
                        choice_data = {
                            'id': choice.id,
                            'text': choice.text,
                        }
                        choices_list.append(choice_data)

                    question_data['choices'] = choices_list

                if question.type == 'text':
                    pass

                questions_list.append(question_data)

            survey_data['questions'] = questions_list

            return Response(survey_data, status=status.HTTP_200_OK)
        return HttpResponse('This survey is not recieving responses.')

    def post(self, request):
        user = request.user
        if user.username != None:
            uid = user.id
        else:
            uid = ''

        json_data = json.loads(request.body)
        survey_id = json_data['survey_id']
        response_data = json_data['data']

        if Survey.objects.filter(id=survey_id).exists():
            survey = get_object_or_404(Survey, id=survey_id)
            if survey.active == True:
                response_id = ''
                while True:
                    random_string = ''.join((random.choice(string.ascii_lowercase) for x in range(10)))
                    response_id = survey_id + '_' + random_string
                    if SurveyResponse.objects.filter(response_id=response_id).exists():
                        continue
                    else:
                        break

                response = SurveyResponse()
                response.survey_id = survey_id
                response.user_id = uid
                response.response_id = response_id

                response_valid = True
                for answer in response_data:
                    if Question.objects.filter(id=answer['question_id']).exists():
                        continue
                    else:
                        response_valid = False
                        break

                if response_valid == True:
                    response.save()
                    for answer in response_data:
                        answer_data = Answer()

                        answer_data.survey_repsonse_id = get_object_or_404(SurveyResponse, response_id=response_id).id
                        answer_data.question_id = answer['question_id']
                        answer_data.value = answer['value']
                        answer_data.save()

                    return Response({'message': 'Response Sucessfull', 'response_id': response_id},
                                    status=status.HTTP_201_CREATED)

                else:
                    return Response({'message': 'Response Invalid'}, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({'message': 'This survey is not recieving responses.'},
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'message': 'Response Invalid'}, status=status.HTTP_400_BAD_REQUEST)


# Manager

class CreateSurveyClass(APIView):
    permission_classes = (IsAuthenticated, CanManageSurvey)

    def post(self, request):
        serializers = CreateSurveySerializer(data=request.data)
        if serializers.is_valid():
            survey = Survey()
            survey.title = serializers.validated_data['title']
            survey.description = serializers.validated_data['description']
            survey.url = serializers.validated_data['url']
            survey.create_user = request.user
            survey.save()
            return Response({'message': 'success'}, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class AddQuestion(APIView):
    permission_classes = (IsAuthenticated, CanManageSurvey)

    def post(self, request):
        json_data = request.data

        survey = Survey.objects.filter(id=json_data['survey_id']).first()

        if survey:
            question = Question()
            question.survey_id = json_data['survey_id']
            question.order = Question.objects.filter(survey_id=json_data['survey_id']).count() + 1
            question.text = json_data['question_text']
            question.type = json_data['question_type']

            if question.type in ['text', 'multi', 'single']:
                question.save()

                if question.type in ['multi', 'single']:
                    choices = json_data['question_choices']
                    for choice in choices:
                        new_choice = MultipleChoice()
                        new_choice.question = question
                        new_choice.text = choice['choice_text']
                        new_choice.multi_choice = choice['multi_choice']
                        new_choice.save()
                if question.type in ['text']:
                    pass

            else:
                return Response({'message': 'Question must be text, multi, single', 'code': 400},
                                status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'success', 'code': 201}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Survey not found', 'code': 404}, status=status.HTTP_404_NOT_FOUND)


class GetResponse(APIView):
    permission_classes = (IsAuthenticated, CanViewResponses)

    def get(self, request):
        survey_id = request.GET['survey_id']

        survey = get_object_or_404(Survey, pk=survey_id)
        json_data = {
            "id": survey.id,
            "title": survey.title,
            'responses': []
        }

        response_list = SurveyResponse.objects.filter(survey_id=survey_id).all()

        for response in response_list:
            response_data = {
                'response_id': response.response_id,
                'date': response.date,
                'data': [],
            }
            data = []
            answer_list = Answer.objects.filter(survey_repsonse_id=response.id).all()
            for answer in answer_list:
                answer_data = {
                    'question_id': answer.question_id,
                    'value': answer.value,
                }
                data.append(answer_data)
            response_data['data'] = data

            json_data['responses'].append(response_data)
            # responses.append(response_data)

        # json_data.append(responses)

        return Response(json_data, status=status.HTTP_200_OK)


class RenameSurvey(APIView):
    permission_classes = (IsAuthenticated, CanManageSurvey,)

    def put(self, request):
        survey_id = request.data['survey_id']
        new_title = request.data['new_title']

        survey = Survey.objects.filter(id=survey_id).first()
        if survey:
            survey.title = new_title
            survey.save()
            return Response({'message': 'success', 'survey_id': survey_id, 'new_title': new_title},
                            status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Survey not found'}, status=status.HTTP_404_NOT_FOUND)


class OpenSurvey(APIView):
    permission_classes = (IsAuthenticated, CanManageSurvey,)

    def put(self, request):
        survey_id = request.data['survey_id']
        survey = Survey.objects.filter(id=survey_id).first()
        if survey:
            if survey.active:
                return Response({'message': 'Survey is already open'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                survey.active = True
                survey.save()
                return Response({'message': 'success', 'survey_id': survey_id}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Survey not found'}, status=status.HTTP_404_NOT_FOUND)


class CloseSurvey(APIView):
    permission_classes = (IsAuthenticated, CanManageSurvey,)

    def put(self, request):
        survey_id = request.data['survey_id']
        survey = Survey.objects.filter(id=survey_id).first()
        if survey:
            if survey.active:
                survey.active = False
                survey.save()
                return Response({'message': 'success', 'survey_id': survey_id}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Survey is already close'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Survey not found'}, status=status.HTTP_404_NOT_FOUND)


class CreateSurveySerializer(serializers.ModelSerializer):
    url = serializers.CharField(validators=[
        RegexValidator(
            regex=r'^[a-z0-9-]+$',
            message='URL only allow lowercase characters, numbers, and hyphens.'
        )
    ])

    class Meta:
        model = Survey
        fields = ('title', 'description', 'url')
