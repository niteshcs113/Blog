from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', Fun.as_view(), name='index'),
    path('<int:pk>', Post_.as_view(), name='view'),
    path('<int:pk>/comment/', comment_, name='comment'),
    path('post/comment_view/<int:pk>', reply, name='reply'),
    path('suggestion/', suggestion, name='suggestions'),
    path('about/', about, name='about'),
    path('<int:pk>/profileview/', ProfileView.as_view(), name='profileview')

]
