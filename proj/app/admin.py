from django.contrib import admin
from . import models
# Register your models here.
model_list = [models.Category, 
              models.User, 
              models.UserProfile, 
              models.Order,
              models.Customer,
              models.Member,
              models.Product]

for model in model_list:
    admin.site.register(model)
