class Paper:
    def __init__(self, color, quantity):
        self.color = color
        self.quantity = quantity
    
    def write_paper(self, text):
        self._paper_content = text

    def read_paper(self):
        return self._paper_content
    

class Book(Paper):
    def __init__(self, title):
        self.title = title
        super().__init__('White',200)
    def price(self, price):
        self.price = price 
    
page = Paper("White", 1)    
novel = Book("This is my world")
novel.write_paper("Long before angels were singing in the sky, and quite evidently everyone was pretty high!")
print (novel.read_paper())
print (novel.quantity)
print (page.quantity)

