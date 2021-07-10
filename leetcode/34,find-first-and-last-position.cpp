class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> high;
        int n=nums.size()-1;
        for (int i=0;i<=n;i++) {
            if (nums[i]==target) {
                high.push_back(i);
                high.push_back(i);
                break;
            }
        }
         if (high.empty()) {
        high.push_back(-1);
        high.push_back(-1);
    }
        else {
        for(int i=high[0]+1;i<=n;i++) {
            if (nums[i]==target) high[1]++;
        }
        }
    return high;
    }
};