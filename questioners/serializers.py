from rest_framework import serializers
from questioners.models import Question, Answer, Category


class QuestionSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    answers = serializers.SerializerMethodField()
    img = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    @staticmethod
    def get_answers(self):
        ans_objs = Answer.objects.filter(question=self)
        print(ans_objs)
        data = []
        for ans in ans_objs:
            data.append({'answer': ans.answer, 'is_correct': ans.is_true})
        return data

    @staticmethod
    def get_category(self):
        return self.category.category_name

    @staticmethod
    def get_img(obj):
        if obj.img:
            s = 'http://127.0.0.1:8000' + obj.img.url
            return s


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
