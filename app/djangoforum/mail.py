from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend

class CustomEmailBackend(EmailBackend):
    """ Custom Email backend used in the project """
    def send_messages(self, messages):
        for message in messages:
            # if settings.DEBUG is enabled we want to send the e-mail to a specific debug e-mail instead of
            # sending it to end users. This way while deployed in local and DEV, e-mails are not send to real people.
            if settings.DEBUG:
                message.subject = "{subject} [{to}]".format(
                    subject=message.subject,
                    to=', '.join(message.to)
                )
                message.to = [settings.DEBUG_EMAIL]
        return super(CustomEmailBackend, self).send_messages(messages)


# Documentation
# https://docs.djangoproject.com/fr/3.0/topics/email/


# Quick example
#
# from django.core.mail import send_mail
# send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)

# Html Template example
#
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# msg_plain = render_to_string('templates/email.txt', {'some_params': some_params})
# msg_html = render_to_string('templates/email.html', {'some_params': some_params})
# send_mail('Subject here', msg_plain, 'from@example.com', ['to@example.com'], html_message=msg_html, fail_silently=False)
