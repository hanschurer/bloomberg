# https://leetcode.com/problems/design-underground-system/description/

# — Title: Design Commuter Cost Tracker for Branches
# Difficulty: Medium
# Prompt: Build a system to track average travel times (costs) between company sites (e.g., “JFK→Manhattan”, “Boston→NYC”) for employees traveling on expense accounts. Implement checkIn(id, siteName, time), checkOut(id, siteName, time), and getAverageTime(startSite, endSite) to return the average duration between two sites across all completed trips.


class UndergroundSystem:

    def __init__(self):
        self.check_in_data = {}
        self.journey_data = collections.defaultdict(lambda : [0, 0])
                
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = [stationName, t]

    def checkOut(self, id: int, end_station: str, t: int) -> None:
        # Access and remove the data for id. Note that removing it is actually
        # optional, but we'll discuss the benefits of it in the space complexity
        # analysis section.
        start_station, start_time = self.check_in_data.pop(id)
        
        self.journey_data[(start_station, end_station)][0] += (t - start_time)
        self.journey_data[(start_station, end_station)][1] += 1
            
    def getAverageTime(self, start_station: str, end_station: str) -> float:
        total_time, total_trips = self.journey_data[(start_station, end_station)]
        # The average is simply the total divided by the number of trips.
        return total_time / total_trips