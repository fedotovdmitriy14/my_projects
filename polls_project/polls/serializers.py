from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from polls.models import Poll, Question, Choice, Answer


class CurrentUserDefault(object):
    def set_context(self, serializer_field):
        self.user_id = serializer_field.context['request'].user.id

    def __call__(self):
        return self.user_id

class PollSerializer(serializers.ModelSerializer):

    questions = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'


    def update(self, instance, validated_data):
        if 'start_date' in validated_data:
            raise serializers.ValidationError({'Нельзя изменить поле start_date'})
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

    def validate(self, attrs):
        try:
            obj = Choice.objects.get(question=attrs['question'].id, text=attrs['text'])
        except Choice.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('Этот вариант уже указан')


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

    def validate(self, attrs):
        question_type = attrs['question_type']
        if question_type == 'text' or question_type == 'single' or question_type == 'multiple':
            return attrs
        raise serializers.ValidationError('Неправильно задан тип вопроса. Тип вопроса может быть только text, single '
                                          'или multiple')



class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(default=CurrentUserDefault())
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='id')
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice = serializers.SlugRelatedField(queryset=Choice.objects.all(), slug_field='id', allow_null=True)
    choice_text = serializers.CharField(max_length=200, allow_null=True, required=False)

    class Meta:
        model = Answer
        fields = '__all__'


    def validate(self, attrs):
        question_type = Question.objects.get(id=attrs['question'].id).question_type
        try:
            if question_type == "single" or question_type == "text":
                obj = Answer.objects.get(question=attrs['question'].id, poll=attrs['poll'],
                                         user_id=attrs['user_id'])
            elif question_type == "multiple":
                obj = Answer.objects.get(question=attrs['question'].id, survey=attrs['survey'],
                                         user_id=attrs['user_id'],
                                         choice=attrs['choice'])
        except Answer.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('Вы уже отвечали на этот вопрос')