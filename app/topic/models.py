from django.db import models
from django.utils.translation import ugettext as _


class Topic(models.Model):
    title = models.CharField(
        verbose_name=_("Titre"),
        max_length=255)
    description = models.TextField(
        verbose_name=_("Description"))

    is_solved = models.BooleanField(
        verbose_name=_("Est resolu ?"),
        default=False)

    creator = models.ForeignKey(
        'user.User',
        verbose_name=_("Créateur"),
        on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(
        verbose_name=_("Date de création"),
        auto_now_add=True)

    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")

    def __str__(self):
        return self.title


class TopicMessage(models.Model):
    topic = models.ForeignKey(
        'topic.Topic',
        verbose_name=_("Topic"),
        on_delete=models.SET_NULL, null=True)
    message = models.TextField(
        verbose_name=_("Description"))

    creator = models.ForeignKey(
        'user.User',
        verbose_name=_("Créateur"),
        on_delete=models.SET_NULL, null=True)    
    created_at = models.DateTimeField(
        verbose_name=_("Date de création"),
        auto_now_add=True)

    class Meta:
        verbose_name = _("Topic - Message")
        verbose_name_plural = _("Topic - Messages")

    def __str__(self):
        return "%s - %s" % (self.topic, self.message[:15])
