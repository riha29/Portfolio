class Author:
  def __init__(self, *args):
    self.name= 'Default'
    self.books1= ''
    self.books2= ''
    self.books3= ''
    if len(args)==1:
      self.name= args[0]
    elif len(args)==3:
      self.name= args[0]
      self.books1= args[1]
      self.books2= args[2]
  def addBooks(self, *books):
    if len(books)==2:
      self.books1= books[0]
      self.books2= books[1]
    elif len(books)==3:
      self.books1= books[0]
      self.books2= books[1]
      self.books3= books[2]
  def printDetails(self):
    print(f"Author Name: {self.name}\n--------\nList of Books:\n{self.books1}\n{self.books2}\n{self.books3} ")
  def changeName(self, newName):
    self.name= newName

auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print('===================')
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print('===================')
auth2.printDetails()
print("===================")
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()