from bookshelf.models import Book

Book.objects.get(id=1)
#<Book: 1984>
 book.delete()
#(1, {'bookshelf.Book': 1})
