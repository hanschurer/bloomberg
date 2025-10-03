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
