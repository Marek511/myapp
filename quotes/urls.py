from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('scraper/<str:option>/', views.scraper, name='scraper'),
    path('author/<int:author_id>', views.author, name='author'),
    path('quote/<int:quote_id>', views.quote, name='quote'),
]
