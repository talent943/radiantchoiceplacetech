from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .decorators import user_not_authenticated
from .forms import UserRegistrationForm, UserLoginForm, SignupForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserUpdateForm
from django.urls import reverse_lazy, reverse
# email authentication libraries
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.http import HttpResponse
from django.views.generic import View, UpdateView
import smtplib
from django.conf import settings
import socket
from .tokens import account_activation_token
from django_email_verification import send_email
from django.http import HttpResponseRedirect

# host = socket.gethostname()
# print("HOST NAME IS:{}".format(host))
"""
s = socket.socket()
host = socket.gethostbyname('smtp.gmail.com')
print("HOST NAME IS:{}".format(host))
# host = '127.0.0.1'
port = 587

s.connect(('smtp.gmail.com', 587))
print(s.recv(1024))
s.close
"""



User = get_user_model()

server = smtplib.SMTP()


@user_not_authenticated
def register_user(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            user_email = form.cleaned_data['email']
            user_username = form.cleaned_data['username']
            user_password = form.cleaned_data['password1']

            # Create new user
            user = User.objects.create_user(username=user_username, email=user_email, password=user_password)

            # Make user unactive until they click link to token in email
            user.is_active = False 
            send_email(user)

            return HttpResponseRedirect(reverse('users/login'))

    return render(request, 'users/register.html', {'form':form})
 


# Sign Up View
@user_not_authenticated
def signup(request):  
    if request.method == 'POST':  
        form = SignupForm(request.POST)  
        if form.is_valid():  
            # the form has to be saved in the memory and not in DB
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            #This is  to obtain the current cite domain   
            current_site_info = get_current_site(request)  
            mail_subject = 'The Activation link has been sent to your email address'  
            message = render_to_string('users/acc_active_email.html', {  
                'user': user,  
                'domain': current_site_info.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please proceed confirm your email address to complete the registration')  
    else:  
        form = SignupForm()  
    return render(request, 'users/signup.html', {'form': form})


@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main/home.html")

@user_not_authenticated
def custom_login(request):
    if request.user.is_authenticated:
        return redirect('main/home.html')

    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('main/home.html')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = UserLoginForm() 
    
    return render(
        request=request,
        template_name="users/login.html", 
        context={'form': form}
        )


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    current_site = get_current_site(request)
    message = render_to_string('template_activate_account.html', {
        'user': user.username,
        # 'domain': get_current_site(request).domain,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('users/login')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('main/home')