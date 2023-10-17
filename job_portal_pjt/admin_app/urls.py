from django.urls import path
from . import views


urlpatterns = [
    path('admin_app/',views.home,name='admin-home' ),
    path('admin_app/cmp_view/<int:id>/',views.view_more,name='cmp-view' ),
    path('admin_app/emp_view/<int:id>/',views.emp_view,name='emp-view' ),

    path('admin_app/cmp_request/<int:id>/',views.cmp_rqst,name='cmp-rqst' ),
    path('admin_app/cmp_delete/<int:id>/',views.cmp_delete,name='cmp-dlt' ),
   
]