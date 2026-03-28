class Person:
	def __init__(self, name):
		print(f"New person waiting for the bus!! {name}!")
		self.name = name
		
class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers   
        self.passengers = []                  

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} is on the bus.")
        else:
            print("The bus is full. You can't add amore people.")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} left the bus.")
        else:
            print(f"{person.name} is not in the bus.")

    def show_passengers(self):
        if len(self.passengers) == 0:
            print("The bus is empty.")
        else:
            print(f" {len(self.passengers)} people are in the bus:")
        for p in self.passengers:
            print(f"- {p.name}")


# create people
person_1 = Person("Bryan")
person_2 = Person("Alex")
person_3 = Person("Carlos")
person_4 = Person("Robinson")
person_5 = Person("Isy")

#create bus
bus = Bus(3)

bus.add_passenger(person_1)  
bus.add_passenger(person_2)  
bus.add_passenger(person_3)  
bus.add_passenger(person_4)
bus.add_passenger(person_5)


bus.remove_passenger(person_1) 
bus.remove_passenger(person_4)  

bus.show_passengers()
