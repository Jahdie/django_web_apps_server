from django.contrib import admin
from .models import *
#TODO переопределить добавление объекта в модель TableHead, чтоб при добавление считались column_num

MODELS_LIST = (Tab, TableHeader, TableSider, Query, TableBodyFieldType, TableBody)

admin.site.register(MODELS_LIST)