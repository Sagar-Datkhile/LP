# --------- SJF Non-Preemptive ---------

class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at     # Arrival Time
        self.bt = bt     # Burst Time
        self.wt = 0      # Waiting Time
        self.tat = 0     # Turnaround Time
        self.ct = 0      # Completion Time
        self.finished = False

def sjf_scheduling(processes):
    time = 0
    completed = 0
    n = len(processes)

    while completed < n:
        # Ready processes
        ready_queue = [p for p in processes if p.at <= time and not p.finished]

        if ready_queue:
            ready_queue.sort(key=lambda x: (x.bt, x.at))
            current = ready_queue[0]

            time += current.bt
            current.ct = time
            current.tat = current.ct - current.at
            current.wt = current.tat - current.bt
            current.finished = True
            completed += 1
        else:
            time += 1

# Input
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter Arrival Time for Process {i+1}: "))
    bt = int(input(f"Enter Burst Time for Process {i+1}: "))
    processes.append(Process(i+1, at, bt))

# Run scheduling
sjf_scheduling(processes)

# Output Table
print("\nProcess\tAT\tBT\tWT\tTAT\tCT")
total_wt = total_tat = 0

for p in processes:
    total_wt += p.wt
    total_tat += p.tat
    print(f"P{p.pid}\t{p.at}\t{p.bt}\t{p.wt}\t{p.tat}\t{p.ct}")

print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
print(f"Average Turnaround Time = {total_tat / n:.2f}")
