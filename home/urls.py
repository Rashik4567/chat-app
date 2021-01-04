from django.urls import path
from .views import defineUser, login, register, userCreate, userList, massageList, massageSend, senders

urlpatterns = [
    path('u/<str:pk>', senders),
    path('m', massageSend),
    path('p/<str:spk>/<str:rpk>', massageList),
    path('uc', userCreate),
    path('uf/<str:pk>', defineUser),
    path('login', login),
    path('register', register)
]
