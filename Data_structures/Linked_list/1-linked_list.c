#include <stdio.h>
#include <stdlib.h>

struct node
{
	int num;

	struct node *nextptr;
}*stnode;

void createNodeList(int n);
void reverseDispList();
void displayList();

int main(void)
{
	int n;

	printf("Linked List: Create a singly linked list and print it in reverse order: \n");
	printf("Input the number of nodes: ");
	scanf("%d", &n);
	createNodeList(n);
	printf("Data entered in the list are: \n");
	displayList();
	reverseDispList();
	printf("The list in reverse is: \n");
	displayList();
	return (0);
}

void createNodeList(int n)
{
	struct node *fnNode, *tmp;
	int num, i;

	stnode = (struct node *)malloc(sizeof(struct node));
	if (stnode == NULL)
	{
		printf("Memory cannot be allocated.\n");
	}
	else
	{
		printf("Input data for node 1 : \n");
		scanf("%d", &num);
		stnode->num = num;
		stnode->nextptr = NULL;
		tmp = stnode;
		for (i = 2; i < n; i++)
		{
			fnNode = (struct node *)malloc(sizeof(struct node));
			if (fnNode == NULL)
			{
				printf("Memory cannot be allocated.\n");
				break;

			}
			else
			{
				printf("Input data for node %d: ", i);
				scanf("%d", &num);
				fnNode->num = num;
				fnNode->nextptr = NULL;
				tmp->nextptr = fnNode;
				tmp = tmp->nextptr;
			}
		}
	}
}

void reverseDispList()
{
	struct node *prevNode, *curNode;

	if (stnode != NULL)
	{
		prevNode = stnode;
		curNode = stnode->nextptr;
		stnode = stnode->nextptr;

		prevNode->nextptr = NULL;
		while (stnode != NULL)
		{
			stnode = stnode->nextptr;
			curNode->nextptr = prevNode;

			prevNode = curNode;
			curNode = stnode;
		}
		stnode = prevNode;
	}
}

void displayList()
{
	struct node *tmp;

	if (stnode == NULL)
	{
		printf("No data found in the list.\n");
	}
	else
	{
		tmp = stnode;
		while (tmp != NULL)
		{
			printf("Data = %d\n", tmp->num);
			tmp = tmp->nextptr;
		}
	}
}
