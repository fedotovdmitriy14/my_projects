from rest_framework import serializers

from movies.models import Watchlist, Platform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)            # чтобы показывал имя юзера

    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    # reviews = serializers.StringRelatedField(many=True, read_only=True)
    reviews = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='review_detail',  # это ссылка на конкретный фильм, а также нужно добавить context={'request': request} во вьюху
    )

    class Meta:
        model = Watchlist
        # fields = '__all__'
        exclude = ['avg_rating_previous',]

    def name_length(value):
        if len(value) < 2:
            raise serializers.ValidationError("name is too short")

    def validate_score(self, value):
        if value > 10:
            raise serializers.ValidationError('Score should be from 0 to 10')
        else:
            return value

    def validate_object(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError('Title and description should be different!')
        else:
            return data

class PlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)
    watchlist = serializers.StringRelatedField(many=True, read_only=True)               # возвращает def __str__
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='obj',    # это ссылка на конкретный фильм, а также нужно добавить context={'request': request} во вьюху
    # )



    class Meta:
        model = Platform
        fields = '__all__'





# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     score = serializers.IntegerField()
#     len_name = serializers.SerializerMethodField()
#
#     def get_len_name(self, object):
#         return len(object.name)
#
#     def validate_score(self, value):
#         if value > 10:
#             raise serializers.ValidationError('Score should be from 0 to 10')
#         else:
#             return value
#
#     def validate_object(self, data):
#         if data['score'] == data['name']:
#             raise serializers.ValidationError('NO')
#         else:
#             return data
#
#     def create(self, validated_data):
#         with open('log.txt', 'w') as f:
#             f.write(str(validated_data))
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.score = validated_data.get('score', instance.score)
#         instance.save()
#         return instance