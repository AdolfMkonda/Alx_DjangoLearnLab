from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book")

    class Meta:
        permissions = ['can_add_book', 'can_change_book', 'can_delete_book']
        
    
    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField()
    books = models.ManyToManyField(Book, on_delete=models.CASCADE, related_name="libraly")

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField()
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):

    ROLE_CHOICES = [
        ('Member', 'Member'),
        ('Admin', 'Admin'),
    ]

    user = models.CharField()
    favorite_books = models.ManyToManyField(Book, related_name="fav_by")
    user = models.OneToOneField(user, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')


    def __str__(self):
        return self.user
    
 

