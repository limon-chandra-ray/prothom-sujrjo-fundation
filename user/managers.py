from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_office_staff(self,user_name,email,password=None):
        office_staff = self.model(
            user_name    = user_name,
            email        = email
        )
        office_staff.set_password(password)
        office_staff.save(using = self._db)
        return office_staff
    

    def create_donar(self,user_name,email,password=None):
        donar = self.model(
            user_name = user_name,
            email=email
        )
        donar.set_password(password)
        donar.save(using = self._db)
        return donar

    def create_superuser(self,user_name,email,password=None):
        admin = self.model(
            user_name    = user_name,
            email        = email
        )
        admin.set_password(password)
        admin.is_admin  = True
        admin.is_staff  = True
        admin.save(using = self._db)
        return admin