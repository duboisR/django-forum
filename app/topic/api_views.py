from rest_framework import generics

from django.db.models import Count

import topic.models
import topic.serializer

class TopicListAPIView(generics.ListAPIView):
    """
    Returns a list of **selected** topics in the system.
    """

    queryset = topic.models.Topic.objects.all()
    serializer_class = topic.serializer.TopicSerializer

    def get_queryset(self):
        """
        Return the list of items for this view.
        """
        queryset =  super().get_queryset()

        queryparam_filter = self.request.GET.get('filter', 'all')
        if queryparam_filter == 'solved':
            queryset = queryset.filter(is_solved=True)
        elif queryparam_filter == 'unsolved':
            queryset = queryset.filter(is_solved=False)
        elif queryparam_filter == 'noreplies':
            queryset = queryset.annotate(num_messages=Count('topicmessage')).filter(num_messages=0)

        queryparam_search = self.request.GET.get('search', '')
        if queryparam_search:
            queryset = queryset.filter(title__icontains=queryparam_search)

        return queryset


class TopicRetrieveAPIView(generics.RetrieveAPIView):
    """
    Returns the **selected** topic informations.
    """

    queryset = topic.models.Topic.objects.all()
    serializer_class = topic.serializer.TopicRetrieveSerializer


class TopicMessageCreateAPIView(generics.CreateAPIView):
    """
    Create message linked to a **specific** topic.
    """

    queryset = topic.models.TopicMessage.objects.all()
    serializer_class = topic.serializer.TopicMessageSerializer