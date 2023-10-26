class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int len = nums.size();
        vector<int> res(2, -1); // Initialize with -1 as a placeholder.
        
        for (int i = 0; i < len; i++) {
            for (int j = i + 1; j < len; j++) {
                if (nums[i] + nums[j] == target) {
                    res[0] = i;
                    res[1] = j;
                    return res; // Return the result once found.
                }
            }
        }
        
        // If no such pair is found, return an empty vector.
        return res;
    }
};