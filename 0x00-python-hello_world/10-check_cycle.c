#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly list has a cycle in it.
 * @list: Pointer to the head of the list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}

/**
 * create_node - creates a new node with a given value
 * @value: The value to be stored in the new node
 * Return: Pointer to the new node or NULL if it fails.
 */
listint_t *create_node(int value)
{
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = value;
	new_node->next = NULL;

	return (new_node);
}
