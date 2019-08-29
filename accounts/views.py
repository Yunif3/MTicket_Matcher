from django.contrib.auth import login as auth_login
from accounts.forms import SignUpForm
from django.shortcuts import render, redirect
from market.models import Contact

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.save()
            contact = Contact.objects.create(email = user.email, fb = 'www.m.me/' + form.cleaned_data['fb'], user = user)
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})