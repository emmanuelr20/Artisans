from django.contrib import admin
from .models import UserAccount, Address, Rating, Company, AffiliateList
from django.contrib.auth.models import User

#admin.site.register(User)
admin.site.register(UserAccount)
admin.site.register(Address)
admin.site.register(Rating)
admin.site.register(Company)
admin.site.register(AffiliateList)
# Register your models here.
