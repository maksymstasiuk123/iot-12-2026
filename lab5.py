from enum import Enum

class Gender(Enum):
    FEMALE = "Female"
    MALE = "Male"
    NON_BINARY = "Non-binary"

class Guest:
    def __init__(self, guest_id, name, age, city, phone_number, gender):
        self.__id = guest_id
        self.__name = name
        self.__age = age
        self.__city = city
        self.__phone_number = phone_number
        self.__gender = gender

    def __del__(self):
        print(f"Guest {self.__name} deleted.")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_city(self):
        return self.__city

    def get_phone_number(self):
        return self.__phone_number

    def get_gender(self):
        return self.__gender

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_city(self, city):
        self.__city = city

    def set_phone_number(self, phone):
        self.__phone_number = phone

    def set_gender(self, gender):
        self.__gender = gender

    def isLuckyPhoneNumber(self):
        return self.__phone_number.count("7") > 3

    def display(self):
        print(f"ID: {self.__id}")
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"City: {self.__city}")
        print(f"Phone: {self.__phone_number}")
        print(f"Gender: {self.__gender.value}")
        print(f"Lucky phone: {self.isLuckyPhoneNumber()}")
        print("-" * 35)
        
        
class Party:
    def __init__(self, day, reason):
        self.day = day
        self.reason = reason
        self.guests = []

    def __del__(self):
        print("Party deleted.")

    def add_guest(self, guest):
        self.guests.append(guest)

    def findAverageAge(self, gender):
        selected = [g.get_age() for g in self.guests if g.get_gender() == gender]

        if len(selected) == 0:
            return 0

        return sum(selected) / len(selected)

    def sortById(self):
        self.guests.sort(key=lambda guest: guest.get_id())

    def displayGuests(self):
        print(f"\nParty: {self.reason}")
        print(f"Day: {self.day}\n")

        for guest in self.guests:
            guest.display()
            

def main():
    party = Party("20.11.2026", "Birthday")
    
    g1 = Guest(1, "Ivan", 20, "Lviv", "0987873695", Gender.MALE)
    g2 = Guest(2, "Anna", 20, "Lviv", "0983473645", Gender.FEMALE)
    g3 = Guest(5, "Ivan", 20, "Lviv", "0988773643", Gender.MALE)
    
    party.add_guest(g1)
    party.add_guest(g2)
    party.add_guest(g3)
    
    for guest in party.guests:
        print(guest.get_name())
        
        
    print("Guests before sorting:")
    party.displayGuests()

    party.sortById()

    print("\nGuests after sorting by ID:")
    party.displayGuests()

    print("Average age (MALE):", party.findAverageAge(Gender.MALE))
    print("Average age (FEMALE):", party.findAverageAge(Gender.FEMALE))
    print("Average age (NON_BINARY):", party.findAverageAge(Gender.NON_BINARY))

if __name__ == "__main__":
   main()