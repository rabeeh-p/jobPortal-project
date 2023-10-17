from django.shortcuts import render,redirect
from . models import*
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.



def index(request):
    job_obj=Job.objects.all()
    context={'jobs':job_obj}
    return render(request,'index.html',context)


def login(request):
    if request.method == 'POST':     
      name=request.POST.get("username")
      password=request.POST.get("password")
      user=auth.authenticate(username=name,password=password)
    #   if user.role=='company':
      if user:         
          if user.role==2:
              auth.login(request,user)
              return redirect('cmp-details')
          elif user.role==3:
              auth.login(request,user)
              
              return redirect('emp-details')  
          else:
              auth.login(request,user)
              return redirect('admin-home')
              
                     
      else:
       
        return HttpResponse("<h1>invalid user</h1>")

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


@login_required(login_url='login')
def company_home(request):
    C_obj=Company.objects.filter(custom_user=request.user)
    print(C_obj)
    if not C_obj:
        return redirect('error')

    company_obj=Company.objects.filter(custom_user=request.user).first()
    print(company_obj)
    if  not company_obj.is_request :
        return redirect('cmp-waiting')
    job_obj=Job.objects.filter(user=request.user)
    return render(request,'company_home.html',{'job':job_obj})


@login_required(login_url='login')
def error(request):
    return render(request,'error.html')

def cmp_waiting(request):
    return render(request,'cmp_waiting.html')


