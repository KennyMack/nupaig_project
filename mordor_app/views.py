from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from mordor_app.forms import User_Form, User_ProfileForm, Login_Form


def register(request):
    context = RequestContext(request)

    if request.POST:
        user_form = User_Form(data=request.POST)
        profile_form = User_ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        user_form = User_Form()
        profile_form = User_ProfileForm()

    return render(request,
        'Forms/register.html', {'user_form': user_form,
                                'profile_form': profile_form}
    )


@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def user_login(request):

    if request.POST:
        form_login = Login_Form(data=request.POST)

        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form_login = Login_Form()

    return render(request,
        'Forms/login.html', {'form_login': form_login})

def handler404(request):
    response = render(request, 'Handlers/404.html')
    response.status_code = 404
    return response


def handler500(request):
    response = render('Handlers/500.html')
    response.status_code = 500
    return response