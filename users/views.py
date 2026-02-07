from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from resources.models import Resource


#  REGISTER VIEW

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        #  Basic validation
        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required!")
            return redirect('register')

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        #  Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        Profile.objects.create(user=user)
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')
    return render(request, 'users/register.html')

#  LOGIN VIEW
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'users/login.html')


#  LOGOUT VIEW
@login_required
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        # GET request is not allowed (as per Django 405 error you saw)
        messages.warning(request, "Invalid logout method.")
        return redirect('profile')


#  PROFILE VIEW

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={'college': '', 'department': '', 'year': 1}
    )

    uploaded_resources = Resource.objects.filter(
        uploaded_by=request.user
    ).order_by('-uploaded_at')

    if request.method == 'POST':
        profile.college = request.POST.get('college', '')
        profile.department = request.POST.get('department', '')
        profile.year = request.POST.get('year', profile.year)

        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']

        profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')

    # CORRECT CONTEXT
    context = {
        'user': request.user,
        'profile': profile,
        'uploaded_resources': uploaded_resources
    }

    return render(request, 'users/profile.html', context)
