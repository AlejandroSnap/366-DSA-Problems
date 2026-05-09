#include <iostream>
#include <vector>

using namespace std;

vector<int> getConcatenation(vector<int>& nums) {
    vector<int> ans = nums;
    for(int num: nums) {
        ans.push_back(num);
    }

    return ans;
}

int main() {
    vector<int> nums = {1,2,1};
    for(int num: getConcatenation(nums)) {
        cout << num << " ";
    }

    cout << endl;

    return 0;
}