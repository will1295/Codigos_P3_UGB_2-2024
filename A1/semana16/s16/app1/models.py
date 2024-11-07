from django.db import models

class usrs(models.Model):
    n_user = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.n_user
    
class publ(models.Model):
    n_user = models.ForeignKey(usrs,on_delete=models.CASCADE)
    f_pub = models.DateField()
    descrip = models.CharField(max_length=300)


