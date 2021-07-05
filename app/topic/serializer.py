from rest_framework import serializers

import topic.models
import user.models

class TopicCreatorSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField(read_only=True)
    avatar_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = user.models.User
        fields = ['email', 'avatar_url', 'first_name', 'last_name', 'fullname', ]

    def get_fullname(self, obj):
        return obj.get_fullname()

    def get_avatar_url(self, obj):
        return obj.get_avatar_url()


class TopicSerializer(serializers.ModelSerializer):
    creator_serializer = TopicCreatorSerializer(source='creator', read_only=True)
    topicmessage_count = serializers.SerializerMethodField(read_only=True)
    topicmessage_last = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = topic.models.Topic
        fields = ['id', 'title', 'description', 'topicmessage_count', 'topicmessage_last', 'creator_serializer', 'created_at']

    def get_topicmessage_count(self, obj):
        return obj.topicmessage_set.count()

    def get_topicmessage_last(self, obj):
        last_message = obj.topicmessage_set.last()
        if last_message:
            return {
                'creator_name': last_message.creator.get_fullname(),
                'created_at': last_message.created_at
            }
        return None

    def create(self, validated_data):
        obj = topic.models.Topic.objects.create(creator=self.context['request'].user, **validated_data)
        return obj

# TopicMessage
class TopicMessageSerializer(serializers.ModelSerializer):
    creator_serializer = TopicCreatorSerializer(source='creator', read_only=True)

    class Meta:
        model = topic.models.TopicMessage
        fields = ['pk', 'message', 'creator_serializer', 'created_at', ]

    def create(self, validated_data):
        obj = topic.models.TopicMessage.objects.create(
            creator=self.context['request'].user,
            topic=topic.models.Topic.objects.get(pk=self.context['request'].parser_context.get('kwargs').get('topic_pk')),
            **validated_data)
        return obj


class TopicRetrieveSerializer(TopicSerializer):
    messages_serializer = TopicMessageSerializer(source='topicmessage_set', many=True, read_only=True)

    class Meta:
        model = topic.models.Topic
        fields = ['id', 'title', 'description', 'topicmessage_count', 'messages_serializer', 'creator_serializer', 'created_at']
