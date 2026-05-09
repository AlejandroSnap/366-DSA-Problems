#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> findDisappearedNumbers(vector<int>& nums) {
    vector<int> ans, aux(nums.size(), 0);
    int i;
    bool flag = false;

    for(i = 0; i < nums.size(); i++) {
        if(!aux[nums[i] - 1]) {
            aux[nums[i] - 1] = nums[i];
        }
    }

    for(i = 0; i < aux.size() && !flag; i++) {
        if(!aux[i]) {
            if(i > 0) {
                aux[i] = aux[i - 1] + 1;
                ans.push_back(aux[i]);
            } else {
                aux[i] = 1;
                ans.push_back(aux[i]);
            }
        }
    }

    return ans;
}

int main() {
    vector<int> nums = {3, 3};
    for(int num: findDisappearedNumbers(nums)) {
        cout << num << " ";
    }

    cout << endl;

    return 0;
}