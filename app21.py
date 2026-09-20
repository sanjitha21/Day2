import time
pin_history = []
correct_pin = 1234
attempts = 0
while attempts < 3:
    entered_pin = int(input("Enter your pin number: "))
    pin_history.append(entered_pin)
    if entered_pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Access Denied")
        attempts += 1

show_history = input("Do you want to see the pin history? (yes/no): ")
if show_history.lower() == 'yes':
    print("Pin history:")
    for pin in pin_history:
        print(pin)

