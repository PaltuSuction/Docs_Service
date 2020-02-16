from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from authentication_part.forms import UserRegistrationForm, UserLoginForm
from authentication_part.models import User
from core_part.models import Person, Student

'''class Login(LoginView):
    template_name = 'loginPage.html'
    #template_name = 'test_loginPage.html'
    success_url = '/user/{}'.format()'''

def Login(req):
    if req.method == 'POST':
        form = UserLoginForm(req.POST)
        if form.is_valid():
            email = req.POST['email']
            password = req.POST['password']
            user = auth.authenticate(email=email, password=password)
            req.session['user_id'] = str(user.id)
            if user is not None and user.is_active:
                auth.login(req, user)
                return HttpResponseRedirect('/user/{}'.format(user.ticket_number))
            else:
               #form._errors['Authorization_Error'] = 'Неверный логин или пароль'
                return render(req, 'loginPage.html', context={'form': form})
        else:
            return render(req, 'loginPage.html', context={'form': form})
    else:
        form = UserLoginForm()
        return render(req, 'loginPage.html', context={'form': form})


def Registration(req):
    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = form.save(commit=False)
            new_user.set_password(cd['password1'])
            new_user.save()
            new_user.refresh_from_db()

            return HttpResponseRedirect('../user/{}'.format(new_user.ticket_number))
        else:
            return render(req, 'registerPage.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(req, 'registerPage.html', {'form': form})


def MainPage(req, tik_num):
    session_id = req.session['user_id']
    user = User.objects.get(id=session_id)
    student = Student.objects.get(userPerson=user)
    return render(req, 'mainPage.html', context={'student' : student})