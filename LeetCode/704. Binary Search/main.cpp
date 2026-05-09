#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int search(vector<int>& nums, int target) {
    int ans = -1;
    int min = 0;
    int max = nums.size() - 1;
    
    while(ans == -1 && min <= max) {
        int mid = min + (max - min) / 2;

        if(nums[mid] < target) {
            min = mid + 1;
        } else if(nums[mid] > target) {
            max = mid - 1;
        } else {
            ans = mid;
        }
    }

    return ans;
}

int main() {
    vector<int> vec = {-1,0,3,5,9,12};
    cout << search(vec, 9); 
    return 0;
}