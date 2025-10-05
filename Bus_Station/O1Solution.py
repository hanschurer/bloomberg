'''
10/03/2025 Bloomberg Coding Challenge 26ng 1st Round
--------------------------------Origianl Qeustion Start --------------------------------
You are given a list of stations represented as a string separated by hyphens ('-'),
and a dictionary bus_list that maps each bus_id to its current station.
The buses only move from left to right along the stations (e.g., A → B → C → …).
You need to implement a system with the following methods:


def __init__(self, bus_list: dict[int, str], stations: str):
    # constructor: initialize buses and stations

def closest_bus(self, station_id: str) -> int:
    """
    return how far is the closest incoming bus to station_id (to its left).
    """

def find_location_bus(self, bus_id: int) -> str:
    """
    Return the station name where the given bus_id is currently located.
    """

def move(self) -> None:
    """
    Move all buses one station to the right.
    If a bus is already at the last station, it will remain there.
    """
stations = "A-B-C-D-E-F-G"
bus_list = {1: "B", 3: "F"}
closest_bus(A) = -1 no bus on left
closest_bus(B) = 0
closest_bus(C) = 1
closest_bus(D) = 2
closest_bus(E) = 3
closest_bus(F) = 0
--------------------------------Origianl Qeustion End --------------------------------


--------------------------------Follow Up --------------------------------
follow-up: all operations in O(1)
--------------------------------Follow Up --------------------------------

Question:
You are given a list of stations represented as a string separated by hyphens (-), and a dictionary bus_list that maps each bus_id to its current station.
The buses only move from left to right along the stations (e.g., A → B → C …).
'''
class Bus:
    def __init__(self, bus_list: dict[int, str], stations: str):
        # constructor: initialize buses and stations
        # station name list [A, B]
        self.stations = list(stations.split('-'))
        # total length of all stations
        self.length = len(self.stations)
        # [A:0, B:1, ...]
        self.station_index_map = {name:i for i, name in enumerate(self.stations)}
        #   [0, 1, 0, 0, 0, 3, 0]
        self.bus_map = [0] * len(self.stations)
        # {1: "B", 3: "F"}
        self.bus_list = bus_list
        self.rightmost_index = -1
        for bus_id, station in bus_list.items():
            #   [0, 1, 0, 0, 0, 3, 0]
            # s                 e
            station_index = self.station_index_map[station]
            self.bus_map[station_index] = bus_id
            self.rightmost_index = max(station_index, self.rightmost_index)

        self.time = 0
        last_bus_index = -1
        self.closest_list = [-1] * self.length

        # original closest bus map
        for i in range(self.length):
            if self.bus_map[i] != 0:
                last_bus_index = i
            if last_bus_index != -1:
                self.closest_list[i] = i - last_bus_index

    # O n -> O m -> O 1
    def closest_bus(self, station_id: str) -> int:
        """
        return how far is the closest bus to station_id.
        """

        station_index = self.station_index_map[station_id]
        lookup_id = station_index - self.time
        # edge cases
        # no bus at all
        if self.rightmost_index == -1:
            return -1
        # last station
        if station_index == self.length - 1:
            # calculate by right most bus
            right_most = min(self.length - 1, self.rightmost_index + self.time)
            return self.length - 1 - right_most
        # no bus to its left
        if lookup_id < 0:
            return -1
        return self.closest_list[lookup_id]


    # O 1
    def find_location_bus(self, bus_id: int) -> str:
        """
        Return the station name where the given bus_id is currently located.
        """
        origin = self.station_index_map[self.bus_list[bus_id]]
        cur = origin + self.time
        # bus stop at final station
        station_index = min(self.length - 1, cur)
        station_name = self.stations[station_index]

        return station_name
    # O 1
    def move(self) -> None:
        """
        Move all buses one station to the right.
        If a bus is already at the last station, it will remain there.
        """
        self.time += 1

# ---------------- Unit Test in main ----------------
def run_test(description, actual, expected):
    result = "PASS" if actual == expected else "FAIL"
    print(f"{description}: Expected={expected}, Actual={actual} --> {result}")

