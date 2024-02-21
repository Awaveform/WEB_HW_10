from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm, LoginForm, ProfileForm


# def sign_up_user(request):
#     if request.user.is_authenticated:
#         return redirect(to='quote:main')
#
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='quote:main')
#         else:
#             return render(
#                 request,
#                 'users/sign_up.html',
#                 context={"form": form}
#             )
#
#     return render(
#         request,
#         'users/sign_up.html',
#         context={"form": RegisterForm()}
#     )
def sign_up_user(request):
    if request.user.is_authenticated:
        return redirect(to='quote:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save()

            # Log in the user
            login(request, user)

            # Redirect to the main page or another appropriate page
            return redirect(to='quote:main')
        else:
            return render(
                request,
                'users/sign_up.html',
                context={"form": form}
            )

    return render(
        request,
        'users/sign_up.html',
        context={"form": RegisterForm()}
    )


def login_user(request):
    if request.user.is_authenticated:
        return redirect(to='quote:main')

    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            messages.error(
                request, 'Username or password didn\'t match'
            )
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quote:main')

    return render(
        request,
        'users/login.html',
        context={"form": LoginForm()}
    )


@login_required
def logout_user(request):
    logout(request)
    return redirect(to='quote:main')


# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')


@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if profile_form.is_valid():
            profile_form.save()
            messages.success(
                request,
                'Your profile is updated successfully'
            )
            return redirect(to='users:profile')

    profile_form = ProfileForm(instance=request.user.profile)
    return render(
        request,
        'users/profile.html',
        {'profile_form': profile_form}
    )
