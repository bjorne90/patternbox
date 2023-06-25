from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import UserRegistrationForm, UserUpdateForm, PatternForm
from .models import Pattern


class UserLoginView(LoginView):
    template_name = 'profiles/login.html'
    success_url = reverse_lazy('profiles:profile')

    def form_valid(self, form):
        print(form.cleaned_data)  # Print form data for debugging purposes
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    pass


class UserRegistrationView(TemplateView):
    template_name = 'profiles/registration.html'


@login_required
def profile_view(request):
    return render(request, 'profiles/profile.html')


@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    return render(request, 'profiles/profile_edit.html', {'user_form': user_form})


@login_required
def pattern_upload(request):
    if request.method == 'POST':
        pattern_form = PatternForm(request.POST, request.FILES)
        if pattern_form.is_valid():
            pattern = pattern_form.save(commit=False)
            pattern.creator = request.user
            pattern.save()
            return redirect('profile')
    else:
        pattern_form = PatternForm()
    return render(request, 'profiles/pattern_upload.html', {'pattern_form': pattern_form})


@login_required
def pattern_list(request):
    patterns = Pattern.objects.filter(creator=request.user)
    return render(request, 'profiles/pattern_list.html', {'patterns': patterns})

