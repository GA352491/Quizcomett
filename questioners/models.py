from django.db import models

# Create your models here.
from django.db import models

from accounts.models import CustomUser


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    category_name = models.CharField(max_length=100, blank=True, null=True)
    time_frame = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.category_name


class Question(BaseModel):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='question_images', null=True, blank=True)
    question = models.TextField(blank=True, null=True)
    sub_question = models.TextField(blank=True, null=True)
    marks = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.category}-{self.question}'


class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='question_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='answer_images', null=True, blank=True)
    is_true = models.BooleanField(default=False)
    paragraph = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.answer


class QuizHistory(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    submitted_answers = models.JSONField()
    marks_obtained = models.IntegerField()
    completed = models.BooleanField()

    def __str__(self):
        return self.user


class Sets(models.Model):
    set_name = models.CharField(max_length=10, blank=True, null=True)
    questions = models.ManyToManyField(Question, null=True, blank=True)

    class Meta:
        verbose_name = 'Sets'
        verbose_name_plural = "Sets"

    def __str__(self):
        return self.set_name
