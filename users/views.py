from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from users.forms import CreateUserForm, CreateProfileForm, EditUserForm, EditProfileForm
from users.models import Profile


class RegisterView(View):
    def get(self, request):
        user_form = CreateUserForm()
        profile_form = CreateProfileForm()
        return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        user_form = CreateUserForm(request.POST)
        profile_form = CreateProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user,
                                             birth_date=profile_form.cleaned_data['birth_date'])
            return render(request, 'registration/register_done.html', {'new_user': new_user})


class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)
        return render(request, 'registration/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return redirect('')
