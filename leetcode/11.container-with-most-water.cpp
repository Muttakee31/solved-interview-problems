/*
half solved, took help from discussion
*/
class Solution {
public:
    int maxArea(vector<int>& height) {
        int length=height.size();
        int second_index=length-1, first_index=0,maximum=0;
        while (first_index!=second_index) {
           maximum=max(maximum,min(height[first_index],height[second_index])*abs(first_index-second_index));
           if (height[first_index]<height[second_index]) first_index++;
           else second_index--;
           }
        return maximum;
    }
};
