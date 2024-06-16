#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node into a singly linked list
 * @head: Pointer to a pointer to the head of a list
 * @number: number to be inserted
 *
 * Return: Address of the new node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *previous = NULL;
	listint_t *current = NULL;

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	previous->next = new_node;
	new_node->next = current;

	return (new_node);
}
