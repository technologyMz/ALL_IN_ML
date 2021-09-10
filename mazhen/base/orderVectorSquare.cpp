#include<iostream>
#include<vector>
#include <math.h>

using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> re(nums.size());
        int left=0; int right=nums.size()-1; int pos=nums.size()-1;
        while(left<= right){
            if(nums[left]*nums[left] <= nums[right] * nums[right]){
                re[pos] = nums[right] * nums[right];
                right --;
            }
            else {
                re[pos] = nums[left]*nums[left];
                left ++;
            }
            pos --;
        }
        return re;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> nums =  {-1,0,3,5,9,12};
    vector<int> ord = s.sortedSquares(nums);
    for(int i=0; i< ord.size(); i++){
        cout << ord[i] << endl;
    }
    return 0;
}
