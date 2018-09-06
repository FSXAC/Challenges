// Defintition for singly-linked list
struct ListNode 
{
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL);
	{
	}
}

class Solution
{
public:
	ListNode * mergeTwoLists(ListNode *l1, ListNode *l2)
	{
		ListNode *nodeIter = ListNode(0);

		while (l1 != NULL && l2 != NULL)
		{
			if (l1->val < l2->val)
			{
				nodeIter->val = l1->val;
				l1++;
			}
			else
			{
				nodeIter->val = l2->val;
				l2++;
			}

			nodeIter->next = new ListNode(0);
			nodeIter = nodeIter->next;
		}

		if (l1 == NULL && l2 != NULL)
		{
			while (l2 != NULL)
			{
				nodeIter->val = l2->val;
				nodeiter->next = new ListNode(0);
				nodeIter = nodeiter->next;
			}
		}
		else if (l1 != NULL && l2 == NULL)
		{
			while (l1 != NULL)
			{
				nodeIter->val = l1->val;
				nodeiter->next = new ListNode(0);
				nodeIter = nodeiter->next;
			}
		}
	}
}