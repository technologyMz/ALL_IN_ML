#include<iostream>
#include<vector>
#include <math.h>
using namespace std;

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int left=0; int right=nums.size();
        while(left >=0 and left <= right){
            int mid = floor((left + right) / 2);
            if(nums[mid] == target){
                return mid;
            }
            else if (nums[mid] < target)
            {
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
    
        return 0;
    }
};


int main(int argc, char const *argv[])
{   
    Solution s;
    vector<int> nums =  {-1,0,3,5,9,12};
    int idx = s.search(nums, 9);
    cout << "idx: " << idx << endl;
    return 0;
}

