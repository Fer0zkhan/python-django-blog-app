from django.urls import path
from .views import BlogList, BlogDetail, BlogCreate, BlogUpdate, BlogDelete, CustomLogin, RegisterUser, UserDetail, \
    UserUpdate
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLogin.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', BlogList.as_view(), name='blog'),

    path('blog/<int:pk>/detail/', BlogDetail.as_view(), name='blog-details'),
    path('blog/<int:pk>/edit/', BlogUpdate.as_view(), name='blog-edit'),
    path('blog/<int:pk>/delete/', BlogDelete.as_view(), name='blog-delete'),

    path('blog/create/', BlogCreate.as_view(), name='blog-create'),

    path('user/<int:pk>/detail/', UserDetail.as_view(), name='user-detail'),
    path('user/<int:pk>/edit/', UserUpdate.as_view(), name='user-edit')
]
