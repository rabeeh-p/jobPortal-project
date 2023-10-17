from django.shortcuts import render,redirect
from home_app.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def home1(request):
    return render(request,'home1.html')

@login_required(login_url='login')
def emp_jobview(request,id):
    # company_obj= Company.ob
    obj=Job.objects.get(id=id)
    skills_obj=JobSkills.objects.filter(job_id=id)
    return render(request,'job_view.html',{'job':obj,'skills':skills_obj})

@login_required(login_url='login')
def emp_profile(request):
    education_obj=Education.objects.filter(emp=request.user)
    obj_c=Employee.objects.filter(custom_user=request.user) 
    empskills_obj=EmpSkills.objects.filter(emp=request.user) 
    empcommunication_obj=EmpCommunication.objects.filter(emp=request.user) 
    empexp_obj=EmpExperience.objects.filter(emp=request.user)

    custom_obj=CustomUser.objects.filter(username=request.user)

    context={
        'obj':obj_c,
        'skills':empskills_obj,
        'communication':empcommunication_obj,
        'empex':empexp_obj,
        'custom':custom_obj,
        'edu':education_obj
        }
    return render(request,'emp_profile.html',context)


@login_required(login_url='login')
def edit_pro(request,id):
    marital_obj=Marital.objects.all()
    gender_obj=Gender.objects.all()
    emp_obj=Employee.objects.get(id=id)
    image2=emp_obj.image
    if request.method=='POST':
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        email=request.POST.get('email')
        # image11 = request.FILES.get['image10']
        image11 = request.FILES.get('image10')
        number=request.POST.get('number')
        experience=request.POST.get('exp')
        department=request.POST.get('department')
        date=request.POST.get('dop')     
        emp_obj.first_name=f_name   
        emp_obj.last_name=l_name  
        emp_obj.email=email
        

        # date2=emp_obj.date_of_birth

        emp_obj.phone_number=number
        emp_obj.experience=experience
        emp_obj.department=department
        
       
        if image11:
            emp_obj.image=image11
        else:
            emp_obj.image=image2
        # if not image11:
        #     emp_obj.image=image2
       


        
        if date:
             
            emp_obj.date_of_birth=date 

        # else:
        #     emp_obj.date_of_birth=date2


        emp_obj.save()
        return redirect('emp-prof')
    return render(request,'edit_profile.html',{'emp':emp_obj,'gnd':gender_obj,'marital':marital_obj})



@login_required(login_url='login')
def addskills(request):
    adskills_obj=EmpSkills.objects.filter(emp=request.user)

    if request.method == 'POST':
        skill=request.POST.get('skills')
    
        sample=EmpSkills.objects.create(emp=request.user,skills=skill)
      
        return redirect('emp-prof')



    return render(request,'addskills.html',{'skl':adskills_obj})

@login_required(login_url='login')
def addExp(request):
    exp_obj=EmpExperience.objects.filter(emp=request.user)

    if request.method == 'POST':
       
        j_profile=request.POST.get('profile1')
        salary=request.POST.get('salary')
        location=request.POST.get('location')
        name=request.POST.get('c_name')
    
        sample=EmpExperience.objects.create(emp=request.user,name=name,location=location,salary=salary,job_profile=j_profile)
        sample.save()
        return redirect('emp-prof')
    return render(request,'addExp.html',{'exp':exp_obj})


@login_required(login_url='login')
def addCommunication(request):
    obj=EmpCommunication.objects.filter(emp=request.user)
    if request.method == 'POST':
       
        communication=request.POST.get('cm')
       
    
        sample=EmpCommunication.objects.create(emp=request.user,communication=communication)
        sample.save()
        return redirect('emp-prof')
    return render(request,'addCommunication.html',{'com':obj})

@login_required(login_url='login')
def addEducation(request):
    level_obj=LevelEducation.objects.all()
    education_obj=Education.objects.filter(emp=request.user)

    if request.method == 'POST':
        school=request.POST.get('school')
        course=request.POST.get('course')
        std_date=request.POST.get('start_date')
        ended_date=request.POST.get('ended_date')
        details=request.POST.get('additional')
        level_id=request.POST.get('level1')
        print(level_id)
        level_object=LevelEducation.objects.get(id=level_id)

        edu_sample=Education.objects.create(emp=request.user,level=level_object,school=school,course=course,started_date=std_date,ended_date=ended_date,details=details)
        edu_sample.save()
        return redirect('emp-prof')

    return render(request,'addEducation.html',{'edu':education_obj,'lvl':level_obj})


@login_required(login_url='login')
def viewMore(request,id):
    emb_obj=EmpExperience.objects.get(id=id)
    print(emb_obj)
    return render(request ,'ViewExp.html',{'exp':emb_obj})



def skillDelete(request,id):
    skill_obj=EmpSkills.objects.get(id=id).delete()
    return redirect('emp-prof')