if __name__ == "__main__":
    stations_str = "A-B-C-D-E-F-G"

    # ---------------- Case 1: Original example ----------------
    print("=== Case 1: Bus 1 at B, Bus 3 at F ===")
    bus_system = Bus({1: "B", 3: "F"}, stations_str)
    # Closest bus queries
    run_test("Closest bus to A", bus_system.closest_bus("A"), -1)  # no bus to the left
    run_test("Closest bus to B", bus_system.closest_bus("B"), 0)   # bus at B
    run_test("Closest bus to C", bus_system.closest_bus("C"), 1)   # bus at B
    run_test("Closest bus to D", bus_system.closest_bus("D"), 2)   # bus at B
    run_test("Closest bus to E", bus_system.closest_bus("E"), 3)   # bus at B
    run_test("Closest bus to F", bus_system.closest_bus("F"), 0)   # bus at F
    # Location queries
    run_test("Location of bus 1", bus_system.find_location_bus(1), "B")
    run_test("Location of bus 3", bus_system.find_location_bus(3), "F")
    # Move buses twice
    bus_system.move(); bus_system.move()
    run_test("After 2 moves, bus 1", bus_system.find_location_bus(1), "D")
    run_test("After 2 moves, bus 3", bus_system.find_location_bus(3), "G")
    run_test("After 2 moves, closest bus to F", bus_system.closest_bus("F"), 2)

    # ---------------- Case 2: Bus at the first station ----------------
    print("\n=== Case 2: Single bus starting at A ===")
    bus_system = Bus({10: "A"}, stations_str)
    run_test("Closest bus to A", bus_system.closest_bus("A"), 0)   # bus at A
    run_test("Closest bus to B", bus_system.closest_bus("B"), 1)   # bus at A
    run_test("Closest bus to C", bus_system.closest_bus("C"), 2)   # bus at A
    run_test("Location of bus 10", bus_system.find_location_bus(10), "A")
    bus_system.move()
    run_test("After 1 move, bus 10", bus_system.find_location_bus(10), "B")

    # ---------------- Case 3: Bus at the last station ----------------
    print("\n=== Case 3: Single bus starting at G ===")
    bus_system = Bus({20: "G"}, stations_str)
    run_test("Closest bus to F", bus_system.closest_bus("F"), -1)  # bus is not to the left
    run_test("Closest bus to G", bus_system.closest_bus("G"), 0)   # bus at G
    run_test("Location of bus 20", bus_system.find_location_bus(20), "G")
    bus_system.move()
    run_test("After move, bus 20 still at G", bus_system.find_location_bus(20), "G")

    # ---------------- Case 4: Multiple buses at different positions ----------------
    print("\n=== Case 4: Multiple buses at A, C, E ===")
    bus_system = Bus({1: "A", 2: "C", 3: "E"}, stations_str)
    run_test("Closest bus to B", bus_system.closest_bus("B"), 1)   # bus at A
    run_test("Closest bus to C", bus_system.closest_bus("C"), 0)   # bus at C
    run_test("Closest bus to D", bus_system.closest_bus("D"), 1)   # bus at C
    run_test("Closest bus to E", bus_system.closest_bus("E"), 0)   # bus at E
    run_test("Closest bus to F", bus_system.closest_bus("F"), 1)   # bus at E
    bus_system.move()
    run_test("After 1 move, bus 1", bus_system.find_location_bus(1), "B")
    run_test("After 1 move, bus 2", bus_system.find_location_bus(2), "D")
    run_test("After 1 move, bus 3", bus_system.find_location_bus(3), "F")
    run_test("After 1 move, closest bus to G", bus_system.closest_bus("G"), 1)  # bus at F

    # ---------------- Case 5: No buses at all ----------------
    print("\n=== Case 5: No buses in the system ===")
    bus_system = Bus({}, stations_str)
    run_test("Closest bus to A", bus_system.closest_bus("A"), -1)  # no buses
    run_test("Closest bus to G", bus_system.closest_bus("G"), -1)  # no buses

    # ---------------- Case 6: Multiple buses at the same station ----------------
    print("\n=== Case 6: Two buses starting at the same station C ===")
    bus_system = Bus({1: "C", 2: "C"}, stations_str)
    run_test("Closest bus to C", bus_system.closest_bus("C"), 0)   # buses at C
    run_test("Closest bus to D", bus_system.closest_bus("D"), 1)   # buses at C
    run_test("Location of bus 1", bus_system.find_location_bus(1), "C")
    run_test("Location of bus 2", bus_system.find_location_bus(2), "C")
    bus_system.move()
    run_test("After 1 move, bus 1", bus_system.find_location_bus(1), "D")
    run_test("After 1 move, bus 2", bus_system.find_location_bus(2), "D")

    # ---------------- Case 7: Large number of moves ----------------
    print("\n=== Case 7: Bus moves beyond the last station ===")
    bus_system = Bus({99: "E"}, stations_str)
    for _ in range(10):  # move more times than stations length
        bus_system.move()
    run_test("Bus 99 should remain at G", bus_system.find_location_bus(99), "G")
    run_test("Closest bus to G after many moves", bus_system.closest_bus("G"), 0)
