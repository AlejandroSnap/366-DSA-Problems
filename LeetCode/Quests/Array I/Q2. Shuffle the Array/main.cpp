#include <iostream>
#include <vector>

using namespace std;

vector<int> shuffle(vector<int>& nums, int n) {
    vector<int> ans;
    int i;
    for(i = 0; i < n; i++) {
        ans.push_back(nums[i]);
        ans.push_back(nums[i + n]);
    }

    return ans;
}

int main() {
    
    return 0;
}