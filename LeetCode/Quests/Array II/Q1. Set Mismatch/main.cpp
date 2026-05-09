#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> findErrorNums(vector<int>& nums) {
    vector<int> ans(2, 1), aux(nums.size(), 0);
    int i;
    bool flag = false;

    for(i = 0; i < nums.size(); i++) {
        if(!aux[nums[i] - 1]) {
            aux[nums[i] - 1] = nums[i];
        } else {
            ans[0] = nums[i];
        }
    }

    for(i = 0; i < aux.size() && !flag; i++) {
        if(!aux[i]) {
            if(i > 0) {
                ans[1] = aux[i - 1] + 1;
                flag = true;
            }
        }
    }

    return ans;
}

int main() {
    vector<int> nums = {2, 2};
    for(int num: findErrorNums(nums)) {
        cout << num << " ";
    }
    
    cout << endl;

    return 0;
}