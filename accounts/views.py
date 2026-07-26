from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from groups.models import Groups, GroupStudent
from .forms import LoginForm, AddUserForm, EditTeacherForm
from .models import User


class LoginView(View):
    def get(self,request):
        form = LoginForm()
        context = {
            'form':form
        }
        return render(request,'user/login.html',context)

    def post(self,request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    if user.role == 'ceo':
                        return redirect('admin_page:admin_home')
                    elif user.role == 'teacher':
                        return redirect('teacher_page')
                    elif user.role == 'student':
                        return redirect('student_page')
                else:
                    return render(request, 'user/login.html', {'form': form, 'error': 'Invalid credentials.'})
        else:
            form = LoginForm()

        return render(request, 'user/login.html', {'form': form})
def teacher_list(request):
    teachers = User.objects.all()
    context = {
        'teachers':teachers
    }
    return render(request, 'admin/teacher/techer_page.html',context)

class TeacherDetailView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(User, pk=pk)
        groups = Groups.objects.filter(teacher=teacher)
        context = {
            'teacher': teacher,
            'groups': groups,
        }
        return render(request, 'admin/teacher/teacher-detail.html', context)


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        context = {'form': form}
        return render(request, 'admin/add_user.html', context)

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_page:admin_home')
        context = {'form': form}
        return render(request, 'admin/add_user.html', context)

class UpdateTeacher(View):
    def get(self, request, pk):
        teacher = get_object_or_404(User, pk=pk)
        form = EditTeacherForm(instance=teacher)
        context = {'form': form, 'teacher': teacher}
        return render(request, 'admin/teacher/update-teacher.html', context)

    def post(self, request, pk):
        teacher = get_object_or_404(User, pk=pk)
        form = EditTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('admin_page:admin_home')
        context = {'form': form, 'teacher': teacher}
        return render(request, 'admin/teacher/update-teacher.html', context)







# ============================ Student Section ============================





class StudentView(View):
    def get(self, request):
        return render(request, 'admin/student/student_page.html')

