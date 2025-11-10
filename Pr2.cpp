// Problem Statement : Design suitable data structures and implement Pass-I and Pass-II 
// of a two-pass macro-processor. The output of Pass-I (MNT, MDT and intermediate code 
// file without any macro definitions) should be input for Pass-II.

#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <string>
using namespace std;

/*
 Data Structures:
 - MNT (Macro Name Table): macro_name -> index in MDT
 - MDT (Macro Definition Table): vector of strings
 - Intermediate code: program without macro definitions
*/

struct MNTEntry { 
    int mdtIndex; 
    vector<string> params; 
};

map<string, MNTEntry> MNT;
vector<string> MDT;
vector<string> intermediate;

// -------- PASS I --------
void pass1(vector<string> &source) {
    for (size_t i = 0; i < source.size(); i++) {
        string line = source[i];

        if (line == "MACRO") {
            // Header line next
            i++;
            string header = source[i];
            stringstream ss(header);
            string macroName;
            ss >> macroName;

            vector<string> params;
            string token;

            while (ss >> token) {
                if (token[0] == '&')
                    token = token.substr(1); // remove '&'
                params.push_back(token);
            }

            MNTEntry entry;
            entry.mdtIndex = MDT.size();
            entry.params = params;
            MNT[macroName] = entry;

            // Body until MEND
            i++;
            while (i < source.size() && source[i] != "MEND") {
                string body = source[i];

                // Replace params with placeholders #0,#1...
                for (size_t p = 0; p < params.size(); p++) {
                    size_t pos = body.find("&" + params[p]);
                    if (pos != string::npos) {
                        body.replace(pos, params[p].size() + 1, "#" + to_string(p));
                    }
                }

                MDT.push_back(body);
                i++;
            }

            MDT.push_back("MEND");
        } 
        else {
            intermediate.push_back(line);
        }
    }
}

// -------- MACRO EXPANSION --------
vector<string> expand(string name, vector<string> args) {
    vector<string> result;

    if (MNT.find(name) == MNT.end())
        return result;

    MNTEntry entry = MNT[name];

    for (int i = entry.mdtIndex; i < (int)MDT.size(); i++) {
        string line = MDT[i];
        if (line == "MEND")
            break;

        // Replace #0,#1.. with actual arguments
        for (size_t a = 0; a < args.size(); a++) {
            string ph = "#" + to_string(a);
            size_t pos;
            while ((pos = line.find(ph)) != string::npos) {
                line.replace(pos, ph.size(), args[a]);
            }
        }

        result.push_back(line);
    }

    return result;
}

// -------- PASS II --------
vector<string> pass2() {
    vector<string> output;

    for (string line : intermediate) {
        stringstream ss(line);
        string word;
        ss >> word;

        if (MNT.find(word) != MNT.end()) {
            // Macro call
            vector<string> args;
            string arg;

            while (ss >> arg)
                args.push_back(arg);

            vector<string> expanded = expand(word, args);
            output.insert(output.end(), expanded.begin(), expanded.end());
        } 
        else {
            output.push_back(line);
        }
    }

    return output;
}

// -------- MAIN --------
int main() {
    // Example source program
    vector<string> source = {
        "MACRO",
        "INCR &ARG",
        "LOAD &ARG",
        "ADD =1",
        "MEND",
        "START",
        "INCR X",
        "MOV A,B",
        "INCR Y",
        "END"
    };

    pass1(source);

    cout << "\n=== PASS I OUTPUT ===\n";
    cout << "MNT:\n";
    for (auto &it : MNT) {
        cout << "Macro: " << it.first 
             << " MDT Index: " << it.second.mdtIndex 
             << " Params:";
        for (auto &p : it.second.params)
            cout << " " << p;
        cout << "\n";
    }

    cout << "\nMDT:\n";
    for (size_t i = 0; i < MDT.size(); i++)
        cout << i << ": " << MDT[i] << "\n";

    cout << "\nIntermediate Code:\n";
    for (auto &l : intermediate)
        cout << l << "\n";

    vector<string> finalCode = pass2();

    cout << "\n=== PASS II OUTPUT (Expanded Code) ===\n";
    for (auto &l : finalCode)
        cout << l << "\n";

    return 0;
}
