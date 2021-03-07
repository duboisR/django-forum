from django.views.generic import TemplateView


class LoginTemplateView(TemplateView):
    template_name = 'main/login.html'

class RegisterTemplateView(TemplateView):
    template_name = 'main/register.html'

class ResetPwdFormTemplateView(TemplateView):
    template_name = 'main/reset_pwd_form.html'

class ResetPwdDoneTemplateView(TemplateView):
    template_name = 'main/reset_pwd_done.html'

class ResetPwdConfirmTemplateView(TemplateView):
    template_name = 'main/reset_pwd_confirm.html'

class ResetPwdCompleteTemplateView(TemplateView):
    template_name = 'main/reset_pwd_complete.html'

class TopicListTemplateView(TemplateView):
    template_name = 'main/topic_list.html'

class TopicDetailTemplateView(TemplateView):
    template_name = 'main/topic_detail.html'

class TopicCreateTempalteView(TemplateView):
    template_name = 'main/topic_create.html'