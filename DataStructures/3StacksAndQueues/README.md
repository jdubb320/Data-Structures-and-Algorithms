# Stacks and Queues

## Stack

Think of a _stack_ of plates :)

**LIFO: Last In First Out**

Operations on Stacks:

- _pop()_: remove top item from stack
- _push(item)_: add an item to top of stack
- _peek()_: return the top of stack
- _isEmpty()_: return true only if stack is empty

O(1) for adds/removes but not for accessing i'th item; constant since no rearranging of items required

Can be implemented as linked list if adding/removal are on the _same_ side

## Queue

Think of a line/queue at a ticket stand

**FIFO: Fist In First Out**

Operations on Queues:

- _add(item)_: add item to the end of the queue
- _remove()_: remove first item in queue
- _peek()_: return the top of queue
- _isEmpty()_: return true only if queue is empty

Can be implemented as linked list if adding/removal are on the _opposite_ sides