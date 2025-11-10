#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "Enter number of processes: ";
    cin >> n;

    vector<int> arrival_time(n);
    vector<int> burst_time(n);
    vector<int> completion_time(n, 0);
    vector<int> waiting_time(n, 0);
    vector<int> tat(n, 0);

    cout << "\nEnter Arrival Time and Burst Time for each process:\n";
    for (int i = 0; i < n; i++) {
        cout << "Process[" << i + 1 << "] Arrival Time: ";
        cin >> arrival_time[i];
        cout << "Process[" << i + 1 << "] Burst Time: ";
        cin >> burst_time[i];
    }

    int current_time = 0;
    for (int i = 0; i < n; i++) {
        if (current_time < arrival_time[i]) {
            current_time = arrival_time[i];
        }
        current_time += burst_time[i];
        completion_time[i] = current_time;
    }

    for (int i = 0; i < n; i++) {
        tat[i] = completion_time[i] - arrival_time[i];
        waiting_time[i] = tat[i] - burst_time[i];
    }

    double avg_wait = 0, avg_tat = 0;
    for (int i = 0; i < n; i++) {
        avg_wait += waiting_time[i];
        avg_tat += tat[i];
    }
    avg_wait /= n;
    avg_tat /= n;

    cout << "\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n";
    for (int i = 0; i < n; i++) {
        cout << "P" << i + 1 << "\t" << arrival_time[i] << "\t\t" << burst_time[i]
             << "\t\t" << waiting_time[i] << "\t\t" << tat[i] << "\n";
    }

    cout << "\nAverage Waiting Time: " << avg_wait << "\n";
    cout << "Average Turnaround Time: " << avg_tat << "\n";

    return 0;
}
