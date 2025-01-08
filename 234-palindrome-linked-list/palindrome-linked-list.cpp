/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        stack<int> container;
        ListNode* temp;

        temp = head;

        while (temp != nullptr) {
            container.push(temp->val);
            temp = temp->next;
        }
    
        
        while (head != nullptr) {
            if (head->val != container.top()){
                return false;
            }

            container.pop();
            head = head->next;
        }
        return true;
    }
};