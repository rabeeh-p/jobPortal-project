from django.shortcuts import render,redirect
from home_app.models import *

# Create your views here.


def home(request):
    company_obj=Company.objects.all()
    emp_obj=Employee.objects.all()
    context={'cmp':company_obj,'emp':emp_obj}
    return render(request,'home.html',context)



def view_more(request,id):
    company_obj=Company.objects.get(id=id)
    print(company_obj)
    return render(request,'cmp_view.html',{'cmp':company_obj})

def emp_view(request,id):
    emp_obj=Employee.objects.get(id=id)

    return render(request,'emp_view.html',{'emp':emp_obj})



# if cmp_obj.is_request == False:
    #     cmp_obj.is_request=True
    #     cmp_obj.save()
    # else:
    #     cmp_obj.is_request=False
    #     cmp_obj.save()
def cmp_rqst(request,id):
    cmp_obj=Company.objects.get(id=id)
    
    cmp_obj.is_request = not cmp_obj.is_request
    cmp_obj.save()
    return redirect('admin-home')



def cmp_delete(request,id):
    Company.objects.get(id=id).delete()
    return redirect('admin-home')