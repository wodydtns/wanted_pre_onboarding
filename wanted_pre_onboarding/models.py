from django.db import models


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=20)
    company_nation = models.CharField(max_length=20)
    company_region = models.CharField(max_length=20)


class Employment(models.Model):
    employment_id = models.AutoField(primary_key=True)
    employment_position = models.CharField(max_length=50)
    employment_reward = models.IntegerField(default=0)
    employment_use_tech = models.CharField(max_length=50)
    employment_content = models.TextField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)


class User(models.Model):
    user_id = models.CharField(max_length=50)
    user_password = models.CharField(max_length=200)
    user_create_date = models.DateTimeField()
    user_update_date = models.DateTimeField()


class Applyment(models.Model):
    applyment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Employment, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
