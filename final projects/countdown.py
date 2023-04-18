# Import the time module
import time

# Ask the user for the number of seconds to count down
seconds = input("Enter the number of seconds to count down: ")

# Convert the input string to an integer
seconds = int(seconds)

# Start the countdown
while seconds > 0:
    # Print the current remaining number of seconds
    print(seconds)

    # Sleep for one second
    time.sleep(1)

    # Decrement the number of seconds remaining
    seconds -= 1

# Print a message when the countdown is complete
print("Countdown complete!")
