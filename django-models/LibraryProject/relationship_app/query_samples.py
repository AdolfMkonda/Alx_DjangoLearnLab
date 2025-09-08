from relationship_app.models import Author, Book, Librarian, Library

Book.objects.get(Book.all())


Library.objects.get(name=library_name)
Library.books.all()

Librarian.objects.get(id = 1)

Author.objects.get(name=author_name)
object.filter(author=author)


object.filter(author=author)