/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdio.h>
#include <stdlib.h>


struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *createLinkedLists(int *arr, int size)
{
    struct ListNode *head = NULL;
    struct ListNode *prev = NULL;
    for (int i = 0; i < size; i++)
    {
        struct ListNode *temp = (struct ListNode*) malloc(sizeof(struct ListNode));
        // printf("%d\n", arr[i]);
        temp->val = arr[i];
        temp->next = NULL;
        if (!head)
        {
            head = temp;
        } else
        {
            prev->next = temp;
        }
        prev = temp;
    }
    return head;
}

struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *prev = NULL;
    struct ListNode *ptr = head;
    
    while(ptr)
    {
        struct ListNode *next = ptr->next;
        ptr->next = prev;
        prev = ptr;
        ptr = next;
    }
    return prev;
}

int main()
{
    int arr[] = {1,2,3,4,5};
    // int arr[] = {1, 2};
    // int arr[] = {};
    int size = sizeof(arr)/sizeof(arr[0]);
    struct ListNode *l = createLinkedLists(arr, size);
    struct ListNode *reversed;
    reversed = reverseList(l);
    while(reversed != NULL)
    {
        printf("%d\n", reversed->val);
        reversed = reversed->next;
    }
    return 0;
}