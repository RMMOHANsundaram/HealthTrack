from django.urls import path
from . import views


urlpatterns = [

    path(
        'my/',
        views.my_records,
        name='my_records'
    ),

    path(
        '<int:record_id>/',
        views.record_detail,
        name='record_detail'
    ),

    path(
        'create/<int:appointment_id>/',
        views.create_record,
        name='create_record'
    ),

    path(
        '<int:record_id>/prescription/',
        views.add_prescription,
        name='add_prescription'
    ),

    path(
        'doctor/all/',
        views.doctor_records,
        name='doctor_records'
    ),
]