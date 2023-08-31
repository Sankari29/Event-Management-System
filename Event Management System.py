import json

class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location

class EventManager:
    def __init__(self):
        self.events = []

    def create_event(self, name, date, location):
        event = Event(name, date, location)
        self.events.append(event)
        print("Event '{}' created.".format(name))

    def view_events(self):
        if not self.events:
            print("No events available.")
        else:
            print("Upcoming Events:")
            for event in self.events:
                print("Name: {}\nDate: {}\nLocation: {}\n".format(event.name, event.date, event.location))

    def save_events(self, filename):
        event_list = []
        for event in self.events:
            event_list.append({
                'name': event.name,
                'date': event.date,
                'location': event.location
            })
        with open(filename, 'w') as file:
            json.dump(event_list, file)
        print("Events saved to '{}'.".format(filename))

    def load_events(self, filename):
        try:
            with open(filename, 'r') as file:
                event_list = json.load(file)
                for event_data in event_list:
                    event = Event(event_data['name'], event_data['date'], event_data['location'])
                    self.events.append(event)
            print("Events loaded from '{}'.".format(filename))
        except FileNotFoundError:
            print("File '{}' not found. No events loaded.".format(filename))

if __name__ == "__main__":
    event_manager = EventManager()
    save_file = "events.shank"

    event_manager.load_events(save_file)

    while True:
        print("\nEvent Management System")
        print("1. Create Event")
        print("2. View Events")
        print("3. Save Events")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter event name: ")
            date = input("Enter event date: ")
            location = input("Enter event location: ")
            event_manager.create_event(name, date, location)
        elif choice == "2":
            event_manager.view_events()
        elif choice == "3":
            event_manager.save_events(save_file)
        elif choice == "4":
            print("Exiting the Event Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
