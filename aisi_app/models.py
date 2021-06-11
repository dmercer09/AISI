from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def validate(self,formData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}

        

        if len(formData["first_name"]) < 5:
            errors["first_name"] = "First Name should be at least 5 characters"
        if len(formData["last_name"]) < 5:
            errors["last_name"] = "Last Name should be at least 5 characters"
        if len(formData["username"]) < 5:
            errors["username"] = "Username should be at least 5 characters"
        if len(formData["email"]) < 5:
            errors["email"] = "Email should be at least 5 characters"
        if len(formData["password"]) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if formData["confirm_password"] != formData["password"]:
            errors["confirm_password"] = "Confirm password should match Password"
        if not EMAIL_REGEX.match(formData['email']):             
            errors['email'] = ("Invalid email address!")
        email_check = self.filter(email=formData['email'])
        if email_check:
            errors['email_in_use'] = "Email already in use"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()

    

class AISI_Post(models.Model):
    message = models.CharField(max_length=999)
    poster = models.ForeignKey(User, related_name='user_posts', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    aisi_post = models.ForeignKey(AISI_Post, related_name="post_comments", on_delete=models.CASCADE)