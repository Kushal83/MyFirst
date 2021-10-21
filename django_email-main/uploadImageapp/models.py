from django.db import models

class uploadModel(models.Model):
    Pan_card = models.ImageField(upload_to="profiles", height_field=300, width_field=342)
    Aadhaar_card = models.ImageField(upload_to ="profiles", height_field = 300 ,width_field = 342)
    Company_document = models.ImageField(upload_to = "profiles", height_field = 300 , width_field = 342)
    Photo = models.ImageField(upload_to = "profiles", height_field = 300 ,width_field = 342)