# company fields
def register_cmp(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myuser= CustomUser.objects.create_user(username=name,email=email,password=password,role=2)  
        myuser.save()
        return redirect('login')
    return render(request,'registeration.html')


@login_required(login_url='login')
def company_details_view(request):
    company_obj=Company.objects.filter(custom_user=request.user)
    if company_obj:
        return redirect('home')
   

    if request.method=='POST':
        web=request.POST.get('web')
        phone=request.POST.get('phone')
        industry=request.POST.get('ind')
        desscription=request.POST.get('des')
        location=request.POST.get('location')
        image1=request.FILES['image1234']
        founded_date=request.POST.get('date')
        myuser= Company.objects.create(image=image1,website_link=web,phone_number=phone,industry=industry,location=location,founded_date=founded_date,description=desscription,custom_user=request.user)
        myuser.save()
        return redirect('home')
    return render(request,'company_details.html')


@login_required(login_url='login')
def company_create(request):
    job_type=JobType.objects.all()
    if request.method=='POST':
        title=request.POST.get('title')
        jobfield=request.POST.get('field')
        salary=request.POST.get('salary')
        desscription=request.POST.get('des')
        location=request.POST.get('location')
        exp=request.POST.get('exp')
        sks=request.POST.get('sk')
        exp_edu=request.POST.get('edu')
        vacancies=request.POST.get('vacancy')
        type_id=request.POST.get('type')
        type=JobType.objects.get(id=type_id)

        myuser= Job.objects.create(title=title,experience=exp,job_filed=jobfield,vacancies=vacancies,salary=salary,location=location,description=desscription,job_type=type,education_rqmnts=exp_edu,user=request.user)
        job_skills=JobSkills.objects.create(job=myuser,skills=sks)
        job_skills.save()
        return redirect('home')
    return render(request,'company_create.html',{'type':job_type})


@login_required(login_url='login')
def company_viewmore(request,id):
    C_obj=Job.objects.filter(user=request.user)
    if not C_obj:
        return redirect('error')
    
    job_obj=Job.objects.get(id=id)
    skills_obj=JobSkills.objects.filter(job=job_obj)
    # apply_obj=JobApplication.objects.filter(job=id)'apply':apply_obj,
    app=ApplyJob.objects.filter(job=id)
    return render(request,'company_viewmore.html',{'job':job_obj,'skl':skills_obj,'app':app})

@login_required(login_url='login')
def jobpost_delete(request,id):
    job_obj=Job.objects.get(id=id).delete()
    return redirect('home')


@login_required(login_url='login')
def appley_empdetails(request,id): 
    app_obj=ApplyJob.objects.get(id=id)
    # print(app_obj.emb)
    emp1=app_obj.emb
    custom_obj=app_obj.custom_user
    # print(emp1)
    emp_obj=Employee.objects.filter(first_name =emp1)
    print(emp_obj) 
    
    # pending
    skill_obj=EmpSkills.objects.filter(emp=custom_obj)
    ex_obj=EmpExperience.objects.filter(emp=custom_obj)
    cm_obj=EmpCommunication.objects.filter(emp=custom_obj)
    edu_obj=Education.objects.filter(emp=custom_obj)

    return render(request,'appley_emp_details.html',{'emp':emp_obj,'skl':skill_obj,'empex':ex_obj,'communication':cm_obj,'edu':edu_obj})


@login_required(login_url='login')
def cmp_profile(request):
    cmp_obj=Company.objects.filter(custom_user=request.user)
    company_custom=CustomUser.objects.filter(username=request.user)

    return render(request,'cmp_profile.html',{'cmp_pro':cmp_obj,'customs':company_custom})




# embloyee registeration
def register_emp(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
       
        myuser= CustomUser.objects.create_user(username=name,email=email,password=password,role=3)
        
        # myuser.save()
        return redirect('login')

    return render(request,'registration2.html')

@login_required(login_url='login')
def employee_details_view(request):    
     
     embloyee_obj=Employee.objects.filter(custom_user=request.user)
     if embloyee_obj:
        return redirect('emp-home') 
     
     #pending

     marit_obj1=Marital.objects.all()
     gender_obj1=Gender.objects.all()
     
    
     if request.method=='POST':
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        email=request.POST.get('email')
        image1=request.FILES['image01']
        number=request.POST.get('number')
        experience=request.POST.get('exp')
        department=request.POST.get('department')

        marit_id=request.POST.get('marital')
        marital_obj=Marital.objects.get(id=marit_id)
        gender_id=request.POST.get('gender1')
        gender_obj=Gender.objects.get(id=gender_id)


        date=request.POST.get('dop')     
        my_new_user= Employee.objects.create(gender=gender_obj,marital_status=marital_obj,first_name=f_name,last_name=l_name,email=email,image=image1,phone_number=number,date_of_birth=date,department=department,experience=experience,custom_user=request.user)  
        # my_new_user.save()
        # new_gender=Gender.objects.create(section=gender_obj)
        # new_gender.save()
        # marital_new=Marital.objects.create(category=marital_obj)
        # marital_new.save()
        # empskills_obj=EmpSkills.objects.create(emp=request.user,skills=skills)
        # empskills_obj.save()
        # empcommunication_obj=EmpCommunication.objects.create(emp=request.user,communication=communication)
        # empcommunication_obj.save()
        return redirect('emp-home')
     return render(request,'employee_view.html',{'gnd':gender_obj1,'marital':marit_obj1})


@login_required(login_url='login')
def embloyee_home(request):
    job_obj=Job.objects.all()

    job_title=request.GET.get('job')
    job_location=request.GET.get('location')
    job_exp=request.GET.get('exp')
    if job_title:
        job_obj=job_obj.filter(title__icontains=job_title)
    if job_location:
        job_obj=job_obj.filter(location__icontains=job_location)
    if job_exp:
        job_obj=job_obj.filter(experience__icontains=job_exp)

    
    return render(request,'employee_home.html',{'job':job_obj})





@login_required(login_url='login')
def job_apply(request,id):
    man_obj=ApplyJob.objects.filter(custom_user=request.user ,job_id=id)
    if man_obj:
        return redirect('sample') 
    job_obj=Job.objects.get(id=id)
    if request.method=='POST':
        image1=request.FILES['image'] 
        emp_obj=Employee.objects.filter(custom_user=request.user).first()
        print(emp_obj.email)
        user=ApplyJob.objects.create(custom_user=request.user,emb=emp_obj,job=job_obj,resume_img=image1)
        
        return redirect('emp-home')
    return render(request,'job_appley.html')

@login_required(login_url='login')
def job_inbox(request):
    appley_obj=ApplyJob.objects.filter(custom_user=request.user)

    return render (request,'job_inbox2.html',{'obj':appley_obj})


def sample(request):
    
    return render(request,'sample.html')


@login_required(login_url='login')
def application_comform(request,id):
    # job_obj=JobApplication.objects.filter(id=id).first()
    job_obj=ApplyJob.objects.get(id=id)
    job_id=job_obj.job.id
    if job_obj.is_conform == False:
        job_obj.is_conform= True
        job_obj.save()
    else:
        job_obj.is_conform= False
        job_obj.save()
    return redirect('cmp-viewmore',job_id)
