from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate

def aPage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Inicio de sesión exitoso
            return JsonResponse({"message": "Inicio de sesión exitoso", "username": user.username, "email": user.email})
        else:
            # Credenciales incorrectas o usuario no registrado
            return JsonResponse({"message": "Usuario no registrado o credenciales incorrectas"})
