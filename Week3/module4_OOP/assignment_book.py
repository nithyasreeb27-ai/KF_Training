class Book:
    def __init__(self,name,author,*genres):
        self.name=name
        self.author=author
        self.genres=genres
    def display(self):
        print("Name of the book:",self.name)
        print("Author name:",self.author)
        print("Genres:",self.genres)
book1=Book("harry potter","rowling","Fantasy")
book2=Book("The hunger games","suzanne","science fiction")
book3=Book("Shelock holmes","Jeff kinney","Mystery","fiction")
book1.display()
book2.display()
book3.display()