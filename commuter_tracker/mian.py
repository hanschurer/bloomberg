from typing import Dict, Tuple, List
import time


# — Title: Design Commuter Cost Tracker for Branches
# Difficulty: Medium
# Prompt: Build a system to track average travel times (costs) between company sites (e.g., “JFK→Manhattan”, “Boston→NYC”) for employees traveling on expense accounts. Implement checkIn(id, siteName, time), checkOut(id, siteName, time), and getAverageTime(startSite, endSite) to return the average duration between two sites across all completed trips.



class CommuterCostTracker:
    def __init__(self):
        # 存储正在进行中的行程: key为员工ID, value为(起始地点, 签到时间)
        self.active_trips: Dict[int, Tuple[str, float]] = {}
        
        # 存储已完成的行程: key为"起点→终点", value为时间列表
        self.completed_trips: Dict[str, List[float]] = {}
    
    def checkIn(self, employee_id: int, site_name: str, checkin_time: float) -> None:
        """
        员工签到方法，记录员工开始行程的地点和时间
        :param employee_id: 员工唯一标识
        :param site_name: 签到地点
        :param checkin_time: 签到时间（建议使用时间戳）
        """
        # 检查员工是否已经在行程中
        if employee_id in self.active_trips:
            raise ValueError(f"员工 {employee_id} 已经在行程中，无法重复签到")
        
        # 记录签到信息
        self.active_trips[employee_id] = (site_name, checkin_time)
    
    def checkOut(self, employee_id: int, site_name: str, checkout_time: float) -> None:
        """
        员工签出方法，记录员工结束行程的地点和时间，并计算行程时间
        :param employee_id: 员工唯一标识
        :param site_name: 签出地点
        :param checkout_time: 签出时间（建议使用时间戳）
        """
        # 检查员工是否有未完成的签到
        if employee_id not in self.active_trips:
            raise ValueError(f"员工 {employee_id} 没有未完成的签到，无法签出")
        
        # 获取签到信息并移除活跃行程
        start_site, start_time = self.active_trips.pop(employee_id)
        
        # 确保签出时间晚于签到时间
        if checkout_time <= start_time:
            raise ValueError("签出时间必须晚于签到时间")
        
        # 计算行程时间
        trip_duration = checkout_time - start_time
        
        # 生成行程键（起点→终点）
        trip_key = f"{start_site}→{site_name}"
        
        # 将行程时间添加到已完成行程记录
        if trip_key not in self.completed_trips:
            self.completed_trips[trip_key] = []
        self.completed_trips[trip_key].append(trip_duration)
    
    def getAverageTime(self, start_site: str, end_site: str) -> float:
        """
        计算从起点到终点的平均旅行时间
        :param start_site: 起点
        :param end_site: 终点
        :return: 平均旅行时间，如果没有记录则返回0.0
        """
        trip_key = f"{start_site}→{end_site}"
        
        # 检查是否有该行程的记录
        if trip_key not in self.completed_trips or len(self.completed_trips[trip_key]) == 0:
            return 0.0
        
        # 计算并返回平均时间
        durations = self.completed_trips[trip_key]
        return sum(durations) / len(durations)


# 示例用法
if __name__ == "__main__":
    tracker = CommuterCostTracker()
    
    # 员工1: JFK→Manhattan
    tracker.checkIn(1, "JFK", 1000.0)  # 签到时间用时间戳表示
    tracker.checkOut(1, "Manhattan", 1060.0)  # 60分钟后签出
    
    # 员工2: JFK→Manhattan
    tracker.checkIn(2, "JFK", 1100.0)
    tracker.checkOut(2, "Manhattan", 1150.0)  # 50分钟后签出
    
    # 员工3: Boston→NYC
    tracker.checkIn(3, "Boston", 1200.0)
    tracker.checkOut(3, "NYC", 1500.0)  # 300分钟后签出
    
    # 查询平均时间
    print(f"JFK到Manhattan的平均时间: {tracker.getAverageTime('JFK', 'Manhattan')}")  # 应该是55.0
    print(f"Boston到NYC的平均时间: {tracker.getAverageTime('Boston', 'NYC')}")      # 应该是300.0
    print(f"NYC到Boston的平均时间: {tracker.getAverageTime('NYC', 'Boston')}")      # 应该是0.0（没有记录）
