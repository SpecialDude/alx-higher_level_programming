#include "lists.h"

/**
 * reverse_linked_list - Reverse a linked list
 *
 * @head: List head
 *
 * Return: listint_t*
 */
listint_t *reverse_linked_list(listint_t *head)
{
	listint_t *prev = NULL, *cur = head, *tmp;

	while (cur)
	{
		tmp = cur->next;
		cur->next = prev;
		prev = cur;
		cur = tmp;
	}

	return (prev);
}

/**
 * duplicate_list - Duplicate a linked list
 *
 * @head: Head of the list
 *
 * Return: listint_t*
 */
listint_t *duplicate_list(listint_t *head)
{
	listint_t *dub, *current, *new, *prev;

	if (!head)
		return (NULL);

	dub = malloc(sizeof(listint_t));

	if (dub == NULL)
		return (NULL);

	dub->n = head->n;
	dub->next = NULL;

	current = head->next;
	prev = dub;

	while (current)
	{
		new = malloc(sizeof(listint_t));
		if (dub == NULL)
			return (NULL);

		new->n = current->n;

		prev->next = new;

		prev = new;

		current = current->next;

	}
	prev->next = NULL;

	return (dub);
}

/**
 * is_palindrome - Check if a linked list is palindrome
 *
 * @head: List head
 *
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy, *current, *cpycur;

	if (!(*head))
		return (1);

	copy = duplicate_list(*head);
	copy = reverse_linked_list(copy);

	current = *head;
	cpycur = copy;
	while (current)
	{
		if (current->n != cpycur->n)
		{
			free_listint(copy);
			return (0);
		}
		cpycur = cpycur->next;
		current = current->next;
	}

	free_listint(copy);
	return (1);
}
