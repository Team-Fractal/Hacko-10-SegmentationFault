# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .views import complain_panel, room_req, medicalReq, laundary, mess_feedback, emergency, soul
from django.urls import path, include  # add this

urlpatterns = [
    path('complain_panel', complain_panel),
    path('room_req', room_req),
    path('medical', medicalReq),
    path('laundary', laundary),
    path('mess_feedback', mess_feedback),
    path('emergency', emergency),
    path('soul', soul),


    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")),  # Auth routes - login / register
    path("", include("app.urls")),         # UI Kits Html files

]
