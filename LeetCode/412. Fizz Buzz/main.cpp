#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> fizzBuzz(int n) {
    vector<string> ans(n + 1);
    int i;
    for(i = 1; i <= n; i++) {
        string result = to_string(i);
        if(i % 3 == 0 && i % 5 == 0) {
            result = "FizzBuzz";
        } else if(i % 3 == 0) {
            result = "Fizz";
        } else if(i % 5 == 0) {
            result = "Buzz";
        }

        ans[i] = result;
    }

    return ans;
}

int main() {
    for(string x : fizzBuzz(3)) {
        cout << x << " ";
    }

    return 0;
}