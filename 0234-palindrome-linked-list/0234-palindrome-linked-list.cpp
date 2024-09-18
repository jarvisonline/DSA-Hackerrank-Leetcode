class Solution {
public:
    // Function to reverse the linked list
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* curr = head;
        ListNode* temp = NULL;
        while (curr != NULL) {
            temp = curr->next; 
            curr->next = prev; 
            prev = curr;       
            curr = temp;
        }
        return prev;
    }

    
    bool compare(ListNode* l1, ListNode* l2) {
        while (l1 != NULL && l2 != NULL) {
            if (l1->val != l2->val) return false; 
            l1 = l1->next;
            l2 = l2->next;
        }
        return true; 
    }

    
    bool isPalindrome(ListNode* head) {
        if (head == NULL) return true; 


        ListNode* reversedHead = reverseList(head);

    
        return compare(head, reversedHead);
    }
};
