from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from rest_framework import serializers
from .serializers import profileSerializer, userCreateSerializer, userSerializer, massageSerializer
from .models import profile, massage


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def massageSend(request):
    serializer = massageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def massageList(request, spk, rpk):
    massages = []
    sendermassages = massage.objects.filter(sender=spk, reciever=rpk)
    recievermassages = massage.objects.filter(sender=rpk, reciever=spk)

    for i, j in zip(sendermassages, recievermassages):
        massages.append(i)
        massages.append(j)

    serializer = massageSerializer(recievermassages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = userSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
    serializer = userCreateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def senders(request, pk):
    msgList = massage.objects.filter(reciever=pk)
    senderList = []
    for msg in msgList:
        senderListTemp = User.objects.get(username=msg.sender)
        if senderList.count(senderListTemp):
            pass
        else:
            senderList.insert(0, senderListTemp)

    serializer = userSerializer(senderList, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def defineUser(request, pk):
    users = User.objects.filter(id=pk)
    serializers = userSerializer(users, many=True)

    return Response(serializers.data)


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        user.save()

        return redirect('/')
    else:
        return render(request, 'register.html')
