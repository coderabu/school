from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from groups.models import Groups
from .forms import LoginForm, AddUserForm, EditTeacherForm
from .models import User

def main_page(request):
    return render(request,'main/landing.html')

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        context = {
            'form':form
        }
        return render(request,'main/login.html',context)

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
                        return redirect('accounts:teacher_list')
                    elif user.role == 'teacher':
                        return redirect('teacher_page')
                    elif user.role == 'student':
                        return redirect('student_page')
                else:
                    return render(request, 'main/login.html', {'form': form, 'error': 'Invalid credentials.'})
        else:
            form = LoginForm()

        return render(request, 'main/login.html', {'form': form})
def teacher_list(request):
    teachers = User.objects.filter(role='teacher')
    context = {
        'teachers':teachers
    }
    return render(request, 'ceo/teacher/teacher.html',context)

class TeacherDetailView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(User, pk=pk)
        groups = Groups.objects.filter(teacher=teacher)
        context = {
            'teacher': teacher,
            'groups': groups,
        }
        return render(request, 'ceo/teacher/teacher-detail.html', context)


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        context = {'form': form}
        return render(request, 'ceo/teacher/add_user.html', context)

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:teacher_list')
        context = {'form': form}
        return render(request, 'ceo/teacher/add_user.html', context)

class UpdateTeacher(View):
    def get(self, request, pk):
        teacher = get_object_or_404(User, pk=pk)
        form = EditTeacherForm(instance=teacher)
        context = {'form': form, 'teacher': teacher}
        return render(request, 'ceo/teacher/update-teacher.html', context)

    def post(self, request, pk):
        teacher = get_object_or_404(User, pk=pk)
        form = EditTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('accounts:teacher_list')
        context = {'form': form, 'teacher': teacher}
        return render(request, 'admin/teacher/update-teacher.html', context)

class DeleteTeacher(View):
    def post(self, request, pk):
        teacher = get_object_or_404(User, pk=pk)
        teacher.delete()
        return redirect('accounts:teachers')






# ============================ Student Section ============================




def student_list(request):
    students = User.objects.filter(role='student')
    context = {
        'students':students
    }
    return render(request, 'ceo/student/student.html',context)

# class StudentDetail(View):
#     def get(self,request,pk):
#         students = get_object_or_404(User, pk=pk)
#         context = {
#             'students': students,
#         }
#         return render(request, 'ceo/teacher/teacher-detail.html', context)
#
# class UpdateStudent(View):
#     def get(self, request, pk):
#         student = get_object_or_404(User, pk=pk)
#         form = EditTeacherForm(instance=student)
#         context = {'form': form, 'student': student}
#         return render(request, 'ceo/student/update-student.html', context)
#
#     def post(self, request, pk):
#         student = get_object_or_404(User, pk=pk)
#         form = EditTeacherForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts:teacher_list')
#         context = {'form': form, 'student': student}
#         return render(request, 'ceo/student/update-student.html', context)
#
# class DeleteStudent(View):
#     def post(self, request, pk):
#         student = get_object_or_404(User, pk=pk)
#         student.delete()
#         return redirect('accounts:teacher_list')



