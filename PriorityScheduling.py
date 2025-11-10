# --------- Priority Scheduling (Non-Preemptive) ---------

class Process:
    def __init__(self, pid, at, bt, priority):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.priority = priority
        self.wt = 0
        self.tat = 0
        self.ct = 0
        self.finished = False

def priority_scheduling(processes):
    time = 0
    completed = 0
    n = len(processes)

    if n > 0:
        time = min(p.at for p in processes)

    while completed < n:
        ready_queue = [p for p in processes if p.at <= time and not p.finished]

        if ready_queue:
            ready_queue.sort(key=lambda x: (-x.priority, x.at, x.pid))
            current = ready_queue[0]

            time += current.bt
            current.ct = time
            current.tat = current.ct - current.at
            current.wt = current.tat - current.bt
            current.finished = True
            completed += 1
        else:
            future_arrivals = [p.at for p in processes if not p.finished]
            if future_arrivals:
                time = min(future_arrivals)
            else:
                break

n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter Arrival Time for process {i+1}: "))
    bt = int(input(f"Enter Burst Time for process {i+1}: "))
    pr = int(input(f"Enter Priority for process {i+1}: "))
    processes.append(Process(i+1, at, bt, pr))

priority_scheduling(processes)

print("\nProcess\tAT\tBT\tPriority\tCT\tTAT\tWT")
total_wt = total_tat = 0

for p in sorted(processes, key=lambda x: x.pid):
    total_wt += p.wt
    total_tat += p.tat
    print(f"P{p.pid}\t{p.at}\t{p.bt}\t{p.priority}\t\t{p.ct}\t{p.tat}\t{p.wt}")

print(f"\nAverage Waiting Time = {total_wt/n:.2f}")
print(f"Average Turnaround Time = {total_tat/n:.2f}")
