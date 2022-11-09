class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print("*******************************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in  the train are {self.seats}")
        print("*******************************")

    def fareinfo(self):
        print(f"The price of the ticekt is Rs {self.fare} ")
    
    def bookticket(self):
        if(self.seats>0):
            print(f"your ticket has been booked and your seat number is {self.seats} ")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full kindly try in peshawar Express")
    def cancelTicekt(self, seatNo):
        pass

    
rawalpindiExpress = Train("Rawalpindi Express: 14015", 300, 5)
rawalpindiExpress.getstatus()
rawalpindiExpress.bookticket()
rawalpindiExpress.bookticket()
rawalpindiExpress.bookticket()
rawalpindiExpress.bookticket()
rawalpindiExpress.bookticket()
rawalpindiExpress.getstatus()