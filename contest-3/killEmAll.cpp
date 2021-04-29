#include<bits/stdc++.h>
#include<iostream>

using namespace std;

int main() {
    int q, n, m, r;
    cin >> q;

    while(q--) {
        cin >> n;
        cin >> r;

        set<int, greater<int>> s;

        for (int i = 0; i < n; i++) {
            cin >> m;
            s.insert(m);
        }

        long long int mult, shots = 0;
        auto itr = s.begin();

        while(itr != s.end()) {
            mult = shots * r;
            if(*itr - mult <= 0)
                itr++;
            else
                shots++, itr++;
        }

        cout << shots << '\n';
    }
    return 0;
}
