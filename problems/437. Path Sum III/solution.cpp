class Solution {
    int ans = 0;
    unordered_map<long, int> map;
public:
    int pathSum(TreeNode* root, int targetSum) {
        map[0] = 1;
        dfs(root, 0, targetSum);

        return ans;
    }

    void dfs(TreeNode* node, long curSum, int targetSum) {
        if (!node)
            return;

        curSum += node->val;
        
        if (map[curSum - targetSum] > 0) {
            ans += map[curSum - targetSum];
        }

        map[curSum]++;

        dfs(node->left, curSum, targetSum);
        dfs(node->right, curSum, targetSum);

        map[curSum]--;
    }
};
