from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

from users.forms import UserCreationForm


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def clickboard(request):
    context = {
        "eng1": ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        "eng2": ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        "eng3": ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
        "ru1": ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х'],
        "ru2": ['ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э'],
        "ru3": ['я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю'],
    }
    return render(request, 'clickboard.html', context)


def radiogramm(request):
    context = {
        "eng": ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
                'c', 'v', 'b', 'n', 'm'],

        "ru": ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж',
               'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю'],
    }
    return render(request, 'radiogramm.html', context)


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
