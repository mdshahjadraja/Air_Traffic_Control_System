# Air_Traffic_Control_System

## Overview
The **Air Traffic Control System** is a Python-based application that allows users to manage airports, add flight routes, and find the shortest path between two airports using **Dijkstra's Algorithm**. The application features a graphical user interface (GUI) built with **Tkinter**.

## Features
- **Add Airports**: Users can add multiple airports to the system.
- **Add Flight Routes**: Users can create connections between airports with specified distances.
- **Find Shortest Path**: Calculates the shortest distance between two airports using Dijkstra’s Algorithm.
- **User-Friendly GUI**: A simple Tkinter-based interface for easy interaction.

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Install and Run
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/air-traffic-control-system.git
   cd air-traffic-control-system
   ```
2. Install required dependencies (if any):
   ```sh
   pip install tk
   ```
3. Run the application:
   ```sh
   python air_traffic_control.py
   ```

## How to Use
1. **Add an Airport**
   - Enter an airport name in the input field.
   - Click **“Add Airport”** to add it to the system.

2. **Add a Flight Route**
   - Enter two connected airport names and the flight distance.
   - Click **“Add Flight Route”** to save the connection.

3. **Find the Shortest Path**
   - Enter the **start airport** and **destination airport**.
   - Click **“Find Shortest Path”** to compute the shortest route.
   - A message box will display the **shortest flight distance**.

## Algorithm Used
The project implements **Dijkstra’s Algorithm** to find the shortest path between two airports. It uses a priority queue to determine the minimum distance required to travel between nodes (airports) efficiently.

## Example Scenario
1. Add airports: **A, B, C**
2. Add flight routes:
   - A → B (Distance: 3)
   - B → C (Distance: 2)
   - A → C (Distance: 7)
3. Find the shortest path from **A to C**
   - The shortest route is **A → B → C
