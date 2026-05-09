#include <iostream>
#include <vector>

using namespace std;

vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
    vector<int> ans(nums.size(), 0);
    int i, j;
    int count;

    for(i = 0; i < nums.size(); i++) {
        count = 0;
        for(j = 0; j < nums.size(); j++) {
            if(nums[j] < nums[i]) {
                count++;
            }
        }

        ans[i] = count;
    }

    return ans;
}

int main() {
    vector<int> nums = {8,1,2,2,3};
    for(int num: smallerNumbersThanCurrent(nums)) {
        cout << num << " ";
    }

    cout << endl;
    return 0;
}