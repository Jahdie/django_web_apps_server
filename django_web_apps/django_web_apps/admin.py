from django.contrib import admin
from .models import *


MODELS_LIST = (Server, Db, DbTable, DbField)

admin.site.register(MODELS_LIST)