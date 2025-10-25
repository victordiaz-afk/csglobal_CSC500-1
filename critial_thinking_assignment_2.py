print('Part 1: Tip Calculator\n')
print("This program calculates 7% and 18% tips on a bill.")
bill = float(input("Enter the bill amount: "))
tip_7 = bill * 0.07
tip_18 = bill * 0.18

print("\nTip amount at 7%: ", tip_7)
print("Total amount at 7%: ", bill + tip_7)
print("Tip amount at 18%: ", tip_18)
print("Total amount at 18%: ", bill + tip_18)



print('\nPart 2: 24 hour Alarm Clock\n')
def calculate_alarm(current_time, wait_hours):
    return str((current_time//100 + wait_hours//100) % 24) + ":" + str((current_time%100 + wait_hours%100) % 60)

input_correct = False

while not input_correct:
    time = int(input("Enter the current time in hours (0000-2359): "))
    if not (0 <= time <= 2359):
        print("Invalid time. Please enter a time between 0000 and 2359.")
    else:  
        while not input_correct:
            alarm_time = int(input("Enter the hours to wait for the alarm in hours (0000-2359): "))
            if not (0 <= alarm_time <= 2359):
                print("Invalid alarm time. Please enter a time between 0000 and 2359.")
            else:
                input_correct = True

alarm_time = calculate_alarm(time, alarm_time)
print("The alarm will ring at", alarm_time)