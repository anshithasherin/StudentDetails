from django.urls import path
from students.views import *

urlpatterns = [
    path('dash',dashboardview.as_view(),name='dash'),
    path('reg',RegView.as_view(),name="reg"),
    path('landing',Landingview.as_view(),name='landing'),
    path('add',AddStudentDetailsview.as_view(),name='add'),
    path('edit/<int:id>',EditDetailsView.as_view(),name='edit'),
    path('delete/<int:id>',DeleteDetailsView.as_view(),name='delete'),
]
