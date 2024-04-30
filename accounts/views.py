from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpCustom

class SignUpView(CreateView):
    form_class = SignUpCustom
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'



