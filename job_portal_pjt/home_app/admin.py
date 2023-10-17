from django.contrib import admin
from . models import Company,CustomUser,Employee,Job,JobSkills,EmpSkills,EmpCommunication,EmpExperience,Gender,Marital,LevelEducation,Education,JobType,ApplyJob

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Job)

admin.site.register(JobSkills)
admin.site.register(EmpSkills)
admin.site.register(EmpCommunication)
admin.site.register(EmpExperience)
admin.site.register(Gender)
admin.site.register(Marital)
admin.site.register(LevelEducation)
admin.site.register(Education)
admin.site.register(JobType)
admin.site.register(ApplyJob)
