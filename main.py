import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import random


class VehicleDashboard:
    def __init__(self, root):  # Corrected __init_ method
        self.root = root
        self.root.title("Vehicle Dashboard")
        self.root.geometry("800x600")
        self.root.configure(bg="#2C3E50")

        # Initialize parameters
        self.current_speed = 0
        self.current_rpm = 0
        self.current_temp = 70
        self.current_fuel = 100
        self.tyre_pressures = [32, 32, 32, 32]
        self.oil_color_state = True

        # Create the dashboard layout
        self.create_widgets()
        self.update_parameters()
        self.toggle_oil_color()

    def create_widgets(self):
        # Speed and RPM gauge
        self.gauge_frame = tk.Frame(self.root, bg="#2C3E50")
        self.gauge_frame.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        # Speed indicator
        self.speed_label = tk.Label(self.gauge_frame, text="Speed (km/h)", font=("Arial", 14), fg="cyan", bg="#2C3E50")
        self.speed_label.grid(row=0, column=0, padx=10)
        self.speed_var = tk.StringVar(value="0")
        self.speed_value = tk.Label(self.gauge_frame, textvariable=self.speed_var, font=("Arial", 24, "bold"), fg="cyan", bg="#2C3E50")
        self.speed_value.grid(row=1, column=0, padx=10)

        # RPM indicator
        self.rpm_label = tk.Label(self.gauge_frame, text="RPM (x1000)", font=("Arial", 14), fg="orange", bg="#2C3E50")
        self.rpm_label.grid(row=0, column=1, padx=10)
        self.rpm_var = tk.StringVar(value="0")
        self.rpm_value = tk.Label(self.gauge_frame, textvariable=self.rpm_var, font=("Arial", 24, "bold"), fg="orange", bg="#2C3E50")
        self.rpm_value.grid(row=1, column=1, padx=10)

        # Fuel and Temperature indicators
        self.info_frame = tk.Frame(self.root, bg="#2C3E50")
        self.info_frame.grid(row=1, column=0, columnspan=2, pady=20)

        # Fuel indicator
        self.fuel_label = tk.Label(self.info_frame, text="Fuel Level", font=("Arial", 14), fg="lime", bg="#2C3E50")
        self.fuel_label.grid(row=0, column=0, padx=20)
        self.fuel_var = tk.StringVar()
        self.fuel_value = tk.Label(self.info_frame, textvariable=self.fuel_var, font=("Arial", 18), fg="lime", bg="#2C3E50")
        self.fuel_value.grid(row=1, column=0)

        # Temperature indicator
        self.temp_label = tk.Label(self.info_frame, text="Temperature (°C)", font=("Arial", 14), fg="red", bg="#2C3E50")
        self.temp_label.grid(row=0, column=1, padx=20)
        self.temp_var = tk.StringVar()
        self.temp_value = tk.Label(self.info_frame, textvariable=self.temp_var, font=("Arial", 18), fg="red", bg="#2C3E50")
        self.temp_value.grid(row=1, column=1)

        # Tire pressures
        self.tyre_frame = tk.Frame(self.root, bg="#2C3E50")
        self.tyre_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.tyre_label = tk.Label(self.tyre_frame, text="Tire Pressures (PSI)", font=("Arial", 12), fg="white", bg="#2C3E50")
        self.tyre_label.grid(row=0, column=0, columnspan=4, pady=(0, 10))

        self.tyre_vars = [tk.StringVar() for _ in range(4)]
        for i in range(4):
            tyre_canvas = tk.Canvas(self.tyre_frame, width=70, height=50, bg="#2C3E50", highlightthickness=0)
            tyre_canvas.create_rectangle(5, 5, 65, 45, outline="yellow", width=2)
            tyre_canvas.grid(row=1, column=i, padx=10)
            tyre_label = tk.Label(tyre_canvas, text=f"Tyre {i + 1}", font=("Arial", 8), fg="white", bg="#2C3E50")
            tyre_label.place(x=12, y=5)
            tyre_pressure = tk.Label(tyre_canvas, textvariable=self.tyre_vars[i], font=("Arial", 12), fg="yellow", bg="#2C3E50")
            tyre_pressure.place(x=20, y=25)

        # Engine oil status
        self.oil_frame = tk.Frame(self.root, bg="#2C3E50")
        self.oil_frame.grid(row=3, column=0, columnspan=2, pady=10)

        self.engine_oil_label = tk.Label(self.oil_frame, text="Engine Oil Status", font=("Arial", 14), bg="#2C3E50")
        self.engine_oil_label.grid(row=0, column=0, padx=10)

        # Camera button and image displays
        self.camera_button = tk.Button(self.root, text="Capture Image", command=self.capture_image, bg="orange")
        self.camera_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Frames to display images
        self.image_frame = tk.Frame(self.root, bg="#2C3E50")
        self.image_frame.grid(row=5, column=0, columnspan=2)

        self.original_label = tk.Label(self.image_frame, text="Original", bg="#2C3E50", fg="white")
        self.original_label.grid(row=0, column=0, padx=10)
        self.degraded_label = tk.Label(self.image_frame, text="Degraded", bg="#2C3E50", fg="white")
        self.degraded_label.grid(row=0, column=1, padx=10)
        self.reconstructed_label = tk.Label(self.image_frame, text="Reconstructed", bg="#2C3E50", fg="white")
        self.reconstructed_label.grid(row=0, column=2, padx=10)

        self.original_image = tk.Label(self.image_frame)
        self.original_image.grid(row=1, column=0)
        self.degraded_image = tk.Label(self.image_frame)
        self.degraded_image.grid(row=1, column=1)
        self.reconstructed_image = tk.Label(self.image_frame)
        self.reconstructed_image.grid(row=1, column=2)

    def capture_image(self):
        # Open the camera and capture an image
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if ret:
            original_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            degraded_img = cv2.GaussianBlur(original_img, (15, 15), 0)
            reconstructed_img = cv2.addWeighted(original_img, 1.5, degraded_img, -0.5, 0)

            self.display_image(self.original_image, original_img)
            self.display_image(self.degraded_image, degraded_img)
            self.display_image(self.reconstructed_image, reconstructed_img)

    def display_image(self, label, img):
        img = Image.fromarray(img)
        img = img.resize((150, 150))
        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk

    def update_parameters(self):
        self.current_speed = max(0, min(200, self.current_speed + random.choice([-1, 0, 1, 5, 10])))
        self.current_rpm = self.current_speed * 50 + random.randint(-50, 50)
        self.current_temp = max(70, min(120, self.current_temp + (self.current_rpm // 500)))
        self.current_fuel = max(0, self.current_fuel - 0.05 if self.current_speed > 0 else 0)

        for i in range(4):
            self.tyre_pressures[i] = max(28, min(35, self.tyre_pressures[i] + random.uniform(-0.1, 0.1)))

        self.speed_var.set(f"{int(self.current_speed)}")
        self.rpm_var.set(f"{int(self.current_rpm / 1000)}")
        self.fuel_var.set(f"{int(self.current_fuel)}%")
        self.temp_var.set(f"{int(self.current_temp)} °C")

        for i in range(4):
            self.tyre_vars[i].set(f"{self.tyre_pressures[i]:.1f}")

        self.root.after(1000, self.update_parameters)

    def toggle_oil_color(self):
        self.oil_color_state = not self.oil_color_state
        color = "green" if self.oil_color_state else "red"
        self.engine_oil_label.config(fg=color)
        self.root.after(60000, self.toggle_oil_color)


if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleDashboard(root)
    root.mainloop()

