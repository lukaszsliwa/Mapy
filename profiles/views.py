# encoding: utf-8
from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect
from django.contrib import auth
from forms import LoginForm, ProfileForm, EditProfileForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from maps.models import Map
from favorites.models import Favorite

"""
.. moduleauthor:: Łukasz Śliwa
"""

@login_required
def index(request):
    """
    Pokazuje stronę główną użytkownika. Na stronie znajdują się informacje
    o ulubionych mapach (list map) oraz ostatnio pokonane dystansy.

    .. include:: ../source/login_required.rst

    """
    favorites = Favorite.objects.favorites_for_model(Map, request.user)
    times = request.user.time_set.all()
    summary = 0.0
    for time in times:
        summary += time.distance
    return direct_to_template(request, 'profiles/index.html', locals())

def show(request, username):
    """
    Pokazuje profil użytkownika i dane dotyczące pokonanych przez niego kilometrów.
    """
    user = User.objects.get(username=username)
    return direct_to_template(request, 'profiles/show.html', locals())

def new(request):
    """
    Tworzy formularz nowego użytkownika (metoda GET) lub tworzy nowe konto (metoda POST).

    :returns: jeśli formularz jest poprawnie uzupełniony to tworzy użytkownika
              i przekierowuje go do strony z logowaniem; jeśli formularz zawiera błędy to
              generuje go jeszcze raz wskazując błędne pola

    """
    if request.method == 'GET':
        return direct_to_template(request, 'profiles/new.html', { 'form': ProfileForm() })
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                User.objects.get(Q(username=username) | Q(email=email))
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username,
                    email,
                    password)
                user.save()
                return redirect('login')
            else:
                form.errors['username'] = [u'Podana nazwa użytkownika lub e-mail już istnieje.']

        return direct_to_template(request, 'profiles/new.html', locals())

@login_required
def edit(request):
    """
    Obsługuje dwa typy żądań:
        * GET -- tworzy formularz do edytowania swoich danych
        * POST -- sprawdza poprawność danych i zapisuje je w bazie

    :returns: jeśli podane dane są poprawne do generuje stronę do edycji danych,
              jeśli dane są niepoprawne to wskazuje błędne pola

    .. include:: ../source/login_required.rst

    """
    if request.method == 'GET':
        form = EditProfileForm(initial={
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email })
    elif request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
            user.save()
    return direct_to_template(request, 'profiles/edit.html', locals())

def login(request):
    """
    Tworzy stronę do logowania (GET) lub loguje użytkownika jeśli jego konto
    istnieje i jest aktywne (POST).
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('my-profile')
    else:
        form = LoginForm()
    return direct_to_template(request, 'profiles/login.html', locals())

@login_required
def logout(request):
    """
    Wylogowuje użytkownika i przekierowuje na stronę logowania.
    
    .. include:: ../source/login_required.rst

    """
    auth.logout(request)
    return redirect('login')
