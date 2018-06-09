from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Suggestion)
admin.site.register(ReplyModel)
admin.site.register(UserProfile)