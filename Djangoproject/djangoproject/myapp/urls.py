from django.urls import path
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_us, name='contact_us'),
    #path('books/', views.books, name='books'),
    path('about/', views.about_us, name='about_us'),
    path('books/<int:book_id>/', views.books_detail, name='books_detail'),
    path('search/', views.search_view, name='search_results')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# path('search/', views.search_view, name='search_results')
#path('add_to_cart/', add_to_cart, name='add_to_cart'),