import tkinter as tk
from datetime import datetime
import time
import math
import pytz

class WorldClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("World Clock")
        
        # Analog Clock
        self.analog_canvas = tk.Canvas(root, width=400, height=400, bg="lightblue")  # Change background color
        self.analog_canvas.pack()

        # Add Circle for Analog Clock
        self.analog_canvas.create_oval(40, 40, 360, 360, width=2, outline="black")  # Increase size of the circle

        # Digital Clock
        self.digital_label = tk.Label(root, font=("Helvetica", 24))
        self.digital_label.pack(pady=10)

        # Time Zone Selection
        self.time_zones = ["UTC", "America/New_York", "Europe/London", "Asia/Tokyo", "Asia/Kolkata", "Australia/Sydney", "America/Los_Angeles"]
        self.selected_time_zone = tk.StringVar()
        self.selected_time_zone.set(self.time_zones[0])
        
        # Label for Time Zone Selection
        self.time_zone_label = tk.Label(root, text="Select the time zone:")
        self.time_zone_label.pack(pady=5, padx=10, anchor=tk.W)

        # Time Zone Dropdown
        self.time_zone_menu = tk.OptionMenu(root, self.selected_time_zone, *self.time_zones, command=self.update_clock)
        self.time_zone_menu.pack(pady=5, padx=10, anchor=tk.W)

        # Analog Clock Hands
        self.hour_hand = None
        self.minute_hand = None
        self.second_hand = None

        # Analog Clock Numbers
        self.draw_clock_numbers()

        # Initial Update
        self.update_clock()
        self.root.after(1000, self.update_clock)

    def update_clock(self, _=None):
        selected_time_zone = self.selected_time_zone.get()
        tz = pytz.timezone(selected_time_zone)
        current_time = datetime.now(tz)
        
        hour = current_time.hour % 12
        minute = current_time.minute
        second = current_time.second

        self.update_analog_clock(hour, minute, second)
        self.update_digital_clock(current_time)

        self.root.after(1000, self.update_clock)

    def update_analog_clock(self, hour, minute, second):
        self.analog_canvas.delete("all")
        self.analog_canvas.create_oval(40, 40, 360, 360, width=2, outline="black")  # Increase size of the circle
        self.draw_clock_numbers()
        self.update_hand(self.hour_hand, hour * 30 + minute * 0.5, 80, "blue")    # Decrease length
        self.update_hand(self.minute_hand, minute * 6, 110, "green")               # Decrease length
        self.update_hand(self.second_hand, second * 6, 130, "red")                 # Decrease length

    def update_digital_clock(self, current_time):
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S %Z")
        self.digital_label.config(text=formatted_time)

    def update_hand(self, hand, angle, length, color):
        angle_rad = math.radians(angle - 90)
        x = 200 + length * math.cos(angle_rad)
        y = 200 + length * math.sin(angle_rad)
        hand = self.analog_canvas.create_line(200, 200, x, y, width=3, arrow=tk.LAST, fill=color)

    def draw_clock_numbers(self):
        for i in range(12):
            angle = math.radians(i * 30 - 60)  # 30 degrees per hour, starting from 12 o'clock
            x = 200 + 0.95 * 150 * math.cos(angle)  # 0.75 is to adjust for the distance from the center
            y = 200 + 0.95 * 150 * math.sin(angle)
            self.analog_canvas.create_text(x, y, text=str(i + 1), font=("Helvetica", 12, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = WorldClockApp(root)
    root.mainloop()
