from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Groups, Subject, GroupStudent
from .forms import GroupForm, SubjectForm, AddStudentToGroupForm
from accounts.models import User


class SubjectListView(View):
    def get(self, request):
        subjects = Subject.objects.all()
        context = {'subjects': subjects}
        return render(request, 'ceo/subject/subject_list.html', context)


class AddSubjectView(View):
    def get(self, request):
        form = SubjectForm()
        context = {'form': form}
        return render(request, 'ceo/subject/add_subject.html', context)

    def post(self, request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups:subject_list')
        context = {'form': form}
        return render(request, 'ceo/subject/add_subject.html', context)


class GroupListView(View):
    def get(self, request):
        groups = Groups.objects.select_related('teacher', 'subject').all()
        context = {'groups': groups}
        return render(request, 'ceo/groups/groups_list.html', context)


class AddGroupView(View):
    def get(self, request):
        form = GroupForm()
        teachers = User.objects.filter(role='teacher')
        subjects = Subject.objects.all()

        context = {
            'form': form,
            'teachers': teachers,
            'subjects': subjects,
        }
        return render(request, 'ceo/groups/add_groups.html', context)

    def post(self, request):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups:group_list')
        else:
            print(form.errors)

        teachers = User.objects.filter(role='teacher')
        subjects = Subject.objects.all()

        context = {
            'form': form,
            'teachers': teachers,
            'subjects': subjects,
        }
        return render(request, 'ceo/groups/add_groups.html', context)


class GroupDetailView(View):
    def get(self, request, pk):
        group = get_object_or_404(Groups, pk=pk)
        students = GroupStudent.objects.filter(group=group)
        context = {
            'group': group,
            'students': students,
        }
        return render(request, 'ceo/groups/group_detail.html', context)


class DeleteGroupView(View):
    def post(self, request, pk):
        group = get_object_or_404(Groups, pk=pk)
        group.delete()
        return redirect('groups:group_list')

class AddStudentToGroupView(View):
    def get(self, request, pk):
        group = get_object_or_404(Groups, pk=pk)
        form = AddStudentToGroupForm()
        students = User.objects.filter(role='student')
        context = {'group': group, 'form': form,
                   'students': students}
        return render(request, 'ceo/groups/add_student_group.html', context)

    def post(self, request, pk):
        group = get_object_or_404(Groups, pk=pk)
        form = AddStudentToGroupForm(request.POST)
        if form.is_valid():
            students = form.save(commit=False)
            students.group = group
            students.save()
            return redirect('groups:group_detail', pk=group.pk)
        students = User.objects.filter(role='student')
        context = {'group': group, 'form': form,
                   'students':students}
        return render(request, 'ceo/groups/add_student_group.html', context)
