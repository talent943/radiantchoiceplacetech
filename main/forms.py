from django import forms
from .models import Student, Courses, Contact

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
        model = Courses

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
    

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = [
            "first_name",
            "last_name",
            "email_address",
            "phone_number",
            "course",
            "date_enrolled",
        ]
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    email_address = forms.EmailField(max_length = 200)
    phone_number = forms.CharField(max_length = 20)
    date_enrolled = forms.DateInput()
    course = forms.ModelMultipleChoiceField(
        queryset=Courses.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class CoursesUpdateForm(forms.ModelForm):
    class Meta:
        model = Courses

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


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = [
            "first_name",
            "last_name",
            "email_address",
            "phone_number",
            "course",
            "date_enrolled",
        ]
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    email_address = forms.EmailField(max_length = 200)
    phone_number = forms.CharField(max_length = 20)
    date_enrolled = forms.DateInput()
    course = forms.ModelMultipleChoiceField(
        queryset=Courses.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )



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

