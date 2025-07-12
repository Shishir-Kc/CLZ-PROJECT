from django.contrib import admin
from . import models

# Register your models here.

# tile 
admin.site.register(models.Header)
#slide show

admin.site.register(models.Slider)

admin.site.register(models.News)

admin.site.register(models.Event)

admin.site.register(models.GalleryImage)

admin.site.register(models.Quick_acess_academics)

admin.site.register(models.Quick_acess_admission)

admin.site.register(models.Achievements)

admin.site.register(models.Academics)

admin.site.register(models.Head_faculty)

admin.site.register(models.Academic_resources)

admin.site.register(models.Contact)