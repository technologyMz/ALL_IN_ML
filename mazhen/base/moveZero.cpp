#include<iostream>
#include<vector>

using namespace std;

/**
 * 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

    示例:

    输入: [0,1,0,3,12]
    输出: [1,3,12,0,0]
    说明:

    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。

 **/

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int l = 0; int r = 0; int n = nums.size();
        while(r< n){
            if(nums[r]){
                swap(nums[l], nums[r]);
                l++;
            } 
            r++;
        }
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> nums =  {1,9,8,0,4,0,5,6,7,0};
    s.moveZeroes(nums);
    for(int i=0; i< nums.size(); i++){
        cout << nums[i] << endl;
    }
    return 0;
}