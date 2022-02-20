class Process:
    def __init__(self, pid, arrival_time, burst_time, priority) -> None:
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority