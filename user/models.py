from django.db import models

import uuid

class Profile(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,unique=True)
    phone = models.CharField(max_length=11)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return str(self.name) + ", " + str(self.email) + ', ' + str(self.phone) 
