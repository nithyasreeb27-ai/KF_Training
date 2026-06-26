class Book:
    def __init__(self,name,author,*genres):
        self.name=name
        self.author=author
        self.genres=genres
    def display(self):
        print("Name of the book:",self.name)
        print("Author name:",self.author)
        print("Genre:",self.genres)
s1=Book("harry potter","rowling","Fantasy")
s2=Book("The hunger games","suzanne","science fiction")
s3=Book("Shelock holmes","Jeff kinney","Mystery","fiction")
s1.display()
s2.display()
s3.display()