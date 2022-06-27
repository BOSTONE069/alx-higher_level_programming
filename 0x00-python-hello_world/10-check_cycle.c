#include "lists.h"

/**
 * check_cycle - function that finds a loop in a linked list
 * based on Floyd’s cycle-finding algorithm
 * @list: pointer to the struct listint_t
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast != NULL)
	{
		slow = slow->next;
		if (fast->next == NULL)
			break;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
