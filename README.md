# 🚗 Vehicle Dashboard

A real-time vehicle dashboard simulator built with Python and Tkinter. This desktop application provides a visually rich, dark-themed interface that displays live-updating vehicle telemetry — including speed, RPM, fuel level, engine temperature, tire pressures, engine oil status, and an integrated camera module for image capture and processing.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Speedometer** | Displays current vehicle speed in km/h with live simulation |
| **RPM Gauge** | Shows engine RPM (×1000), dynamically linked to speed |
| **Fuel Level** | Tracks fuel consumption in real time (depletes while moving) |
| **Temperature Monitor** | Engine temperature gauge that responds to RPM changes |
| **Tire Pressure Display** | Individual PSI readings for all 4 tires with realistic fluctuations |
| **Engine Oil Status** | Visual indicator that toggles between healthy (green) and warning (red) states |
| **Camera Capture** | Captures images via webcam and displays original, degraded, and reconstructed versions |

---

## 📸 Screenshots

> Run the application to see the dashboard in action — a dark-themed interface (800×600) with color-coded gauges and live-updating telemetry.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **GUI Framework:** Tkinter / ttk
- **Computer Vision:** OpenCV (`cv2`)
- **Image Processing:** Pillow (`PIL`)

---

## 📦 Prerequisites

- Python 3.7 or higher
- A webcam (optional — required only for the image capture feature)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/keerthireddypothula-code/vehicledashboard
cd Vehicle-Dashboard
```

### 2. Install Dependencies

```bash
pip install opencv-python Pillow
```

> **Note:** `tkinter` is included with standard Python installations. If it's missing, install it via your system's package manager (e.g., `sudo apt install python3-tk` on Ubuntu).

### 3. Run the Application

```bash
python main.py
```

---

## 📁 Project Structure

```
Vehicle-Dashboard/
├── main.py        # Main application — dashboard GUI and simulation logic
└── README.md      # Project documentation
```

---

## ⚙️ How It Works

### Dashboard Simulation

The dashboard simulates realistic vehicle behavior using randomized parameter updates every **1 second**:

- **Speed** fluctuates within 0–200 km/h with incremental changes
- **RPM** is derived from speed with a random variance
- **Temperature** increases with higher RPM (range: 70–120 °C)
- **Fuel** gradually depletes when the vehicle is in motion
- **Tire Pressures** drift slightly within a realistic range (28–35 PSI)

### Engine Oil Indicator

The oil status toggles between **green** (healthy) and **red** (warning) every **60 seconds**, simulating periodic status checks.

### Camera Module

Clicking **"Capture Image"** activates the webcam and performs:

1. **Original** — Raw captured frame
2. **Degraded** — Gaussian blur applied to simulate degradation
3. **Reconstructed** — Weighted combination to sharpen and restore detail

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---


