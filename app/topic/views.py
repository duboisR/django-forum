from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

import topic.models


# Create your views here.
class TopicListView(LoginRequiredMixin, ListView):
    template_name = 'topic/topic_list.html'
    model = topic.models.TopicMessage

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['queryparam_filter']  = self.request.GET.get('filter', 'all')
        context['queryparam_search']  = self.request.GET.get('search', '')
        return context


class TopicMessageView(LoginRequiredMixin, CreateView):
    template_name = 'topic/topic_detail.html'
    model = topic.models.TopicMessage
    fields = ['message', ]

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['topic_instance'] = topic.models.Topic.objects.get(pk=kwargs.get('topic_pk'))
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.topic = topic.models.Topic.objects.get(pk=kwargs.get('topic_pk'))
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class TopicCreateView(LoginRequiredMixin, CreateView):
    template_name = 'topic/topic_create.html'
    model = topic.models.Topic
    fields = ['title', 'description', ]

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)
