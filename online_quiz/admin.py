from django.contrib import admin
from online_quiz.models import school_staff_admin
from online_quiz.models import quiz_question_bank

# Register your models here.
class school_staff_admin_class(admin.ModelAdmin):
    list_display=['school_staff_admin_empid','school_staff_admin_name','school_staff_admin_password']
admin.site.register(school_staff_admin,school_staff_admin_class)

class quiz_question_class(admin.ModelAdmin):
    list_display=['quiz_question','quiz_option1','quiz_option2','quiz_option3','quiz_option4','quiz_answer']
admin.site.register(quiz_question_bank,quiz_question_class)
