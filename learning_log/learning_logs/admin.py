from django.contrib import admin
# import models.Topic as Topic
# from learning_logs.models import Topic,Entry
from .models import Topic,Entry

admin.site.register(Topic)
admin.site.register(Entry)
