from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

class Question(models.Model):
    """ the string question and date published inside the parenthesis are used in the admins page in place of the variable names when provided """
    question_text = models.CharField("question", max_length=200)
    pub_date = models.DateTimeField("date published")

    # for convenience when dealing with interactvie prompts
    def __str__(self):
        return self.question_text
    
    @admin.display(
            boolean=True,
            ordering="pub_date",
            description="Published recently",
    )
    
    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
