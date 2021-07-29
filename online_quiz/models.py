from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class school_staff_admin(models.Model):
    school_staff_admin_empid=models.IntegerField(primary_key=True)
    school_staff_admin_name=models.CharField(max_length=50)
    school_staff_admin_password=models.CharField(max_length=8)
    def __str__(self):
        return self.school_staff_admin_name


class new_quiz_register(models.Model):
    quiz_name=models.CharField(max_length=50,default='demo')
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class quiz_question_bank(models.Model):
    quiz_question=models.CharField(max_length=100,default='demo')
    quiz_option1=models.CharField(max_length=100,default='demo')
    quiz_option2=models.CharField(max_length=100,default='demo')
    quiz_option3=models.CharField(max_length=100,default='demo')
    quiz_option4=models.CharField(max_length=100,default='demo')
    quiz_answer=models.CharField(max_length=100,default='demo')
