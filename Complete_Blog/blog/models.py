from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile', blank=True, default='media/profile/default.jpg')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    bio = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.profile.username


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    code = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='media', blank=True)
    link = models.CharField(max_length=500, blank=True)
    file = models.FileField(upload_to='files', blank=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    profile_name = models.CharField(max_length=50, blank=True)
    profile_image = models.ImageField(upload_to='profile')

    def __str__(self):
        return self.profile_name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=150, help_text='Enter Your Name')
    comment = models.TextField(help_text='Write your comment here')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


class Suggestion(models.Model):
    suggestion_title = models.CharField(max_length=250)
    user = models.CharField(max_length=100)
    e_mail = models.EmailField()
    dated = models.DateTimeField(auto_now=True)
    suggestion = models.TextField(default='Write your suggestions here')

    def __str__(self):
        return self.suggestion_title


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=150, help_text='Enter Your Name')
    comment = models.TextField(help_text='Write your comment here')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


class ReplyModel(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=150, help_text='Enter Your Name')
    reply = models.TextField(help_text='Write your comment here')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reply
