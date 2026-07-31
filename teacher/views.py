from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from groups.models import Groups, GroupStudent
from attendance.models import Attendance


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

class MarkAttendance(View):
    def get(self, request):
        # 1-bosqich: faqat guruh va sana tanlash formasi
        groups = Groups.objects.filter(teacher=request.user)
        context = {
            'groups': groups,
            'step': 1,  # birinchi bosqich
        }
        return render(request, 'teacher/mark_attendance.html', context)

    def post(self, request):
        groups = Groups.objects.filter(teacher=request.user)
        group_id = request.POST.get('group')
        date = request.POST.get('date')

        # agar "Saqlash" tugmasi bosilgan bo'lsa
        if request.POST.get('save'):
            group = get_object_or_404(Groups, pk=group_id, teacher=request.user)
            group_students = GroupStudent.objects.filter(group=group)

            for gs in group_students:
                status = request.POST.get(f'status_{gs.student.id}')
                if status:
                    Attendance.objects.update_or_create(
                        student=gs.student,
                        group=group,
                        date=date,
                        defaults={'status': status}
                    )
            return redirect('teacher:mark_attendance')

        # agar "Ko'rish" tugmasi bosilgan bo'lsa — studentlarni chiqar
        group = get_object_or_404(Groups, pk=group_id, teacher=request.user)
        group_students = GroupStudent.objects.filter(group=group)
        context = {
            'groups': groups,
            'group': group,
            'group_students': group_students,
            'date': date,
            'step': 2,  # ikkinchi bosqich
        }
        return render(request, 'teacher/mark_attendance.html', context)