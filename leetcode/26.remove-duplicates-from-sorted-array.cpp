class Solution {
    // could not solve.
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size()==0) return 0;
        else {
        int i = 0, j=1;
        while(j < nums.size())
        {
            if(nums[i] != nums[j])
            {
                swap(nums[++i], nums[j]);
            }
            j++;
        }
        
        return i+1;
    }
        }
};