# views.py
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignupForm, SigninForm
from django.contrib.auth import authenticate, login

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Process form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            
            # Create user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.phone_number = phone_number
            user.save()
            return redirect('signin')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            # Authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
            else:
                # Handle invalid login
                return render(request, 'signin.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = SigninForm()
    return render(request, 'signin.html', {'form': form})
