#include <iostream>
#include <vector>

using namespace std;

int findMaxConsecutiveOnes(vector<int>& nums) {
    int ans = 0, aux = 0, i;
    bool flag = false;
    for(i = 0; i < nums.size(); i++) {
        if(nums[i] == 1) {
            aux++;
        } else {
            ans = max(ans, aux);
            aux = 0;
        }
    }

    ans = max(ans, aux);
    return ans;
}   

int main() {
    vector<int> nums = {1,1,0,1,1,1};
    cout << findMaxConsecutiveOnes(nums) << endl;

    return 0;
}