from django.db import models

# Create your models here.
class admintbl(models.Model):
    id = models.AutoField(primary_key=True)
    userename=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.userename} {self.password}'

class routestbl(models.Model):
    id = models.AutoField(primary_key=True)
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    distance=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.source} {self.destination} {self.distance} {self.duration}'

class managebustbl(models.Model):
    id = models.AutoField(primary_key=True)
    busname=models.CharField(max_length=100)
    routeid=models.CharField(max_length=100)
    dtime=models.CharField(max_length=100)
    totalseat=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.busname} {self.routeid} {self.dtime} {self.totalseat}'

class managequotastbl(models.Model):
    id = models.AutoField(primary_key=True)
    qname=models.CharField(max_length=100)
    per=models.CharField(max_length=100)
    cutofftime=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.qname} {self.per} {self.cutofftime}'


class booknowtbl(models.Model):
    id = models.AutoField(primary_key=True)
    busname=models.CharField(max_length=100)
    dtime=models.CharField(max_length=100)
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    jdate=models.CharField(max_length=100)
    quota=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)
    def __str__(self):
        return f' {self.id} {self.name} {self.busname} '