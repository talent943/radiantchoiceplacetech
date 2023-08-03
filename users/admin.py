from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, CustomUser, AdminHOD, Staff, Course, Subject, Student, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaffs, NotificationStudent, NotificationStaffs

admin.site.register(Profile)
admin.site.register(CustomUser)
admin.site.register(AdminHOD)
admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)