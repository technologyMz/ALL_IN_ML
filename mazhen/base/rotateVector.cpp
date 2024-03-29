#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    void reverse(vector<int>& nums, int start, int end) {
        while (start < end) {
            swap(nums[start], nums[end]);
            start += 1;
            end -= 1;
        }
    }
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        reverse(nums, 0, nums.size() - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.size() - 1);
    }
};


int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> nums =  {1,2,3,4,5,6,7};
    s.rotate(nums, 3);
    for(int i=0; i< nums.size(); i++){
        cout << nums[i] << endl;
    }
    return 0;
}
