#configure URLs
from django.urls import path
from .views import TList, TDetail, TCreate, TUpdate, TDelete, UserLoginView, RegPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TList.as_view(), name="task"),
    path('task-create/', TCreate.as_view(), name="task-create"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', RegPage.as_view(), name="register"),
    path('task/<int:pk>/', TDetail.as_view(), name="tasks-detail"),
    path('task-update/<int:pk>/', TUpdate.as_view(), name="tasks-update"),
    path('task-delete/<int:pk>/', TDelete.as_view(), name="tasks-delete")

]