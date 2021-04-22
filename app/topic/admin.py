from django.contrib import admin
from django.utils.translation import ugettext as _

import topic.models


class TopicMessageInline(admin.TabularInline):
    model = topic.models.TopicMessage
    verbose_name = _("Topic (Message)")
    verbose_name_plural = _("Topic (Messages)")
    extra = 1


@admin.register(topic.models.Topic)
class TopicAdmin(admin.ModelAdmin):
    model = topic.models.Topic

    list_display = (
        'title', 'is_solved', 'creator', 'created_at', )
    date_hierarchy = 'created_at'

    readonly_fields = ('created_at', )
    inlines = [TopicMessageInline, ]