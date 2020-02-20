from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import generic
from django.contrib.auth import views
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "signup.html"


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('tools/base.html')
    template_name = 'registration/login.html'
