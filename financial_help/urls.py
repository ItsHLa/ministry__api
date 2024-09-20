from django.urls import path

from . import views

urlpatterns = [
    ## REFEGUEE
    path('add_request/',views.add_request,name='add_request'),
    path('get_response/', views.get_response, name='get_responses'),
    ## EMPLOYEE
    path('get_requests/',views.get_requests,name='get_requests'),
    path('add_response/<pk>',views.add_response,name='add_response'),
    # path('members/',views.members,name='members'),
]
