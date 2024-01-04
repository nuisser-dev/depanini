from django.shortcuts import render,redirect
from requests import request
from .models import *
from django.contrib import messages
import csv
from depaninii.tree_model import *
def home(request):
    context={}
    return render(request,'home_page.html',context)
#login_demandeur_service
def login(request):
    context={}
    if request.method=='POST':
        nam = request.POST.get('name')
        pas = request.POST.get('pas')
        if Ds.objects.filter(email=nam).exists() and Ds.objects.filter(password=pas).exists() :
         log=Ds.objects.filter(email=nam, password=pas).first()
        
        
        
         return redirect('dashboard',log.id)
        else:
         messages.info(request,"check your password or you email!!!!")
      
         return render(request,'login_page/login.html',context)

    return render(request,'login_page/login.html',context)

def sgin_up_ds(request):
    context={}
    x=Ds.objects.all().values()
    
    if request.method=='POST':
        
        s=Ds()
        nam = request.POST['name']
        pas1 = request.POST['email']
        pas2 = request.POST['pas']
        pas3 = request.POST['pas1']
        if(pas3!=pas2):
             messages.info(request,"password check it !!!!")
        else:
             s.name=nam
             s.email=pas1
             s.password=pas2
       
             s.save()
             
             return redirect('ooffer',s.id)
    return render(request,'ds_pages/sginup_ds.html',context)


def loginDE(request):
    context={}
    if request.method=='POST':
        nam = request.POST.get('name')
        pas = request.POST.get('pas')
        if De.objects.filter(email=nam).exists() and De.objects.filter(password=pas).exists() :
         log=De.objects.filter(email=nam, password=pas).first()
        
        
         return redirect('dash_de',log.id)
        else:
         messages.info(request,"check your password or you email!!!!")
      
         return render(request,'de_pages/login.html',context)

    return render(request,'de_pages/login.html',context)


def sgin_up_de(request):
    context={}
    x=De.objects.all().values()
    
    if request.method=='POST':
        
        s=De()
        nam = request.POST['name']
        pas1 = request.POST['email']
        pas2 = request.POST['pas']
        pas3 = request.POST['pas1']
        if(pas3!=pas2):
             messages.info(request,"password check it !!!!")
        else:
             s.name=nam
             s.email=pas1
             s.password=pas2
       
             s.save()
             
             return redirect('cv',s.id)
    return render(request,'de_pages/sginup_de.html',context)
def cv(request,id):
    context={}
    
    if request.method=='POST':
        cv=Cv()
        title_cv = request.POST['title_cv']
        experience = request.POST['experience']
        skills = request.POST['skills']
        interest = request.POST['interest']
        education = request.POST['education']
        prjct = request.POST['prjct']
        fr = De.objects.get(id=id)
        cv.title_cv=title_cv
        cv.experience=experience
        cv.skills=skills
        cv.interst=interest
        cv.education=education
        cv.prjct=prjct
        cv.id_de=fr
        cv.save()
       

        data0=[fr.id,title_cv,experience,skills,interest,education,prjct]
        data = []
        data.append(data0)


       
        file_path = 'fake_development_data.csv'

       
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
          
            writer.writerows(data) 

        return  redirect('dash_de',fr.id)

    return render(request,'de_pages/cv.html',context)

def dash_de(request,id):
    context={}
    off= offer.objects.all().values()
    
    return render(request,'de_pages/dash_de.html',{'off':off})


def ds_dashboard(request, id):
    context = {}
    chosen_dicts = []  # Initialize an empty list to hold the dictionaries

    if request.method == 'POST':
        bestone = request.POST['bestone']
        best_values = get_best(bestone)
        if best_values == 0:
            messages.info(request, "There is no match yet, please research.")
        else:
            for i in best_values:
                data = pd.read_csv('fake_development_data.csv')
                chosen_row = data[data['id'] == i]
                chosen_dict = chosen_row.to_dict(orient='records')
                chosen_dicts.append(chosen_dict)  # Append the chosen_dict to the list

    context['bestone'] = chosen_dicts  # Assign the list to the context variable

    return render(request, 'ds_pages/dashborad_ds.html', context)



def ooffer(request,id):
    context={}
    
    
    if request.method=='POST':
        of=offer()
        offe = request.POST['offer']
        desc = request.POST['desc']
        salary = request.POST['salary']
        of.offer=offe
        of.desc=desc
        of.salary=salary
        of.id_ds=Ds.objects.get(id=id)
        of.save()
       
        return redirect('dashboard',id)
    return render(request,'ds_pages/offer.html',context)


