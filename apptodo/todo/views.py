from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from .forms import RegistrationForm
from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET', 'POST'])
def TodoView(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# def auth_register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             password1 = form.cleaned_data.get('password1')
#             password2 = form.cleaned_data.get('password2')
#             try:
#                 user = User.objects.get(username=form.cleaned_data['username'])
#                 message = "Username already Exists!"
#                 email = User.objects.get(email=form.cleaned_data['email'])
#                 message = "Email already Exists!"
#             except ObjectDoesNotexist:
#                 u = User.objects.create_user(username=username, email=email, password1=password1, )
