#include <iostream>
#include <vector>
#include <deque>
#include <iomanip>
using namespace std;

void round_robin(vector<int> at, vector<int> bt, int n, int tq) {
    vector<int> rt = bt, ct(n), tat(n), wt(n);
    deque<int> readyQ;
    vector<string> gantt;
    vector<bool> in_queue(n, false);
    int time = 0, completed = 0;

    while (completed < n) {
        for (int i = 0; i < n; ++i)
            if (at[i] <= time && rt[i] > 0 && !in_queue[i])
                readyQ.push_back(i), in_queue[i] = true;

        if (readyQ.empty()) {
            gantt.push_back("/////");
            time++;
            continue;
        }

        int idx = readyQ.front();
        readyQ.pop_front();

        int exec = min(tq, rt[idx]);

        for (int t = 0; t < exec; ++t) {
            gantt.push_back("P" + to_string(idx + 1));
            time++;

            for (int i = 0; i < n; ++i)
                if (at[i] <= time && rt[i] > 0 && !in_queue[i])
                    readyQ.push_back(i), in_queue[i] = true;
        }

        rt[idx] -= exec;

        if (rt[idx] == 0)
            ct[idx] = time, completed++;
        else
            readyQ.push_back(idx);
    }

    for (int i = 0; i < n; ++i) {
        tat[i] = ct[i] - at[i];
        wt[i] = tat[i] - bt[i];
    }

    cout << "\nProcess\tAT\tBT\tCT\tTAT\tWT\n";
    for (int i = 0; i < n; ++i)
        cout << "P" << i + 1 << "\t" << at[i] << "\t" << bt[i] << "\t" << ct[i] << "\t" << tat[i] << "\t" << wt[i] << "\n";

    double avgTAT = 0, avgWT = 0;
    for (int i = 0; i < n; ++i) avgTAT += tat[i], avgWT += wt[i];

    cout << fixed << setprecision(2);
    cout << "\nAverage TAT = " << avgTAT / n;
    cout << "\nAverage WT = " << avgWT / n << "\n";

    vector<string> block_procs;
    vector<int> block_ends;
    int start = 0;

    for (int i = 1; i <= (int)gantt.size(); i++) {
        if (i == (int)gantt.size() || gantt[i] != gantt[start]) {
            block_procs.push_back(gantt[start]);
            block_ends.push_back(i);
            start = i;
        }
    }

    cout << "\nGantt Chart:\n ";
    for (auto &p : block_procs) cout << "_______ ";
    cout << "\n|";
    for (auto &p : block_procs) {
        int sp = 7 - (int)p.size();
        cout << string(sp / 2, ' ') << p << string(sp - sp / 2, ' ') << "|";
    }
    cout << "\n ";
    for (auto &p : block_procs) cout << "_______ ";
    cout << "\n0";
    for (auto &e : block_ends) cout << string(7, ' ') << e;
    cout << "\n";
}

int main() {
    int n, tq;
    cout << "Enter number of processes: ";
    cin >> n;

    vector<int> at(n), bt(n);
    for (int i = 0; i < n; ++i) {
        cout << "Process[" << i + 1 << "] Arrival Time: ";
        cin >> at[i];
        cout << "Process[" << i + 1 << "] Burst Time: ";
        cin >> bt[i];
    }

    cout << "\nEnter the time quantum: ";
    cin >> tq;

    round_robin(at, bt, n, tq);
    return 0;
}
