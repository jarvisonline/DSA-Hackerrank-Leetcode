class Solution {
public:
    void levelSumHelper(TreeNode* node, int level, vector<long long>& levelSums) {
        if (!node) return;
        
        if (level >= levelSums.size()) {
            levelSums.push_back(0);
        }
        
        levelSums[level] += node->val;
        
        levelSumHelper(node->left, level + 1, levelSums);
        levelSumHelper(node->right, level + 1, levelSums);
    }
    
    long long kthLargestLevelSum(TreeNode* root, int k) {
        vector<long long> levelSums;
        
        levelSumHelper(root, 0, levelSums);
        
        sort(levelSums.begin(), levelSums.end(), greater<long long>());
        
        if (k > levelSums.size()) {
            return -1;
        }
        
        return levelSums[k - 1];
    }
};
