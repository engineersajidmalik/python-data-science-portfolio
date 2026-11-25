### Dunder methods also known as Magic Methods
## represented by double underscore __init__
## allows developers to define and customize the behavior of the objects

class Book:
   def __init__ (self, title, author, num_pages):
       self.title = title
       self.author = author
       self.num_pages = num_pages

   def __str__(self):
        return f"{self.title} by {self.author} and it has {self.num_pages} pages"


## Creates 3 objects of books
book1 = Book("Atomic Habits", "Me", 345)
book2 = Book("Think and Grow Rich", "Me2", 378)
book3 = Book("Why Nations Fails", "Me3", 434)

print(book1)
print(book2)
print(book3)

print(book1 == book2)


