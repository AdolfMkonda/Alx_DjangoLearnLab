
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
#(1, {'bookshelf.Book': 1})[?25h[18;1H[?1004l[?2004l[?1l>[>4;m[?1049l[23;0;0tVim: Caught deadly signal TERM
Vim: Finished.
[18;1H[23;2t[23;1t