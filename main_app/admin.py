from django.contrib import admin

# Register your models here.
from .models import Keyboard, Keycap, Stablizer

# registers our model 
# creates CRUD UI on our admin app
admin.site.register(Keyboard)
admin.site.register(Keycap)
admin.site.register(Stablizer)