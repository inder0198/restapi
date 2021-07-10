from django.urls import path,include
from .import views
from .import auth
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'heroes',views.displaydata,basename='student')

urlpatterns = [
    path('', views.studentDetails.as_view()),
    path('show/', views.ShowData.as_view()),
    path('update/', views.UpdateData.as_view()),
    path('display/', views.DisplayUsers.as_view()),
    path('task/', views.Task.as_view()),
    path('delete/', views.DeleteData.as_view()),
    # path('displayData/', views.displaydata.as_view()),
    path('gettoken/', auth.CustAuthToken.as_view()),
    path('',include(router.urls)),
    # path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))

]