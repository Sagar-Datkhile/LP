#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Process {
    int pid;
    int at;      
    int bt;       
    int rt;       
    int ct = 0;  
    int wt = 0;   
    int tat = 0;  
    bool finished = false;
};

void srtf_scheduling(vector<Process>& processes) {
    int n = processes.size();
    int completed = 0;
    int time = 0;
    int prev = -1; 

    while (completed < n) {
       
        int idx = -1;
        int min_rt = 1e9;
        for (int i = 0; i < n; i++) {
            if (processes[i].at <= time && !processes[i].finished && processes[i].rt < min_rt) {
                min_rt = processes[i].rt;
                idx = i;
            }
        }

        if (idx != -1) {
          
            processes[idx].rt--;
            time++;

            
            if (processes[idx].rt == 0) {
                processes[idx].finished = true;
                completed++;
                processes[idx].ct = time;
                processes[idx].tat = processes[idx].ct - processes[idx].at;
                processes[idx].wt = processes[idx].tat - processes[idx].bt;
            }
        } else {
            
            time++;
        }
    }
}

int main() {
    int n;
    cout << "Enter number of processes: ";
    cin >> n;

    vector<Process> processes(n);
    for (int i = 0; i < n; i++) {
        cout << "Enter Arrival Time for Process " << i + 1 << ": ";
        cin >> processes[i].at;
        cout << "Enter Burst Time for Process " << i + 1 << ": ";
        cin >> processes[i].bt;
        processes[i].pid = i + 1;
        processes[i].rt = processes[i].bt; 
    }

    srtf_scheduling(processes);

    cout << "\nProcess\tAT\tBT\tWT\tTAT\tCT\n";
    double total_wt = 0, total_tat = 0;
    for (const auto& p : processes) {
        total_wt += p.wt;
        total_tat += p.tat;
        cout << "P" << p.pid << "\t" << p.at << "\t" << p.bt
             << "\t" << p.wt << "\t" << p.tat << "\t" << p.ct << "\n";
    }

    cout << "\nAverage Waiting Time = " << total_wt / n << "\n";
    cout << "Average Turnaround Time = " << total_tat / n << "\n";

    return 0;
}

