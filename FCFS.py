# Problem Statement : Write a program to simulate CPU Scheduling Algorithms :
# FCFS, SJF (Preemptive), Priority (Non-Preemptive) and Round Robin (Preemptive).

# --------- FCFS ---------
# Input number of processes
n = int(input("Enter number of processes: "))

# Lists to store arrival times, burst times, completion times, waiting times, turnaround times
arrival_time = []
burst_time = []
completion_time = [0] * n
waiting_time = [0] * n
tat = [0] * n

# Taking arrival and burst times as input
print("\nEnter Arrival Time and Burst Time for each process:")
for i in range(n):
    at = int(input(f"Process[{i+1}] Arrival Time: "))
    bt = int(input(f"Process[{i+1}] Burst Time: "))
    arrival_time.append(at)
    burst_time.append(bt)

# Calculate completion times in FCFS order
current_time = 0
for i in range(n):
    if current_time < arrival_time[i]:
        current_time = arrival_time[i]  # CPU idle until process arrives
    current_time += burst_time[i]
    completion_time[i] = current_time

# Calculate TAT and WT
for i in range(n):
    tat[i] = completion_time[i] - arrival_time[i]
    waiting_time[i] = tat[i] - burst_time[i]

# Calculate averages
avg_wait = sum(waiting_time) / n
avg_tat = sum(tat) / n

# Display table
print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"P{i+1}\t\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{tat[i]}")

print(f"\nAverage Waiting Time: {avg_wait:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}\n")


'''
Output: 
Enter number of processes: 4

Enter Arrival Time and Burst Time for each process:
Process[1] Arrival Time: 0
Process[1] Burst Time: 3
Process[2] Arrival Time: 1
Process[2] Burst Time: 4
Process[3] Arrival Time: 2
Process[3] Burst Time: 2
Process[4] Arrival Time: 3
Process[4] Burst Time: 1

Process	Arrival Time	Burst Time	Waiting Time	Turnaround Time
P1	0		3		0		3
P2	1		4		2		6
P3	2		2		5		7
P4	3		1		6		7

Average Waiting Time: 3.25
Average Turnaround Time: 5.75


'''