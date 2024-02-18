from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Book
# Create your views here.

def home(request):
    # Fetch some featured books (you can customize this query)
    featured_books = Book.objects.all()[:3]
    context = {
        'featured_books': featured_books
    }
    return render(request, 'home.html', context)

def contact_us(request):
    # Process form submission here if needed
    return render(request, 'contact_us.html')
def about_us(request):
    return render(request, 'about_us.html')

def books_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books_detail.html', {'book': book})

def search_view(request):
    query = request.GET.get('q')
    results = books_detail.objects.filter(title__icontains=query)  # Example search logic
    return render(request, 'search_results.html', {'results': results, 'query': query})
#def search_view
      