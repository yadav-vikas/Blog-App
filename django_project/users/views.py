from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import  UserRegisterForm
from django.contrib import messages # show flash messgaes like confirmed user!!!

#the types of flash message can be given
# messages.rebug
# messages.info
# messages.success
# messages.warning
# messages.error


# django provides functionality of converting functions into htmls forms
def register(request):
    """If user requests POST method then it instantiate UserCreationForm wih that data is
    and store username variable with 'username' at some sort of dictionary strucutr
    Else it instantiates an empty form

    Args:
        request ([any]): [description]

    Returns:
        [UserCreationForm]: [returns a form data on POST Method]
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()# if user data is valid then save it else show user whats wrong with sign up(maybe that user exists)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!') #flash message if valid form.
            return redirect('blog-home') # after successfull sign up redirect link to home page
    else:
        form = UserRegisterForm()

    
    return render(request,'users/register.html', {'form': form})

