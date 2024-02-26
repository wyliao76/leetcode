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

struct ListNode *createNodes(int list[], int size)
{
    struct ListNode *head = NULL;
    struct ListNode *prev = NULL;
    for (int i = 0; i < size; i++)
    {
        struct ListNode *node = (struct ListNode*) malloc(sizeof(struct ListNode));
        node->val = list[i];
        node->next = NULL;
        if (!head)
        {
            head = node;
        } else
        {
            prev->next = node;
        }
        prev = node;
    }
    return head;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *head = NULL;
    struct ListNode *prev = NULL;
    int carry = 0;
    while(l1|| l2)
    {
        int v1 = l1 ? l1->val : 0;
        int v2 = l2 ? l2->val : 0;
        int sum = v1 + v2 + carry;
        carry = sum >= 10 ? 1 : 0;
        struct ListNode *node = (struct ListNode*) malloc(sizeof(struct ListNode));
        node->val = sum % 10;
        node->next = NULL;
        if (head == NULL)
        {
            head = node;
        } else
        {
            prev->next = node;
        }
        prev = node;
        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }
    if (carry)
    {
        struct ListNode *node = (struct ListNode*) malloc(sizeof(struct ListNode));
        node->val = carry;
        node->next = NULL;
        prev->next = node;
    }
    return head;
}

int main(int argc, char **argv)
{
    // int l1[] = {2, 4, 3};
    // int l1[] = {0};
    int l1[] = {9, 9, 9, 9, 9, 9, 9};
    int size = sizeof(l1)/sizeof(l1[0]);

    struct ListNode *head1 = createNodes(l1, size);

    // int l2[] = {5, 6, 4};
    // int l2[] = {0};
    int l2[] = {9, 9, 9, 9};
    size = sizeof(l2)/sizeof(l2[0]);
    struct ListNode *head2 = createNodes(l2, size);

    struct ListNode *head = addTwoNumbers(head1, head2);
    struct ListNode *itr = head;
    while(itr != NULL)
    {
        printf("%d\n", itr->val);
        itr = itr->next;
    }
}