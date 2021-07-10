class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int steps[10009];
        cost.push_back(0);
        int n=cost.size();
        steps[0]=0;
        steps[1]=cost[0];
        for (int i=2;i<=n;i++) {
            steps[i]=min(steps[i-1]+cost[i-1],steps[i-2]+cost[i-1]);
        }
        return steps[n];
    }
};