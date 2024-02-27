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
    struct ListNode *prev = NULL;
    struct ListNode *itr = head;
    struct ListNode *copyHead = NULL;
    struct ListNode *copyHeadPrev = NULL;
    struct ListNode *copyTail = NULL;
    struct ListNode *copyTailPrev = NULL;
    int index = 1;
    while(itr != NULL)
    {
        if (index < left)
        {
            struct ListNode *temp = (struct ListNode*) malloc(sizeof(struct ListNode));
            temp->val = itr->val;
            temp->next = NULL;
            if (!copyHead)
            {
                copyHead = temp;
            } else
            {
                copyHeadPrev->next = temp;
            }
            copyHeadPrev = temp;
        }
        if (index >= left && index <=right)
        {
            struct ListNode *temp = (struct ListNode*) malloc(sizeof(struct ListNode));
            temp->val = itr->val;
            temp->next = prev;
            prev = temp;
        }
        if (index > right)
        {
            struct ListNode *temp = (struct ListNode*) malloc(sizeof(struct ListNode));
            temp->val = itr->val;
            temp->next = NULL;
            if (!copyTail)
            {
                copyTail = temp;
            } else
            {
                copyTailPrev->next = temp;
            }
            copyTailPrev = temp;
        }
        index++;
        itr = itr->next;
    }
    
    itr = prev;
    while(itr->next != NULL)
    {
        itr = itr->next;
    }
    itr->next = copyTail;

    if (copyHeadPrev)
    {
        copyHeadPrev->next = prev;
        return copyHead;
    } else
    {
        return prev;
    }
}

int main()
{
    // int arr[] = {1,2,3,4,5};
    // int left = 2;
    // int right = 4;
    // int arr[] = {5};
    // int left = 1;
    // int right = 1;
    int arr[] = {3,5};
    int left = 1;
    int right = 1;
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