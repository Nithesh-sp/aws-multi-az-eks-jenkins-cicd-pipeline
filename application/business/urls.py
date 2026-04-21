from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns
    path('',views.home_page,name='home'),
    path('order-entry/', views.order_entry, name='order_entry'),
    path('success-page/', views.success_page, name='success_page'),
    path('user-page/',views.user_page, name="user_page" ),
    path('price-list/',views.price_list,name="price_list"),
    path('price-update/<int:pk>/',views.price_list_update,name="price_list_update"),
    path('track-order/',views.track_page,name='task_page'),
    path('ordered/',views.ordered_page,name='ordered_page'),
    path('detailed/<int:pk>/',views.detailed_page,name="detailed_page"),
    path('health/',views.health,name="health")
    ]
