from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser
from .forms import UserRegistrationForm,LoginForm
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
def start(request): 
    return render(request, "start.html")

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid(): 
            un = form.cleaned_data['username']
            email = form.cleaned_data['email'] 
            password = form.cleaned_data['password']  
            gender = form.cleaned_data['gender']
            '''try:
                existing_user = CustomUser.objects.get(username=un)
                return JsonResponse({'message': "Username already taken"}, status=409)
            except CustomUser.DoesNotExist:
                CustomUser.objects.create_user(username=un, email=email, password=password)
                return redirect('start')'''
            u_n = CustomUser.objects.filter(username=un)
            #print(CustomUser.objects.get(username=un))
            if u_n.exists():
                return JsonResponse({'message':"username already taken"},status=409)
            else:
                CustomUser.objects.create_user(username=un, email=email, password=password,gender=gender)
                return redirect('start')
             
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
        
            user = authenticate(request,username= username,password=password )
            if user is not None:
                login(request,user)
                return redirect("index")
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
        
    else:
        form = LoginForm()
    return render(request, "login.html", {'form': form})

def logout_view(request):
    logout(request)
    return redirect('start')
    
