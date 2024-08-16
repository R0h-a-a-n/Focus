from timer import Timer

def main():
    timer = Timer()

    duration_input = input("Enter the duration for the timer in seconds: ")

    try:
        duration = int(duration_input)

        if duration > 0:
            def on_start():
                print("Timer started!")

            def on_tick(remaining_time):
                print(f"Time remaining: {remaining_time} seconds")

            def on_end():
                print("Time's up!")

            timer.start_timer(duration, on_timer_start=on_start, on_timer_tick=on_tick, on_timer_end=on_end)
        else:
            print("Please enter a positive duration.")

    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()
