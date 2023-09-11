from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


class MyUser(AbstractUser):
    pass
    phone = models.CharField(null=True,blank=True, max_length=9, verbose_name='رقم الجوال')
    email = models.EmailField(null=True,blank=True, max_length=254, verbose_name='البريد الإلكتروني')
    

    def __str__(self):
        return str(self.username)
    class Meta:
        
        verbose_name = 'المستخدمين'
        verbose_name_plural = 'المستخدمين'


class Customer(models.Model):
    user = models.OneToOneField(MyUser, null=True, blank=True, on_delete=models.CASCADE, verbose_name="المستخدم")
    full_name = models.CharField(max_length=100, null=True, verbose_name="اسم كامل")
    identifyNo = models.CharField(max_length=120, null=False, unique=True, verbose_name='الرقو الوطني')
    place_Birth = models.CharField(null=True, max_length=9, verbose_name='محل الميلاد')
    place_identify_cut = models.CharField(max_length=100, null=True, verbose_name="مكان صدور البطاقة")
    stop_at = models.CharField(null=True,blank=True, max_length=255, verbose_name='نم الوقوف في')

    active=models.BooleanField(default=True,null=True ,blank=True,verbose_name='تفعيل الحساب')
    def __str__(self):
        return f"{self.full_name}"

    def save(self, *args, **kwargs):
        if not self.pk:
            user = MyUser()
            user.username = self.identifyNo
            user.first_name = self.full_name
        
           
            user.is_superuser=False
            user.is_staff=True
            user.is_active=self.active
            
            user.set_password(str(self.identifyNo))
            user.save()
            group_name = 'العملاء'
            group, created = Group.objects.get_or_create(name=group_name)
            group.user_set.add(user)
            self.user = user  
        else:  # If the object already exists, update the associated user object as well
            self.user.username = self.identifyNo
            self.user.first_name = self.full_name

          
            self.user.is_superuser=False
            self.user.is_staff=True
            self.user.is_active=self.active
            self.user.set_password(str(self.identifyNo))
            self.user.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.user.delete()  # Delete the associated user object as well
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'العميل'
        verbose_name_plural = 'العملاء'

class CustomerAssessts(models.Model):
    image_assesst = models.ImageField(upload_to='photos/customer_assessts/%y/%m/%d',blank=True)
    type_assesst=models.CharField(max_length=100, null=True, verbose_name="مكان صدور البطاقة")
    customer = models.ForeignKey(Customer, related_name='Customer_Assessts', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.customer.full_name}"

    