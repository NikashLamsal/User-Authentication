from django.contrib.auth.base_user import BaseUserManager




class Custommanager(BaseUserManager):


    def create_user(self,phone_number,password=None,**extra_fields):
        if phone_number is None:
            raise ValueError("Phone Number is Required")
        # email = self.normalize_email(email)
        user = self.model(phone_number = phone_number,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,phone_number,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("superuser must is_staff should be true")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("superuser must is_superuser should be true")
        
        if extra_fields.get('is_active') is not True:
            raise ValueError("superuser must is_active should be true")
        

        return self.create_user(phone_number,password,**extra_fields)
