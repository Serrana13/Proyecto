from django.urls import path
from .views import *

urlpatterns = [

    path('', home),

    path('about/', about),

    path('pages/', PostList.as_view(), name="pages"),

    path('pages/<int:pk>/', PostDetail.as_view(), name="page"),

    path('pages/create/', PostCreate.as_view(), name="create_page"),

    path('pages/edit/<int:pk>/', PostUpdate.as_view(), name="edit_page"),

    path('pages/delete/<int:pk>/', PostDelete.as_view(), name="delete_page"),

]