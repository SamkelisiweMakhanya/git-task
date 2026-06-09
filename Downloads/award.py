def get_award(total_time):
     if total_time <= 100:
        print(" Award: Provincial colors")
     elif 101 <= total_time <= 105:
        print("Award: Provincial half colors")
     elif 106 <= total_time <= 110:
        print("Award: Provincial scroll")
     elif total_time >= 111:
        print("No award")

def main():
           print("Results\n")
swimming_min = float(input("Enter thenumber of minutes taken to finish swimming: "))
cycling_min = float(input("Enter the number of minutes taken to finish cycling: "))
running_min = float(input("Enter the number of minutes taken to finish running: "))
total_time = swimming_min + cycling_min + running_min
award = get_award(total_time)
print("\n---Results--")
print(f"Total time taken to complete triathlon is: {total_time} minutes")
print(get_award(total_time))


