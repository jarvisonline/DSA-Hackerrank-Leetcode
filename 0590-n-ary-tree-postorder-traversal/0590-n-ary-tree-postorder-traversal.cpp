/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> res;

        function<void(Node*)> helper = [&](Node* node) {
            if (!node) return;
            for (Node* c : node->children) {
                helper(c);
            }
            res.push_back(node->val);
        };

        helper(root);
        return res;
    }
};