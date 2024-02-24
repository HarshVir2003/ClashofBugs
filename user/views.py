from .forms import NewUserForm, LoginForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth.backends import ModelBackend
from django.views.decorators.csrf import csrf_protect


class UserSignupPage(FormView):
    template_name = "backend/signup.html"
    form_class = NewUserForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        User = get_user_model()
        user = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
        )
        user.backend = f"{user._meta.app_label}.{ModelBackend.__name__}"
        login(self.request, user)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        # Your custom logic for handling GET requests (optional)
        return super().get(request, *args, **kwargs)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


@login_required
def user_logout(request):
    logout(request)
    return redirect('users:home')


class CustomLoginView(LoginView):
    template_name = 'backend/login.html'
    form_class = LoginForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        # Your custom logic after successful login (optional)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        # Your custom logic after failed login (optional)
        return response

    def get_success_url(self):
        # Your custom logic for redirect after successful login
        return reverse('users:home')  # Replace with your actual success URL

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Your custom logic for handling POST requests (optional)
        return super().post(request, *args, **kwargs)


class HomePage(View):
    template_name = "backend/1home_update.html"

    def get(self, request):
        return render(request, self.template_name, {"request": request})
