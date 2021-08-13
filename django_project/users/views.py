from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import  UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required # not access to profile if not logged it again after logout
from django.contrib import messages # show flash messgaes like confirmed user!!!

#the types of flash message can be given
# messages.rebug
# messages.info
# messages.success
# messages.warning
# messages.error


# django provides functionality of converting functions into htmls forms
# def register(request):
#     """If user requests POST method then it instantiate UserCreationForm wih that data is
#     and store username variable with 'username' at some sort of dictionary strucutr
#     Else it instantiates an empty form

#     Args:
#         request ([any]): [description]

#     Returns:
#         [UserCreationForm]: [returns a form data on POST Method]
#     """
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()# if user data is valid then save it else show user whats wrong with sign up(maybe that user exists)
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created! Please log in to continue!') #flash message if valid form.
#             return redirect('login') # after successfull sign up redirect link to home page
#     else:
#         form = UserRegisterForm()
#     return render(request,'users/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    """Creating function to check wether the user is logged in to perform changes
    and view their profile

    Args:
        request ([any]): [description]

    Returns:
        [reder]: [returling the login page]
    """
    if request.method == 'POST': # if the user data is not POST method we will not be saving the data and create new form
        u_form = UserUpdateForm(request.POST, instance=request.user) # prefilled user data in the profile form(instancitaed the existing user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # prefilled user image in the form (instanciated for the form)

        if u_form.is_valid() and p_form.is_valid(): # if form data is valid then we will save it else we will redirect back to profile page to enter details again
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!') #flash message if valid form.
            return redirect('profile') # after successfull sign up redirect link to home page
    else:
        u_form = UserUpdateForm(instance=request.user) # prefilled user data in the profile form(instancitaed the existing user)
        p_form = ProfileUpdateForm(instance=request.user.profile) # prefilled user image in the form (instanciated for the form)
 
    context = {
        'u_form': u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)