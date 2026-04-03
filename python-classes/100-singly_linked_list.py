#!/usr/bin/python3
"""
Module 100-singly_linked_list

Defines a singly-linked list with sorted insertion.
Includes Node and SinglyLinkedList classes.
"""


class Node:
    """Represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a Node.

        Args:
            data (int): The value of the node.
            next_node (Node, optional): The next node (default None).

        Raises:
            TypeError: If data is not an integer or next_node
                       is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node with type checking."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node with type checking."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly-linked list with sorted insertion."""

    def __init__(self):
        """Initialize an empty singly-linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node with value in ascending order.

        Args:
            value (int): Data for the new node.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Return string representation of the list.

        Each node's data is printed on a separate line.
        """
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
