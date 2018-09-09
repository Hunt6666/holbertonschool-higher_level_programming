#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include "lists.h"

/**
 *insert_node - inserts a number into a sorted singly linked list
 *@head: start of linked list
 *@number: the number stored in the node to insert
 *Return: the address of the new node or NULL if fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;
	listint_t *nhead;


	if (head == NULL)
		return (NULL);

	nhead = malloc(sizeof(listint_t));
	if (nhead == NULL)
		return (NULL);
	current = malloc(sizeof(listint_t));
	if (current == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	nhead = *head;
	current = *head;

	while(current->next->n < number || current->next == NULL)
	{
		current = current->next;
		if (nhead->next == NULL)
			break;
		nhead = nhead->next;
	}

	nhead = nhead->next;
	new->n = number;
	new->next = nhead;
	current->next = new;
	return (new);
}
