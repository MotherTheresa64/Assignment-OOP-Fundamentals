# Task 1: Vehicle Registration System
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    
    def update_owner(self, new_owner):
        """Update the owner of the vehicle."""
        self.owner = new_owner

    def __str__(self):
        return f"Vehicle(reg_num={self.registration_number}, type={self.type}, owner={self.owner})"

# Creating instances of Vehicle
vehicle1 = Vehicle("ABC123", "Sedan", "John Doe")
vehicle2 = Vehicle("XYZ789", "SUV", "Jane Smith")

# Demonstrating the update_owner method
print("Before updating owner:")
print(vehicle1)
print(vehicle2)

vehicle1.update_owner("Alice Johnson")
vehicle2.update_owner("Bob Brown")

print("\nAfter updating owner:")
print(vehicle1)
print(vehicle2)

# Task 2: Event Management System Enhancement
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
    
    def add_participant(self):
        """Increase the participant count by one."""
        self.participant_count += 1
    
    def get_participant_count(self):
        """Return the current number of participants."""
        return self.participant_count

    def __str__(self):
        return f"Event(name={self.name}, date={self.date}, participants={self.participant_count})"

# Creating an instance of Event
event1 = Event("Music Festival", "2024-08-15")

# Adding participants and getting the participant count
print("Initial event details:")
print(event1)

event1.add_participant()
event1.add_participant()
event1.add_participant()

print("\nEvent details after adding participants:")
print(event1)
