class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummyNode;
        ListNode* head;
        dummyNode = head = new ListNode(-1);

        if (!l1) return l2;
        if (!l2) return l1;

        int carry = 0;

        while (l1 || l2) {
            int firstVal = 0, secondVal = 0;

            if (l1) {
                firstVal = l1->val;
                l1 = l1->next;
            }
            if (l2) {
                secondVal = l2->val;
                l2 = l2->next;
            }

            int total = firstVal + secondVal + carry;
            carry = total / 10;
            total = total % 10;

            ListNode* newNode = new ListNode(total);
            dummyNode->next = newNode;
            dummyNode = dummyNode->next;
        }

        if (carry) {
            dummyNode->next = new ListNode(1);
        }

        return head->next;
    }
};
