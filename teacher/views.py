from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from groups.models import Groups, GroupStudent


class TeacherProfile(View):
    def get(self, request):
        groups = Groups.objects.filter(teacher=request.user)

        context = {
            'teacher': request.user,
            'groups': groups,
        }
        return render(request, 'teacher/profile.html', context)



class TeacherDashboard(View):
    def get(self, request):
        groups = Groups.objects.filter(teacher=request.user)
        context = {'groups': groups}
        return render(request, 'teacher/teacher.html', context)


class TeacherGroupDetail(View):
    def get(self, request, pk):
        group = get_object_or_404(Groups,  teacher=request.user,pk=pk)
        group_students = GroupStudent.objects.filter(group=group)
        context = {
            'group': group,
            'group_students': group_students,
        }
        return render(request, 'teacher/group_detail.html', context)


class TeacherStudentList(View):
    def get(self, request):
        groups = Groups.objects.filter(teacher=request.user)
        q = request.GET.get('q', '')

        if q:
            results = GroupStudent.objects.filter(
                group__in=groups,
                student__first_name__icontains=q
            ) | GroupStudent.objects.filter(
                group__in=groups,
                student__last_name__icontains=q
            )
        else:
            results = GroupStudent.objects.filter(group__in=groups)

        context = {
            'results': results,
            'q': q,
        }
        return render(request, 'teacher/student_list.html', context)