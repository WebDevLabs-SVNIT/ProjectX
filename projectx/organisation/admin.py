from django.contrib import admin
from organisation.models import Branch,Subject,StudentUserProfile,FacultyUserProfile
# Register your models here.
admin.site.register(Branch)
admin.site.register(Subject)
admin.site.register(StudentUserProfile)
admin.site.register(FacultyUserProfile)