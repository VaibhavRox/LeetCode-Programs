#include <stdio.h>
#include <stdlib.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode* next;
};

// Function to create a new node
struct ListNode* createNode(int val) {
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

// Function to merge two sorted linked lists
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* header = createNode(0); // dummy node
    struct ListNode* temp = header;

    if (list1 == NULL) {
        free(header);
        return list2;
    } else if (list2 == NULL) {
        free(header);
        return list1;
    } else {
        while (list1 != NULL && list2 != NULL) {
            if (list1->val < list2->val) {
                temp->next = list1;
                list1 = list1->next;
            } else {
                temp->next = list2;
                list2 = list2->next;
            }
            temp = temp->next;
        }
        // Leftovers
        if (list1 != NULL) {
            temp->next = list1;
        }
        if (list2 != NULL) {
            temp->next = list2;
        }
        struct ListNode* merged = header->next;
        free(header); // free dummy node
        return merged;
    }
}
