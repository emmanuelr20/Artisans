from django.db import models
from django.contrib.auth.models import User
from user.models import UserAccount

# Create your models here.
class Transaction(models.Model):
	customer			=	models.ForiegnField(UserAccount, related_name='hires', on_delete = models.CASCADE)
	artisan				=	models.ForiegnField(UserAccount, related_name='jobs', on_delete = models.CASCADE)
	price 				=	models.FloatField(null = True)
	start_date			=	models.DateTimeField(null = True)
	end_date			=	models.DateTimeField(null = True)
	status_from_customer=	models.BooleanField(default = False)
	status_from_artisan	=	models.BooleanField(default = False)
	transaction_status	= 	models.BooleanField(default = False)

	def __str__(self):
		return '%s-%s' %(self.customer.user.first_name, self.artisan.user.first_name)

	class Meta:
		verbose_name_plural = "Transactions"
		verbose_name = "Transaction"

			