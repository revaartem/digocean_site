from django.shortcuts import render, redirect
from .forms import UserRegistration, UserLogin
from main_page.models import InformationInContactUs, Footer
from django.contrib.auth import login, authenticate, logout


def registration_view(request):
    """
    View function of the registration page. Processed POST and GET requests.
    
    form - Registration form.\n
    information_in_contact_us - Object model InformationInContactUs.\n
    footer - Footer object model.\n
    user_manager - Checked if user have group 'manager' in his group list.\n
    user_auth - Is user authenticated or not.\n

    :param request: POST or GET request.
    :return: Render of the HTML-page with context.
    
    """
    form = UserRegistration(request.POST or None)
    information_in_contact_us = InformationInContactUs.objects.get()
    footer = Footer.objects.get()
    user_manager = request.user.groups.filter(name='manager').exists()
    user_auth = request.user.is_authenticated
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        data = {
            'user': new_user,
            'information_in_contact_us': information_in_contact_us,
            'footer': footer}
        return render(request, 'registration_done.html', context=data)

    data = {
        'form': form,
        'information_in_contact_us': information_in_contact_us,
        'footer': footer,
        'user_manager': user_manager,
        'user_auth': user_auth
    }
    return render(request, 'registration.html', context=data)


def login_view(request):
    """
    View function of the login page. Processed POST and GET requests.
    
    form - form from model UserLogin with GET request or None.\n
    next_get - Next page parameters.\n
    information_in_contact_us - Object model InformationInContactUs.\n
    footer - footer - Footer object model.\n
    user_manager - Checked if user have group 'manager' in his group list.\n
    user_auth - Is user authenticated or not.\n
    
    :param request: POST or GET request.
    :return: Render of the HTML-page with context.
    """
    form = UserLogin(request.POST or None)
    next_get = request.GET.get('next')
    information_in_contact_us = InformationInContactUs.objects.get()
    footer = Footer.objects.get()
    user_manager = request.user.groups.filter(name='manager').exists()
    user_auth = request.user.is_authenticated
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        next_post = request.POST.get('next')
        return redirect(next_get or next_post or '/')

    data = {
        'form': form,
        'information_in_contact_us': information_in_contact_us,
        'footer': footer,
        'user_manager': user_manager,
        'user_auth': user_auth
    }

    return render(request, 'login.html', context=data)


def logout_view(request):
    """
    Logout view.
    
    :param request: GET request.
    :return: Redirect to the main page.
    """
    logout(request)
    return redirect('/')
