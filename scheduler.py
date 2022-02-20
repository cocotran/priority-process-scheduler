from tkinter.messagebox import NO
from xxlimited import new
from process import Process

class Scheduler:
    def __init__(self) -> None:
        self.active_queue = []
        self.expired_queue = []

    def get_time_slot(self, priority: int) -> int:
        """Returns the time slot in millisecond 
        """
        return (140 - priority) * (20 if priority < 100 else 5)

    def get_updated_priority() -> int:
        pass

    def accept_new_process(self, new_process: Process) -> None:
        # Get the index
        low = 0
        high = len(self.expired_queue)
        while (low < high):
            mid: int = (low + high) >> 1
            if self.expired_queue[mid].priority < new_process.priority:
                low = mid + 1
            else:
                high = mid
        self.expired_queue.insert(low, new_process)

    def switch_flag(self) -> None:
        if len(self.active_queue) > 0:
            return
        self.active_queue = self.expired_queue
        self.expired_queue = []

    def execute():
        pass