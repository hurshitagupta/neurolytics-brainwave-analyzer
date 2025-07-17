# 🧠 Brain Signal Analyzer (NumPy Only Project)

This is a logic-heavy, NumPy-based project that simulates and analyzes brain signal data from multiple subjects over time. It focuses purely on core Python and NumPy — no visualization or external libraries — to showcase data manipulation, simulation, and analysis skills.

---

## 📁 Folder Structure

brain-signal-analyzer/
│
├── 01_data_generation/
│ └── simulate_brain_data.py # Generates and saves simulated brain signal data
│
├── 02_analysis/
│ └── subject_analysis.py # Computes average and max signal values for each subject
│
├── 03_classification/
│ └── spike_detection.py # Detects abnormal spikes based on signal averages
│
├── brain_data.npy # Simulated data file (NumPy array)
└── README.md # Project documentation

---

## 🧠 Dataset

The `brain_data.npy` file is a 3D NumPy array with the shape:  
`(5 subjects, 60 seconds, 4 signals)`  

Signal Types:
- `delta`
- `theta`
- `alpha`
- `beta`

---

## 📊 Features Implemented

### ✔️ Data Generation (`01_data_generation`)
- Simulates brainwave data using random values
- Stores the signal data as a `.npy` file for future use

### ✔️ Signal Analysis (`02_analysis`)
- Calculates average signal value per subject
- Calculates max signal value per subject

### ✔️ Spike Detection (`03_classification`)
- Detects and displays **abnormal spikes**:
  > Any value greater than the subject’s average for a given signal is treated as a spike

---

## 🧾 Sample Output (from `spike_detection.py`)

Abnormal Spikes Of Subject 0
delta : [ 2  4  5  8 11 13 14 19 20 21 22 25 27 31 32 33 34 37 38 41 42 43 44 45 47 49 50 52 55 58 59]

theta : [ 0  3  4  5  8  9 10 14 15 19 20 21 22 26 30 33 35 37 39 41 45 46 48 50 52 53 54]

alpha : [ 0  3  4  5  7 10 11 17 18 26 29 30 37 38 40 41 42 44 47 49 50 52 54 55 59]

beta : [ 1  2  3  4  6  7  9 12 13 15 16 17 18 21 22 23 32 33 36 38 41 42 44 46 47 50 51 53 54 55 56 59]
******************************
---

## 🎯 Goal of the Project

This project is built to demonstrate:
- Strong logic-building using core Python
- Efficient use of NumPy arrays for real-world signal-like data
- Modular structure using folders and functions
- Clean code practices (no hardcoding, reusable logic)

---

## 🧠 Skills Used

- NumPy slicing, indexing, `where`, `mean`, `max`, `random`
- Python functions, loops, and structure
- Realistic simulation and detection logic

---

## 🚀 Future Scope (Optional Enhancements)

- Add Matplotlib bar charts for average signal visualization
- Create a GUI or dashboard to explore signal patterns
- Include CSV export for average/max/spike data

---

### 🚀 Tech Stack & Tags

`#Python` `#NumPy` `#SignalProcessing` `#BrainDataAnalysis` `#BeginnerProject` `#RecruiterFriendly` `#LogicBuilding` `#MiniMajor`

---

> ✅ Made with logic, not libraries 😉
