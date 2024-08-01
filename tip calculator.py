# Tip Calculator

print("Welcome to the tip calculator!")

# Function to get a valid tip percentage from the user
def get_valid_tip():
    while True:
        try:
            tip_input = input("How much tip would you like to give? 10%, 12%, or 15%: ").strip()
            if tip_input.endswith('%'):
                tip_input = tip_input[:-1]  # Remove the '%' sign
            tip_percentage = int(tip_input)
            if tip_percentage in [10, 12, 15]:
                return tip_percentage
            else:
                print("Please enter a valid tip percentage (10, 12, or 15).")
        except ValueError:
            print("Invalid input. Please enter a number (10, 12, or 15).")

# User inputs for bill and group size
total_bill = float(input("What was the total bill?: £"))
tip_percentage = get_valid_tip()
group_size = int(input("How many people to split the bill? "))

# Calculation
tip_multiplier = (tip_percentage / 100) + 1  # Convert tip percentage to a multiplier
cost_per_person = total_bill * tip_multiplier / group_size  # Calculate the cost per person

# Final result
print(f"Each person should pay: £{cost_per_person:.2f}")

# Check if the chosen tip percentage is reasonable
if tip_percentage < 10:
    print("A tip below 10% is considered low.")
elif tip_percentage <= 15:
    print("A tip between 10% and 15% is considered reasonable.")
else:
    print("A tip above 15% is considered generous.")
