from django.core.urlresolvers import reverse
from django.db import models
from .choices import SKILL_SET, ACC_SET, GENDER, RATING
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.utils import timezone

# models
class Address(models.Model):
    user = models.OneToOneField(User, related_name = 'owner', on_delete=models.CASCADE, null = True, blank = True )
    organisation = models.OneToOneField(User, related_name = 'organisation', on_delete=models.CASCADE, null = True, blank = True )
    address = models.CharField(max_length = 100, blank = True)
    lga = models.CharField(max_length = 40, blank = True)
    state = models.CharField(max_length = 40, blank = True)
    country = models.CharField(max_length = 40,  blank = True)
    
    def get_full_address(self):
        return self.address + ', ' + self.lga + ', ' + self.state + ', ' + self.country

    def __str__(self):
        return self.address

class BankDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length = 50)
    acc_name = models.CharField(max_length = 50)
    acc_num = models.IntegerField()

    def __str__(self):
        return self.bank_name

class Company(models.Model):
    name = models.CharField(max_length = 120)
    tel = models.CharField(max_length = 15, null = True, blank = True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AffiliateList(models.Model):
    def get_affilates(self):
        self.user_account_set.all()

class Rating(models.Model):
        quality_rating = models.FloatField(choices = RATING, default = 0)
        price_rating = models.FloatField(choices = RATING, default = 0)
        courtesy_rating = models.FloatField(choices = RATING, default = 0)
        overall_rating = models.FloatField(choices = RATING, default = 0)
        number_of_ratings = models.IntegerField(default = 0)

        def __str__(self):
            return '{} - {}'.format(str(self.overall_rating), self.useraccount.user.email)

        def set_ratings(self, quality, price, courtesy):
            self.number_of_ratings += 1
            self.quality_rating = (float(self.quality_rating) + float(quality)) / self.number_of_ratings
            self.price_rating = (float(self.price_rating) + float(price)) / self.number_of_ratings
            self.courtesy_rating = (float(self.courtesy_rating) + float(courtesy)) / self.number_of_ratings
            self.overall_rating = (float(self.quality_rating) + float(self.price_rating) + float(self.courtesy_rating))/ 3
            self.save()

def upload_path(instance, filename):
    return '{}/{}'.format(instance.user.id, filename)

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activation_code = models.CharField(max_length = 120, null = True, blank = True)
    is_active = models.BooleanField(default = False)
    tel = models.CharField(max_length = 15, null = True, blank = True)
    slug = models.SlugField(unique = True, null = True)
    acc_type = models.CharField(max_length = 15, choices  = ACC_SET, default = 'regular')
    gender = models.CharField(max_length = 10, choices = GENDER, null = True, blank =True)
    date_of_birth = models.DateField(null = True, blank =True)
    profile_picture = models.ImageField(upload_to = upload_path, null = True, blank = True)
    organisation = models.ForeignKey(Company, null = True, blank =True)
    affiliates = models.OneToOneField(AffiliateList, on_delete=models.CASCADE, null = True, blank =True)
    rating = models.OneToOneField(Rating, on_delete = models.CASCADE, null = True)
    occupation = models.CharField(max_length = 40, choices = SKILL_SET, null = True, blank = True)
    skill = models.CharField(max_length = 120, null = True, blank = True)

    def get_by_occupation(self, occ= None):
        return self.get_queryset(occupation = occ)
    
    def get_absolute_url(self):
        return reverse("user:details", kwargs={"slug": self.slug})

    def create_slug(self, new_slug=None):
        slug = slugify(self.user.get_full_name())
        if new_slug is not None:
            slug = new_slug
        if UserAccount.objects.filter(slug=slug).exists():
            new_slug = "%s-%s" %(slug, timezone.now().date())
            return self.create_slug(new_slug=new_slug)
        return slug

    def __str__(self):
        return self.user.email

