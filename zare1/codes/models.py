from django.db import models
import numpy as np
# Create your models here.
from users.models import CustomUser
import random
class Code(models.Model):
    number=models.CharField(max_length=6,blank=True)
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    time1=models.FloatField(default=0)
    time2= models.FloatField(default=0)

    def __str__(self):
        return np.str(self.number)

    def save(self,*args,**kwargs):
        number_list=[x for x in range(10)]
        code_items=[]
        for i in range(6):
            num=random.choice(number_list)
            code_items.append(num)
        code_string="".join(np.str(item) for item in code_items)
        self.number=code_string

        super().save(*args,**kwargs)

