from django.urls import path
from . import views


urlpatterns = [
    
   path('',views.index,name='index' ),
   path('sample/',views.sample,name='sample' ),
   
   path('login/',views.login,name='login' ),
   path('logout/',views.logout,name='logout' ),


   # company fields
   path('registration_company/',views.register_cmp,name='registration-cmp' ),
   path('company_details/',views.company_details_view,name='cmp-details' ),
   path('home/',views.company_home,name='home' ),
   path('company_create/',views.company_create,name='cmp-create' ),
   path('company_viewmore/<int:id>/',views.company_viewmore,name='cmp-viewmore' ),
   path('cmp_profile/',views.cmp_profile,name='cmp-profile' ),
   path('job_appley_details/<int:id>/',views.appley_empdetails,name='job-appleydetails' ),
   path('job_post_delete/<int:id>/',views.jobpost_delete,name='job-delete' ),


   path('cmp_waiting/',views.cmp_waiting,name='cmp-waiting' ),
   path('application_conform/<int:id>/',views.application_comform,name='cmp-job-conform' ),
   
   
   
   
   path('error/',views.error,name='error' ),
   
   
   
   # embloyee fields
   path('registration_embloyee/',views.register_emp,name='registration-emp' ),
   path('employee_details/',views.employee_details_view,name='emp-details' ),
   path('employee_home/',views.embloyee_home,name='emp-home' ),
   # path('emp_prof/',views.emp_profile,name='emp-prof' ),




   #job 
   path('job_appley/<int:id>/',views.job_apply,name='job-appley' ),
   path('job_inbox/',views.job_inbox,name='job-inbox' ),
   

]