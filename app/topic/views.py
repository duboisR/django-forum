from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import reverse
from django.views.generic import ListView, CreateView, TemplateView

import topic.models
from topic.mixins import QueryparamMixins


# Create your views here.
class TopicListView(LoginRequiredMixin, QueryparamMixins, ListView):
    template_name = 'topic/topic_list.html'
    model = topic.models.Topic
    context_object_name = 'topic_list'
    paginate_by = 5

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
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


class TopicMessageView(LoginRequiredMixin, QueryparamMixins, CreateView):
    template_name = 'topic/topic_detail.html'
    model = topic.models.TopicMessage
    fields = ['message', ]

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['topic_instance'] = topic.models.Topic.objects.get(pk=self.kwargs.get('topic_pk'))
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.topic = topic.models.Topic.objects.get(pk=self.kwargs.get('topic_pk'))
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return "%s?%s" % (reverse('topic_detail', kwargs={'topic_pk': self.kwargs.get('topic_pk')}), self.request.GET.urlencode())



class TopicCreateView(LoginRequiredMixin, QueryparamMixins, CreateView):
    template_name = 'topic/topic_create.html'
    model = topic.models.Topic
    fields = ['title', 'description', ]

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return "%s?%s" % (reverse('topic_detail', kwargs={'topic_pk': self.object.pk}), self.request.GET.urlencode())


class TopicReactListView(QueryparamMixins, TemplateView):
    template_name = 'topic/topic_react_list.html'


class TopicReactMessageView(QueryparamMixins, TemplateView):
    template_name = 'topic/topic_react_detail.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['topic_instance'] = topic.models.Topic.objects.get(pk=self.kwargs.get('topic_pk'))
        return context