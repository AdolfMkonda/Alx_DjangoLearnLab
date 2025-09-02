
from bookshelf.models import Book

book = Book.objects.create(title = "1984", author= "George Orwell", publication_year= "1949")

book.save()


Book.objects.get(id=1)
# <Book: 1984>


Book.objects.get(id = 1)
# <Book: 1984>
Book.title = "Nineteen Eighty-Four"
Book.save()


Book.objects.get(id=1)
#<Book: 1984>
 book.delete()
#(1, {'bookshelf.Book': 1})