/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr) {
            return false;
        }

        set<ListNode*> traversed_nodes;
        traversed_nodes.insert(head);

        while( head->next != nullptr) {
            if (traversed_nodes.count(head->next) != 0) {
                return true;
            }

            traversed_nodes.insert(head);
            head = head->next;
        }

        return false;
        
    }
};