#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 *is_palindrome - checks to see if a listint_t is a palendrome
 *@head: head of the listint_t
 *Return: 0 if is not pal 1 if is
 */

int is_palindrome(listint_t **head)
{
	int i, len;
	listint_t *back = *head;
	listint_t *begin = *head;

	for (i = 0; back->next != NULL; i++)
		back = back->next;
	len = i;
	for (; len / 2 > 0; len--)
	{
		back = *head;
		for (i = 0; i < len; i++)
		{
			back = back->next;
		}
		if (back->n != begin->n)
			return (0);
		begin = begin->next;
	}
	return (1);
}
