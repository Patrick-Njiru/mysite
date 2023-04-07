from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    """ model to add choice fields when creating or modifying a question """
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """ Change the appearance of the questions form or page. """
    fieldsets = [
        ("Date infromation", {"fields": ["pub_date"]}),
        ("Question", {"fields": ["question_text"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["pk", "question_text", "pub_date", "was_published_recently"]
    """ Add method to filter by and maybe editable cells in the table by the two methods below. Try other methods."""
    list_filter = ['pub_date']
    # list_editable = ['question_text']
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
