from django.urls import path
from . import views

urlpatterns = [
  path("register/", views.CreateUserView.as_view()),
  path("assignrole/", views.AssignRoleToUser.as_view()),
  path("create-role/", views.CreateRole.as_view()),
  path("hr/", views.HRPage.as_view()),
]