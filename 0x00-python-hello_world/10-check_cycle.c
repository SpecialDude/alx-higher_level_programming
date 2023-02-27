#include "lists.h"
/**
 * check_cycle - Check if a cycle exists within a linked list
 *
 * @list: The linked list
 *
 * Return: 1 if cycle exists 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_p, *slow_p;

	fast_p = list;
	slow_p = list;

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;

		if (slow_p == fast_p)
			return (1);
	}
	return (0);
}
