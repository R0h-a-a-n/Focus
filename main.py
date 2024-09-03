from timer import Timer
from blocker import block_websites, unblock_websites, get_websites_to_block
from app_blocker import block_applications, unblock_applications, get_apps_to_block
import threading

def main():
    print("Select an option:")
    print("1. Block Websites")
    print("2. Block Applications")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        websites = get_websites_to_block()
        if not websites:
            print("No websites to block.")
            return
        apps_to_block = []
    elif choice == '2':
        apps_to_block = get_apps_to_block()
        if not apps_to_block:
            print("No applications to block.")
            return
        websites = []
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    timer = Timer()

    duration_input = input("Enter the duration for the timer in seconds: ")

    try:
        duration = int(duration_input)

        if duration > 0:
            def on_start():
                print("Timer started!")
                if websites:
                    block_websites(websites)
                if apps_to_block:
                    threading.Thread(target=block_applications, args=(apps_to_block,), daemon=True).start()

            def on_tick(remaining_time):
                print(f"Time remaining: {remaining_time} seconds")

            def on_end():
                print("Time's up!")
                if websites:
                    unblock_websites(websites)
                if apps_to_block:
                    unblock_applications(apps_to_block)

            timer.start_timer(duration, on_timer_start=on_start, on_timer_tick=on_tick, on_timer_end=on_end)
        else:
            print("Please enter a positive duration.")

    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()
