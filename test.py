class Vacuum: # class whose name is vacuum
    def __init__(self,Type,Watt,Bag):#constructer of vacumm
        self.Type=Type # value of type
        self.Watt=Watt # value of watt
        self.Bag=Bag # value of bag

class Cleaner(Vacuum): # class whose name is cleaner and inheriting from vacuum
    def __init__(self,Type,Watt,Bag,Brand,Cord,Colour):#constructer of cleaner
        super().__init__(Type,Watt,Bag) # there is super because of inheriance class
        self.Brand=Brand # value of brand
        self.Cord=Cord # value of cord
        self.Colour=Colour # value of colour

    def getInfo(self): # print all information
        print("Type is: "+self.Type+" ,Watt is: "+self.Watt+", Bag is: "+self.Bag+", Brand is: "+self.Brand+", Cord is: "+str(self.Cord)+", Colour is: "+self.Colour)

# create 4 class and print all information
c1=Cleaner("Dry","1000W","Yes","Singer",True,"Grey")
c2=Cleaner("Wet","600W","No","Rainbow",False,"Black")
c3=Cleaner("Dry","300W","Yes","Vestel",False,"Navy")
c4=Cleaner("Wet","1000W","No","Beko",True,"Red")

c1.getInfo()
c2.getInfo()
c3.getInfo()
c4.getInfo()