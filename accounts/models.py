from django.db import models

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    def __str__(self):
        return '{} {}'.format(self.username, self.password)

class Signup(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=254)
    phone=models.BigIntegerField()
    password=models.CharField(max_length=50)
    login=models.ForeignKey(Login,on_delete=models.CASCADE)

    def __str__(self):
            return '{}{}{}{}'.format(self.email,self.username,self.phone,self.password)
