from django.urls import path
from . import views

urlpatterns = [
    
    path('emp_app/home1/',views.home1,name='home1' ),
    path('emp_app/jobView/<int:id>/',views.emp_jobview,name='job-view' ),


    path('emp_app/edit/<int:id>/',views.edit_pro,name='edit-view' ),
    path('emp_app/emp_prof/',views.emp_profile,name='emp-prof' ),
    path('emp_app/addskills/',views.addskills,name='add-skill' ),
    path('emp_app/addexp/',views.addExp,name='add-exp' ),
    path('emp_app/addcommunication/',views.addCommunication,name='add-communication' ),
    path('emp_app/addeducation/',views.addEducation,name='add-education' ),
    path('emp_app/viewmore/<int:id>/',views.viewMore,name='exp-viewmore' ),

    path('emp_app/skill_delete/<int:id>/',views.skillDelete,name='skill-delete' ),
    
]
