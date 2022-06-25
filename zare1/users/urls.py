from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from users import views
app_name='users'


router=DefaultRouter()
router.register('api',UserViewSet)

urlpatterns=[
    #path('index/',views.index,name='index'),
    #path('alluser/',views.getusers,name='alluser'),
    #path('signup/',views.signup,name='signup'),
    #path('signinorup/',views.signinorup,name='signinorup'),
    #path('varifyser/',views.codeserializer1,name='varifyser'),
    #path('varifylogin/',views.codeserializer1,name='varifylogin'),
    path('',include(router.urls)),


]