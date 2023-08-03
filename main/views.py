from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Courses
from .decorators import user_is_superuser
from .forms import CoursesCreateForm, CoursesUpdateForm, ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings

# Create your views here.
""" def homepage(request):
    courses = Courses.objects.all()

    return render(request=request,
                  template_name='main/home.html',
                  context={"objects": courses}
                  )


def students(request, series: str):
    students = Student.objects.all()

    return render(request=request,
                  template_name='main/students.html',
                  context={"objects": students}
                  )

 def student(request, series: str, article: str):
    student = Student.objects.filter(course=student.first()

    return render(request=request,
                  template_name='main/student.html',
                  context={"object": student}
                  ) """


def new_course(request):
    if request.method == 'POST':
        form = CoursesCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = CoursesCreateForm()

    return render(
        request=request,
        template_name='main/new_record.html',
        context={
            "object": "Courses",
            "form": form
            }
        )

def new_student(request):
    if request.method == "POST":
        form = StudentCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"{form.cleaned_data['series'].slug}/{form.cleaned_data.get('article_slug')}")

    else:
         form = StudentCreateForm()

    return render(
        request=request,
        template_name='main/new_record.html',
        context={
            "object": "Student",
            "form": form
            }
        )

def course_update(request, course):
    return redirect('/')

def course_delete(request, course):
    return redirect('/')

def student_update(request, student, course):
    return redirect('/')

def student_delete(request, student, course):
    return redirect('/')



def home(request):
    courses = Courses.objects.all()
    
    context = {
            "objects": courses,
            "type": "courses"
        }
    return render(request, 'main/home.html', context)

def student(request):
    user = request.user
    students = Student.objects.filter(id=user.id).all()

    context = {
            "objects": students,
            "type": "student"
            }
    return render(request, 'main/student.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid(): 
            form.save()
            subject = request.POST.get("subject", "Welcome to Radiant Choice PlaceTech")
            message = request.POST.get("message", "Our team will contact you within 24hrs.")
            from_email = settings.EMAIL_HOST_USER
            email = form.cleaned_data['email']
            recipient_list = email
            send_mail(subject, message, from_email, [recipient_list])
            return render(request, 'main/success.html') 
    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/contact.html', context)

def success(request):
    return render(request, 'main/success.html')


def about(request):
    return render(request, 'main/about.html')


def course(request):
    course_list = Courses.objects.all()
    context = {
        course_list : course_list
    }
    return render(request, 'main/course.html', context)
