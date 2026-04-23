# Smart Event & Space Scheduler (SESS)
events = []
while True:
    print("\n1. Add Event")
    print("2. View Events")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Event Name: ")
        date = input("Date: ")
        venue = input("Venue: ")
        # Check duplicate booking
        booked = False
        for e in events:
            if e[1] == date and e[2] == venue:
                booked = True
                break
        if booked:
            print("Venue already booked on this date!")
        else:
            events.append([name, date, venue])
            print("Event Added Successfully!")
    elif choice == "2":
        if len(events) == 0:
            print("No events scheduled.")
        else:
            for e in events:
                print("Event:", e[0], "| Date:", e[1], "| Venue:", e[2])

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!") 
