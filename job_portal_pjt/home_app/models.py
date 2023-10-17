from django.db import models

# Create your models here.

from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,username=None,password=None,**extra_fields):
        if not username:
            raise ValueError("User must have a Username ")
        if not password:
            raise ValueError('User must have a password')
        user=self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username,password=None,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 1)
        return self.create_user(username, password,**extra_fields)



ROLL_CHOICE=[
    (1,'Admin'),
    (2,'Company'),
    (3,'Employee')
]


class CustomUser(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(blank=True,null=True)
    is_active=models.BooleanField(default=True,verbose_name='active')
    is_staff=models.BooleanField(default=True)
    role=models.IntegerField(choices=ROLL_CHOICE,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()


    def __str__(self):
        return self.username
    
 

class Company(models.Model):
    custom_user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)


    industry=models.CharField(max_length=20)
    website_link=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image=models.ImageField(upload_to='images',blank=True)
    founded_date = models.DateField()
    is_request = models.BooleanField(default=False)
    


    def __str__(self):
        return self.location
    


class Gender(models.Model):
    section=models.CharField(max_length=30)

    def __str__(self):
        return self.section


class Marital(models.Model):
    category=models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Employee(models.Model):
    custom_user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images',blank=True)
    first_name = models.CharField(max_length=50) 
    last_name=models.CharField(max_length=50)  
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    #  job role
    department = models.CharField(max_length=50)
    
    experience = models.CharField(max_length=50)
    gender=models.ForeignKey(Gender,on_delete=models.CASCADE)
    marital_status=models.ForeignKey(Marital,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name


class LevelEducation(models.Model):
    levels=models.CharField(max_length=40)

    def __str__(self):
        return self.levels

class Education(models.Model):
    emp=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    level=models.ForeignKey(LevelEducation,on_delete=models.CASCADE)
    school=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    started_date=models.DateField()
    ended_date=models.DateField()
    details=models.TextField()

    def __str__(self):
        return self.school


class EmpSkills(models.Model):
    emp=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    skills=models.CharField(max_length=60)

    def __str__(self):
        return self.skills
    

class EmpCommunication(models.Model):
    emp=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    communication=models.CharField(max_length=60)

    def __str__(self):
        return self.communication



class EmpExperience(models.Model):
    emp=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    

    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    salary=models.CharField(max_length=20)
    job_profile=models.CharField(max_length=40)

    def __str__(self):
        return self.name



class JobType(models.Model):
    type=models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Job(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)  
    title = models.CharField(max_length=100)
    description = models.TextField()
    job_field=models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    # year
    experience=models.TextField()   
    # education
    education_rqmnts=models.CharField(max_length=20)
    vacancies=models.CharField(max_length=20)
    published_at = models.DateTimeField(auto_now_add=True)

    job_type=models.ForeignKey(JobType,on_delete=models.CASCADE)
    

    

    def __str__(self):
        return self.title
    
class JobSkills(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    skills=models.TextField()

    def __str__(self):
        return self.skills

    



    
class ApplyJob(models.Model):
    custom_user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    emb=models.ForeignKey(Employee,on_delete=models.CASCADE)
    resume_img=models.ImageField(upload_to='image',blank=True)
    is_conform=models.BooleanField(default=False)

    def __str__(self):
        return self.emb.first_name


   
    
 


