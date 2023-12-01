from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Course
from .forms import CourseForm, UpdateCourseForm

def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def user_home(request):
    return render(request, 'user_home.html')

@login_required
def admin_home(request):
    courses = Course.objects.all()
    return render(request, 'admin_home.html',{'courses': courses})

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('update_view_list')
    else:
        form = CourseForm()

    return render(request, 'add_course.html', {'form': form})



@login_required
def update_view_list(request):
    courses = Course.objects.all()
    return render(request, 'update_view_list.html', {'courses': courses})





@login_required
def update_course(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)

    if request.method == 'POST':
        form = UpdateCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('update_view_list')
    else:
        form = UpdateCourseForm(instance=course)

    return render(request, 'update_course.html', {'form': form})

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    course.delete()

    return redirect('update_view_list')
