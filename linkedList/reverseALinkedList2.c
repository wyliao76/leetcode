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

struct ListNode* reverseList(struct ListNode* head, int left, int right) {
    struct ListNode dummy;
    struct ListNode *prev;
    struct ListNode *curr;

    dummy.next = head;
    dummy.val = 0;

    prev = &dummy;

    for (int i = 0; i < left - 1; i++)
    {
        prev = prev->next;
    }

    curr = prev->next;

    for(int i = 0; i < right - left; i++)
    {
        struct ListNode *next = curr->next;
        curr->next = next->next;
        next->next = prev->next;
        prev->next = next;
    }

    return dummy.next;
}

int main()
{
    int arr[] = {1,2,3,4,5};
    int left = 2;
    int right = 4;
    // int arr[] = {5};
    // int left = 1;
    // int right = 1;
    // int arr[] = {3,5};
    // int left = 1;
    // int right = 1;
    int size = sizeof(arr)/sizeof(arr[0]);
    struct ListNode *l = createLinkedLists(arr, size);
    struct ListNode *reversed;
    reversed = reverseList(l, left, right);
    while(reversed != NULL)
    {
        printf("%d\n", reversed->val);
        reversed = reversed->next;
    }
    return 0;
}