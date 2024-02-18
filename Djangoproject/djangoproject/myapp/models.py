from django.db import models
import uuid

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publication_date = models.DateField()
    cover_image = models.ImageField(null=True, upload_to='book_covers/')
    is_featured = models.BooleanField(default=False)
    book_id = models.CharField(max_length=20, unique=True, default=uuid.uuid4().hex[:8])
    #author = models.TextField()
    def __str__(self):
        return self.title


