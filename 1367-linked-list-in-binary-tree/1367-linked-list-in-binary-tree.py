class Solution:
    def isSubPath(
        self, head: Optional[ListNode], root: Optional[TreeNode]
    ) -> bool:
        if not root:
            return False
        return (
            self._dfs(root, head)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
        )

    def _dfs(self, node: Optional[TreeNode], head: Optional[ListNode]) -> bool:
        if not head:
            return True  
        if not node:
            return False  
        if node.val != head.val:
            return False  
        return self._dfs(node.left, head.next) or self._dfs(
            node.right, head.next
        )