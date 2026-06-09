from django.urls import path
from . import views

# This namespace helps Django distinguish these URLs if you add more apps later
app_name = 'sports_tracker'

urlpatterns = [
    # Path for the Home page (e.g., http://127.0.0.1:8000/)
    path('', views.home, name='home'),
    
    # Path for the List page (e.g., http://127.0.0.1:8000/items/)
    path('items/', views.item_list, name='item_list'),
    
    # Path for the Detail page (e.g., http://127.0.0.1:8000/items/1/)
    # The <int:item_id> captures the number from the URL and passes it to your view
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),
]