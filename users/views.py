from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.forms import RegisterForm


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'home.html'  # Шаблон для логина
    success_url = reverse_lazy('website')  # После входа перенаправлять на страницу website


# ___  не могу настройить работу данного метода использовал def___
# class UserLogoutView(LogoutView):
#     form_class = AuthenticationForm
#     next_page = 'home'  # Перенаправление после выхода

def logout_view(request):
    logout(request)
    return redirect('home')

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('website')

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)


@login_required
def website_view(request):
    print("webserver_view вызван")
    return render(request, template_name='website.html')


