# Array and Strings

## Hash Tables

A mapping of keys to values. Where the key is inputted into a hash function which returns the index of where the value is stored in an array. 3 components: key, hash function, hash table. _Worst case_ occurs if there are collisions, meaning different keys result in the same index. Usual hash functions are something like hash(key) % array_size, which can result in same key. A linked list could be used to store values for hash tables with collisions.

Best case - O(1)

Worst Case - O(N)

## ArrayList & Resizable Arrays

In some languages, arrays are automatically resized when adding items, however, others like Java do not resize automatically and size cannot change after being created. Usually, when size is full then the array doubles in size. The resizing is O(N).

Insertion is still O(1) on average since resize is rare, but worst case is O(N).

## StringBuilder

