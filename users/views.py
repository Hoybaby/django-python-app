from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form' : form})

# decorators add functionality
@login_required
def profile(request):
    if request.method == 'POST':
    # the argurment in will pass the information to the form for the current user and profile
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # this will save the info to update the form
        if u_form.is_valid() and p_form.is_valid():
            u_form.save() 
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
            # i want to use the redirect here isntead of rendering at the bottom because of 'post get redirect pattern'. This way prevents a rpompt asking are you ok resubbmiting
            # because it will reload
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


