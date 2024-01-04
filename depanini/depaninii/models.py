from django.db import models

class Ds(models.Model):
    name=models.CharField(max_length=30)
    lastnm=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
  
    password=models.CharField(max_length=30)

class De(models.Model):
    name=models.CharField(max_length=30)
    lastnm=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
  
    password=models.CharField(max_length=30)


class Cv(models.Model):
    title_cv=models.CharField(max_length=30)
    experience=models.CharField(max_length=30)
    skills=models.CharField(max_length=30)
    interst=models.CharField(max_length=30)
    education=models.CharField(max_length=30)
    prjct=models.CharField(max_length=30)
    id_de=models.OneToOneField(De, on_delete=models.CASCADE)



class offer(models.Model):
    offer=models.CharField(max_length=100)
    desc=models.CharField(max_length=30)
    salary=models.CharField(max_length=30)
    
    id_ds=models.OneToOneField(Ds, on_delete=models.CASCADE)
  
    