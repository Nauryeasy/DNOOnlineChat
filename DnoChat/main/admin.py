from django.contrib import admin
from .models import Contacts
from .models import Messages

admin.site.register(Contacts)
admin.site.register(Messages)