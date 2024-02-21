from django.urls import path
from . import views

app_name = 'quote'

urlpatterns = [
    path('', views.main, name='main'),
    path('quote/', views.quote, name='quote'),
    path('tag/', views.tag, name='tag'),
    path('detail/<int:quote_id>', views.detail, name='detail'),
    path('done/<int:quote_id>', views.set_done, name='set_done'),
    path('delete/<int:quote_id>', views.delete_quote, name='delete'),
]
