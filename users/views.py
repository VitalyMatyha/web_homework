from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView

from .forms import UserRegisterForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        response = super().form_valid(form)

        send_mail(
            subject='Добро пожаловать!',
            message='Спасибо за регистрацию!',
            from_email=None,
            recipient_list=[form.instance.email],
        )

        return response


class UserLoginView(LoginView):
    template_name = 'users/login.html'