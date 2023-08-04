from django.db import models
from login.models import User

# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000, blank=True)
    active = models.BooleanField(default=True)
    url = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    create_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    
    def __str__(self):
        return str(self.id) + '. ' + str(self.title)
    

class Question(models.Model):
    TEXT = 'text'
    MULTICHOICE = 'multi'
    SINGLECHOICE = 'single'
    QUESTION_TYPE_CHOICES = (
        (TEXT, 'Text Question'),
        (MULTICHOICE, 'Multichoice Question (Choose multiple)'),
        (SINGLECHOICE, 'Multichoice Question (Choose one)'),
    )
    
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    order = models.IntegerField(blank=False, null=False)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    type = models.CharField(max_length=200, choices=QUESTION_TYPE_CHOICES, blank=False, null=False, default=TEXT)
    
    class Meta:
        unique_together = (('survey', 'order'),)
        ordering = ['order']
    
    def __str__(self):
        return str(self.id) + '. ' + str(self.text)
    
class SurveyResponse(models.Model):
    response_id = models.CharField(max_length=200, default='0')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField('date published', auto_now_add=True)
    
    def __str__(self):
        return  str(self.survey.title) + ' Response ' + str(self.response_id)
    

class MultipleChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + '. ' + str(self.text)
    
    
class Answer(models.Model):
    survey_repsonse = models.ForeignKey(SurveyResponse, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    value = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.id) + '. ' + str(self.survey_repsonse.response_id) + '.' + str(self.question.text) + ': ' + str(self.value)
    