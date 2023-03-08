#include <stdio.h>
#include <stdlib.h>

/* Define the structure for a singly linked list node */
typedef struct listint_s {
	int n;
	struct listint_s *next;
} listint_t;

/* Function to insert a new node into a sorted singly linked list */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node, *prev_node;

	/* Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL) {
		return NULL;
	}

	/* Set the value of the new node */
	new_node->n = number;
	new_node->next = NULL;

	/* If the list is empty, insert the new node at the beginning */
	if (*head == NULL) {
		*head = new_node;
		return new_node;
	}

	/* Traverse the list to find the correct position to insert the new node */
	current_node = *head;
	prev_node = NULL;
	while (current_node != NULL && current_node->n < number) {
		prev_node = current_node;
		current_node = current_node->next;
	}

	/* Insert the new node at the correct position */
	if (prev_node == NULL) {
		/* Insert at the beginning of the list */
		new_node->next = *head;
		*head = new_node;
	} else {
		/* Insert in the middle or at the end of the list */
		prev_node->next = new_node;
		new_node->next = current_node;
	}

	/* Return the address of the new node */
	return new_node;
}

/* Example usage */
int main()
{
	listint_t *head = NULL;

	/* Create a sorted singly linked list */
	insert_node(&head, 1);
	insert_node(&head, 3);
	insert_node(&head, 5);
	insert_node(&head, 7);
	insert_node(&head, 9);

	/* Insert a new node into the list */
	insert_node(&head, 6);

	/* Print the contents of the list */
	printf("List contents:\n");
	listint_t *current_node = head;
	while (current_node != NULL) {
		printf("%d\n", current_node->n);
		current_node = current_node->next;
	}

	return 0;
}

