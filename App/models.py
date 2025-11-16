from django.db import models

# Create your models here.
class Teacher (models.Model):
    name = models.CharField(max_length=50, null= True, blank=True)
    email = models.EmailField(unique=True,max_length=50)
    t_id = models.PositiveIntegerField()
    image = models.ImageField(upload_to= 'teacher/image',default='def.png' ,height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return f"{self.name}'s Profils"
    
