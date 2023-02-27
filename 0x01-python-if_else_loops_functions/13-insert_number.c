#include "lists.h"
#include <stdio.h>
/**
 * insert_node - Inserts a new node into a singly linked list
 *
 * @head: Head of the list
 * @number: Number to Insert
 *
 * Return: inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *current, *prev;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;

	if ((*head) == NULL)
		*head = newnode;
	else
	{
		current = *head;
		prev = NULL;

		while (current != NULL)
		{
			if (current->n > number)
				break;
			prev = current;
			current = current->next;
		}
		if (prev == NULL)
			*head = newnode;
		else
			prev->next = newnode;
		newnode->next = current;
	}
	return (newnode);
}
