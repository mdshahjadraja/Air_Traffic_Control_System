import tkinter as tk
from tkinter import messagebox
import heapq

# Air Traffic Control System Class
class AirTrafficControlSystem:
    def __init__(self):
        self.airports = {}  # Dictionary to store airport names
        self.graph = {}  # Graph to store flight routes (edges) and their weights (distances)

    # Method to add an airport to the system
    def add_airport(self, airport):
        if airport in self.airports:
            return False  # Airport already exists
        self.airports[airport] = None
        self.graph[airport] = []
        return True

    # Method to add a flight route between two airports with a weight (distance)
    def add_flight_route(self, airport1, airport2, distance=1):
        if airport1 in self.graph and airport2 in self.graph:
            self.graph[airport1].append((airport2, distance))
            self.graph[airport2].append((airport1, distance))  # Since it's a bidirectional route
            return True
        return False

    # Dijkstra's Algorithm to find the shortest path
    def dijkstra(self, start, end):
        # Dictionary to store the shortest distance to each airport
        dist = {airport: float('inf') for airport in self.airports}
        dist[start] = 0
        pq = [(0, start)]  # Priority queue to choose the airport with the smallest distance
        
        while pq:
            current_dist, current = heapq.heappop(pq)

            if current_dist > dist[current]:
                continue

            for neighbor, weight in self.graph[current]:
                new_dist = current_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return dist.get(end, float('inf'))  # Return the shortest distance to the end airport


# GUI with Tkinter
class AirTrafficControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Air Traffic Control System")
        self.atc_system = AirTrafficControlSystem()

        # GUI Elements for Airport and Flight Route Input
        tk.Label(root, text="Airport Name").grid(row=0, column=0, padx=10, pady=5)
        self.airport_entry = tk.Entry(root)
        self.airport_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Flight Route Distance").grid(row=1, column=0, padx=10, pady=5)
        self.flight_distance_entry = tk.Entry(root)
        self.flight_distance_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(root, text="Add Airport", command=self.add_airport).grid(row=2, column=0, columnspan=2, pady=5)
        tk.Button(root, text="Add Flight Route", command=self.add_flight_route).grid(row=3, column=0, columnspan=2, pady=5)

        tk.Label(root, text="Start Airport").grid(row=4, column=0, padx=10, pady=5)
        self.start_airport_entry = tk.Entry(root)
        self.start_airport_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(root, text="End Airport").grid(row=5, column=0, padx=10, pady=5)
        self.end_airport_entry = tk.Entry(root)
        self.end_airport_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Button(root, text="Find Shortest Path", command=self.find_shortest_path).grid(row=6, column=0, columnspan=2, pady=5)

    def add_airport(self):
        airport = self.airport_entry.get()
        if airport:
            if self.atc_system.add_airport(airport):
                messagebox.showinfo("Success", f"Airport {airport} added.")
            else:
                messagebox.showerror("Error", f"Airport {airport} already exists.")
        else:
            messagebox.showerror("Error", "Please enter an airport name.")

    def add_flight_route(self):
        airport1 = self.airport_entry.get()
        flight_distance = self.flight_distance_entry.get()
        if airport1 and flight_distance:
            try:
                distance = int(flight_distance)
                airport2 = self.end_airport_entry.get()
                if self.atc_system.add_flight_route(airport1, airport2, distance):
                    messagebox.showinfo("Success", f"Flight route added between {airport1} and {airport2}.")
                else:
                    messagebox.showerror("Error", "One or both airports not found.")
            except ValueError:
                messagebox.showerror("Error", "Invalid flight route distance.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def find_shortest_path(self):
        start = self.start_airport_entry.get()
        end = self.end_airport_entry.get()
        if start in self.atc_system.airports and end in self.atc_system.airports:
            distance = self.atc_system.dijkstra(start, end)
            if distance == float('inf'):
                messagebox.showinfo("Result", "No path found.")
            else:
                messagebox.showinfo("Result", f"Shortest flight distance: {distance}")
        else:
            messagebox.showerror("Error", "One or both airports not found.")


# Main function to run the Tkinter GUI
def main():
    root = tk.Tk()
    app = AirTrafficControlApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
