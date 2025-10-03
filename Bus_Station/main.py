import math


# 10/03/2025 Bloomberg Coding Challenge 26ng 1st Round
# --------------------------------Origianl Qeustion Start --------------------------------
# You are given a list of stations represented as a string separated by hyphens ('-'),
# and a dictionary bus_list that maps each bus_id to its current station.
# The buses only move from left to right along the stations (e.g., A → B → C → …).
# You need to implement a system with the following methods:


# def __init__(self, bus_list: dict[int, str], stations: str):
#     # constructor: initialize buses and stations

# def closest_bus(self, station_id: str) -> int:
#     """
#     return how far is the closest bus to station_id.
#     """
#
# def find_location_bus(self, bus_id: int) -> str:
#     """
#     Return the station name where the given bus_id is currently located.
#     """

# def move(self) -> None:
#     """
#     Move all buses one station to the right.
#     If a bus is already at the last station, it will remain there.
#     """
# stations = "A-B-C-D-E-F-G"
# bus_list = {1: "B", 3: "F"}
# closest_bus(A) = -1 no bus on left
# closest_bus(B) = 0
# closest_bus(C) = 1
# closest_bus(D) = 2
# closest_bus(E) = 3
# closest_bus(F) = 0
# --------------------------------Origianl Qeustion End --------------------------------


# --------------------------------Follow Up --------------------------------
# follow-up: all operations in O(1)
# --------------------------------Follow Up --------------------------------

# Question:
# You are given a list of stations represented as a string separated by hyphens (-), and a dictionary bus_list that maps each bus_id to its current station.
# The buses only move from left to right along the stations (e.g., A → B → C …).


class Bus_Station:  # You need to implement a system with the following methods:class Bus_Station:
    def __init__(self, bus_list: dict[int, str], stations: str):
        """
        Constructor: initializes buses and stations.
        """
        self.stations = stations.split("-")
        self.bus_locations = bus_list
        # Create a helper dictionary for quick station-to-index lookups
        self.station_to_index = {station: i for i, station in enumerate(self.stations)}

    def closest_bus(self, station_id: str) -> int:
        """
        Return how far is the closest bus to the left of (or at) station_id.
        """
        if station_id not in self.station_to_index:
            return -1  # Station does not exist

        target_index = self.station_to_index[station_id]
        min_distance = math.inf

        # Check every bus's location
        for current_bus_station in self.bus_locations.values():
            bus_index = self.station_to_index[current_bus_station]

            # Consider only buses at or to the left of the target station
            if bus_index <= target_index:
                distance = target_index - bus_index
                if distance < min_distance:
                    min_distance = distance

        # If min_distance was never updated, no bus was found
        if min_distance == math.inf:
            return -1
        else:
            return min_distance

    def find_location_bus(self, bus_id: int) -> str:
        """
        Return the station name where the given bus_id is currently located.
        """
        return self.bus_locations.get(bus_id)

    def move(self) -> None:
        """
        Move all buses one station to the right.
        If a bus is already at the last station, it will remain there.
        """
        last_station_index = len(self.stations) - 1

        for bus_id, current_station in self.bus_locations.items():
            current_index = self.station_to_index[current_station]

            # Move the bus to the next station if it's not at the end
            if current_index < last_station_index:
                next_station = self.stations[current_index + 1]
                self.bus_locations[bus_id] = next_station


# Example usage from the problem description:
stations_str = "A-B-C-D-E-F-G"
bus_list_dict = {1: "B", 3: "F"}

# Create an instance of the system
bus_system = Bus_Station(bus_list_dict, stations_str)

# --- Verification ---
print(f"Closest bus to A: {bus_system.closest_bus('A')}")  # Expected: -1
print(f"Closest bus to B: {bus_system.closest_bus('B')}")  # Expected: 0
print(f"Closest bus to C: {bus_system.closest_bus('C')}")  # Expected: 1
print(f"Closest bus to D: {bus_system.closest_bus('D')}")  # Expected: 2
print(f"Closest bus to E: {bus_system.closest_bus('E')}")  # Expected: 3
print(f"Closest bus to F: {bus_system.closest_bus('F')}")  # Expected: 0

print("-" * 20)

# Find bus locations
print(f"Location of bus 1: {bus_system.find_location_bus(1)}")  # Expected: B
print(f"Location of bus 3: {bus_system.find_location_bus(3)}")  # Expected: F

print("-" * 20)

# Move the buses
print("Moving all buses...")
bus_system.move()

# Check new locations
print(f"New location of bus 1: {bus_system.find_location_bus(1)}")  # Expected: C
print(f"New location of bus 3: {bus_system.find_location_bus(3)}")  # Expected: G
