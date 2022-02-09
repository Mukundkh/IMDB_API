from django.contrib import admin
from .models import WatchList, StreamPlatForm
# Register your models here.

#registering models used
admin.site.register(WatchList)
admin.site.register(StreamPlatForm)
