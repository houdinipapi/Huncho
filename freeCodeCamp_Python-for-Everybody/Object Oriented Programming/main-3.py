# --- OBJECT ORIENTED PROGRAMING --- #

# Sample of a code that is object-oriented
class PartyAnimal:  # --> This is the template for making PartyAnimal objects
    x = 0  # --> Each PartyAnimal object has a bit of data

    def party(self):
        self.x = self.x + 1
        print("So far:", self.x)


an = PartyAnimal()  # --> Constructing a PartyAnimal object and store in 'an'
an.party()  # --> Telling the 'an' object to run the party() code within it
an.party()
an.party()
an.party()
