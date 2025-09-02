# algorithm

Handle hashtable collision:
The key insight is that you must store the original key along with the value so you can verify you've found the right item during retrieval, even when it's been moved due to collisions.
