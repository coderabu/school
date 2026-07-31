from django.shortcuts import render, get_object_or_404
from django.views import View
from groups.models import Groups, GroupStudent
from .models import Attendance


# 1-sahifa: barcha guruhlar
class AttendanceGroupList(View):
    def get(self, request):
        groups = Groups.objects.all()
        context = {'groups': groups}
        return render(request, 'ceo/attendance/group_list.html', context)


# 2-sahifa: guruh ichidagi studentlar + davomat foizi
class AttendanceGroupDetail(View):
    def get(self, request, pk):
        group = get_object_or_404(Groups, pk=pk)
        group_students = GroupStudent.objects.filter(group=group)

        students_data = []
        for gs in group_students:
            total = Attendance.objects.filter(student=gs.student, group=group).count()
            present = Attendance.objects.filter(student=gs.student, group=group, status='present').count()
            absent = Attendance.objects.filter(student=gs.student, group=group, status='absent').count()

            if total > 0:
                percent = round((present / total) * 100)
            else:
                percent = 0

            students_data.append({
                'student': gs.student,
                'total': total,
                'present': present,
                'absent': absent,
                'percent': percent,
            })

        context = {
            'group': group,
            'students_data': students_data,
        }
        return render(request, 'ceo/attendance/group_detail.html', context)


# 3-sahifa: bitta studentning davomat tarixi
class AttendanceStudentDetail(View):
    def get(self, request, group_pk, student_pk):
        group = get_object_or_404(Groups, pk=group_pk)

        from django.contrib.auth import get_user_model
        User = get_user_model()
        student = get_object_or_404(User, pk=student_pk)

        # sana bo'yicha filter
        date = request.GET.get('date', '')

        if date:
            attendances = Attendance.objects.filter(
                student=student,
                group=group,
                date=date
            )
        else:
            attendances = Attendance.objects.filter(
                student=student,
                group=group
            ).order_by('-date')

        context = {
            'group': group,
            'student': student,
            'attendances': attendances,
            'date': date,
        }
        return render(request, 'ceo/attendance/student_detail.html', context)