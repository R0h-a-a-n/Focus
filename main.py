from timer import Timer
from blocker import block_websites, unblock_websites, get_websites_to_block

def main():
    websites = get_websites_to_block()

    if not websites:
        print("No websites to block.")
        return

    timer = Timer()

    duration_input = input("Enter the duration for the timer in seconds: ")

    try:
        duration = int(duration_input)

        if duration > 0:
            def on_start():
                print("Timer started!")
                block_websites(websites)

            def on_tick(remaining_time):
                print(f"Time remaining: {remaining_time} seconds")

            def on_end():
                print("Time's up!")
                unblock_websites(websites)

            timer.start_timer(duration, on_timer_start=on_start, on_timer_tick=on_tick, on_timer_end=on_end)
        else:
            print("Please enter a positive duration.")

    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()
