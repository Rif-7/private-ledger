from django.contrib import admin
from .models import User, Ledger, Categorie


# Register your models here.

admin.site.register(User)
admin.site.register(Ledger)
admin.site.register(Categorie)