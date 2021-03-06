from django.views import View
from accounts.models import CustomUser
from accounts.forms import ProfileForm, SignupUserForm, SignupStaffForm
from django.shortcuts import render, redirect
from allauth.account import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

# Create your views here.
class SignupView(views.SignupView):
    template_name = 'accounts/signup.html'
    form_class = SignupUserForm

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        return context

class StaffSignupView(views.SignupView):
    template_name = 'accounts/staff_signup.html'
    form_class = SignupStaffForm

    def dispatch(self, request, *args, **kwargs):
        response = super(FormView, self).dispatch(request, *args, **kwargs)
        return response

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        form = SignupStaffForm(request.POST or None)
        return render(request, 'accounts/staff_signup.html', {
            'form': form
        })

class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)

        return render(request, 'accounts/profile.html', {
            'user_data': user_data,
        })

class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        form = ProfileForm(
            request.POST or None,
            initial={
                'image': user_data.image,
                'name': user_data.name,
                'furigana': user_data.furigana,
                'description': user_data.description,
            }
        )

        return render(request, 'accounts/profile_edit.html', {
            'form': form,
            'user_data': user_data
        })

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user_data = CustomUser.objects.get(id=request.user.id)
            user_data.name = form.cleaned_data['name']
            user_data.furigana = form.cleaned_data['furigana']
            user_data.description = form.cleaned_data['description']
            if request.FILES.get('image'):
                user_data.image = request.FILES.get('image')
            user_data.save()
            return redirect('profile')

        return render(request, 'accounts/profile.html', {
            'form': form
        })