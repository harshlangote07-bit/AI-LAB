# Vacuum Cleaner Problem
# Goal-Based Agent

# Taking input from the user
room_a = input("Enter status of Room A (dirty/clean): ").lower()
room_b = input("Enter status of Room B (dirty/clean): ").lower()
position = input("Enter vacuum cleaner position (A/B): ").upper()

print("\nInitial State:")
print("Room A:", room_a)
print("Room B:", room_b)
print("Vacuum Position:", position)

print("\n--- Agent Actions ---")

# Continue until both rooms are clean
while room_a == "dirty" or room_b == "dirty":

    # If vacuum is in Room A
    if position == "A":

        # If Room A is dirty, suck the dirt
        if room_a == "dirty":
            print("Vacuum is in Room A -> SUCK")
            room_a = "clean"

        # If Room A is clean but Room B is dirty, move to B
        elif room_b == "dirty":
            print("Room A is clean -> MOVE RIGHT to Room B")
            position = "B"

    # If vacuum is in Room B
    elif position == "B":

        # If Room B is dirty, suck the dirt
        if room_b == "dirty":
            print("Vacuum is in Room B -> SUCK")
            room_b = "clean"

        # If Room B is clean but Room A is dirty, move to A
        elif room_a == "dirty":
            print("Room B is clean -> MOVE LEFT to Room A")
            position = "A"

# Final state
print("\n--- Final State ---")
print("Room A:", room_a)
print("Room B:", room_b)
print("Vacuum Position:", position)

print("\nGoal Reached!")
print("Both rooms are clean.")