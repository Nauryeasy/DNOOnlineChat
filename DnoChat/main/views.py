from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, FindUsers, Messanger
from django.contrib.auth.models import User
from .models import Contacts, Messages


@login_required
def index(request):
    users = User.objects.all()

    contactlist = Contacts.objects.all()
    name = ''
    error = ''
    username = ''
    selfuser = request.user.get_username()

    if request.method == 'POST':
        form = FindUsers(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            for user in users:
                username = user.username
                if name == username:
                    error = 'Контант успешно добавлен!'
                    contact = Contacts(
                        person1=selfuser,
                        person2=name
                    )
                    contact.save()
                    break
                else:
                    error = 'Пользователь не найден!'

    if error == 'Контант успешно добавлен!':
        pass

    form = FindUsers()

    context = {
            "users_list": users,
            'form': form,
            "name": name,
            "error": error,
            "contactlist": contactlist
        }
    return render(request, 'main/index.html', context)


def chatview(request, pk):
    contactlist = Contacts.objects.all()
    selfuser = request.user.get_username()
    message_list = Messages.objects.all()

    if request.method == 'POST':
        form = Messanger(request.POST)
        if form.is_valid():
            message_text = form.cleaned_data.get("message")
            message = Messages(
                id_contact=pk,
                sender=selfuser,
                message=message_text
            )
            message.save()

    for el in contactlist:
        if el.id == pk:
            person1 = el.person1
            person2 = el.person2

    if request.user.username == person1 or request.user.username == person2:
        pass
    else:
        return redirect('leftuser')

    form = Messanger()

    context = {
            "contactlist": contactlist,
            "messagelist": message_list,
            "form": form,
            "pk": str(pk)
        }

    return render(request, 'main/chat.html', context)


def leftuser(request):
    return render(request, 'main/leftuser.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

@login_required
def profile(request):
    contactlist = Contacts.objects.all()

    context = {
            "contactlist": contactlist
        }

    return render(request, 'main/profile.html', context)
