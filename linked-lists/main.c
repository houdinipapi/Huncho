#include <stdio.h>
#include <stdlib.h>

typedef struct node *nodePtr;

/**
  *struct defn and typedef below are
  *broken into two parts for clarity of explaining
  *in our code we would usually combine the two
  */

struct node
{
	int data;
	nodePtr next;
};

typedef struct node node;

int main(int argc, const char *argv[])
{
	/* insert code here */
	nodePtr first = NULL;

	first = malloc(sizeof(node));
	first->next = NULL;

	/* Alternatively */
	/**
	 *node firstNode;
	 *firstNode.next
	 */

	first->data = 61;

	/**
	  *first->next = malloc (sizeof (node));
	  *first->next->next = NULL;
	  *first->next->data = 62;
	  */
	nodePtr temp;

	temp = malloc(sizeof(node));
	temp->next = first;
	first = temp;
	/* End of code */
	printf("Hello, World!\n");
	return (0);
}
