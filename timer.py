import time
import threading

class Timer:
    def __init__(self):
        self._timer_thread = None
        self._remaining_time = 0
        self._is_paused = False
        self._is_running = False

    def start_timer(self, duration, on_timer_start=None, on_timer_tick=None, on_timer_end=None):
        if self._is_running:
            print("Timer is already running.")
            return

        self._remaining_time = duration
        self._is_running = True
        self._is_paused = False

        if on_timer_start:
            on_timer_start()

        self._timer_thread = threading.Thread(target=self._run_timer, args=(on_timer_tick, on_timer_end))
        self._timer_thread.start()

    def _run_timer(self, on_timer_tick, on_timer_end):
        while self._remaining_time > 0 and self._is_running:
            if not self._is_paused:
                time.sleep(1)
                self._remaining_time -= 1

                if on_timer_tick:
                    on_timer_tick(self._remaining_time)

        if self._remaining_time == 0 and self._is_running:
            if on_timer_end:
                on_timer_end()

        self._is_running = False

    def pause_timer(self):
        if self._is_running and not self._is_paused:
            self._is_paused = True
            print("Timer paused.")

    def resume_timer(self):
        if self._is_running and self._is_paused:
            self._is_paused = False
            print("Timer resumed.")

    def stop_timer(self):
        self._is_running = False
        self._remaining_time = 0
        print("Timer stopped.")

    def get_remaining_time(self):
        return self._remaining_time

