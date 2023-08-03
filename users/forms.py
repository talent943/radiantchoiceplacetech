
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django import forms
from .models import Course, SessionYearModel
from .models import Course, Contact

CONTACT_CHOICES = (
    ("email", "E-Mail"),
    ("phone", "Phone"),
)

COURSE_CHOICES = (
    ("ICDL-WORKFORCE", "ICDL WORK FORCE"),
    ("ICDL-PROFESSIONAL", "ICDL PROFESSIONAL"),
    ("ICDL-DIGITAL-CITIZEN", "ICDL DIGITAL CITIZENS"),
    ("ICDL-STUDENT","ICDL STUDENT"),
)


User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    class Meta:  
        model = User  
        fields = ('username', 'email', 'password1', 'password2')


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'image', 'description']

 
 
class DateInput(forms.DateInput):
    input_type = "date"
 
 
class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email",
                             max_length=50,
                             widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password",
                               max_length=50,
                               widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name",
                                 max_length=50,
                                 widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name",
                                max_length=50,
                                widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username",
                               max_length=50,
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address",
                              max_length=50,
                              widget=forms.TextInput(attrs={"class":"form-control"}))
 
    #For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        print("here")
        course_list = []
     
    #For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
             
    except:
        session_year_list = []
     
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
     
    course_id = forms.ChoiceField(label="Course",
                                  choices=course_list,
                                  widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender",
                               choices=gender_list,
                               widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year",
                                        choices=session_year_list,
                                        widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic",
                                  required=False,
                                  widget=forms.FileInput(attrs={"class":"form-control"}))
 
 
 
class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email",
                             max_length=50,
                             widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name",
                                 max_length=50,
                                 widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name",
                                max_length=50,
                                widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username",
                               max_length=50,
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address",
                              max_length=50,
                              widget=forms.TextInput(attrs={"class":"form-control"}))
 
    # For Displaying Courses
    try:
        courses = Course.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []
 
    # For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
             
    except:
        session_year_list = []
 
     
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
     
    course_id = forms.ChoiceField(label="Course",
                                  choices=course_list,
                                  widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender",
                               choices=gender_list,
                               widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year",
                                        choices=session_year_list,
                                        widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic",
                                  required=False,
                                  widget=forms.FileInput(attrs={"class":"form-control"}))

# Contact form

CONTACT_CHOICES = (
    ("email", "E-Mail"),
    ("phone", "Phone"),
)

COURSE_CHOICES = (
    ("ICDL-WORKFORCE", "ICDL WORK FORCE"),
    ("ICDL-PROFESSIONAL", "ICDL PROFESSIONAL"),
    ("ICDL-DIGITAL-CITIZEN", "ICDL DIGITAL CITIZENS"),
    ("ICDL-STUDENT","ICDL STUDENT"),
)

class CoursesCreateForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = [
            "title",
            "duration",
            "cost",
            "tutor",
        ]

    title = forms.CharField(max_length = 20)
    duration = forms.CharField(max_length = 20)
    cost = forms.CharField(max_length = 20)
    tutor = forms.CharField(max_length = 20)


class CoursesUpdateForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = [
            "title",
            "duration",
            "cost",
            "tutor",
        ]

    title = forms.CharField(max_length = 20)
    duration = forms.CharField(max_length = 20)
    cost = forms.CharField(max_length = 20)
    tutor = forms.CharField(max_length = 20)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'mode_of_contact': forms.Select(choices=CONTACT_CHOICES,attrs={'class': 'form-control'}),
        }
        widgets = {
            'course_categories': forms.Select(choices=COURSE_CHOICES,attrs={'class': 'form-control'}),
        }



    

