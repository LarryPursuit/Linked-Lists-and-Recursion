from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance to act as the employee ID roster
    roster = LinkedList()

    # 2) Insert some sample data using insert_at_front or insert_at_end
    roster.insert_at_end(101)
    roster.insert_at_end(102)
    roster.insert_at_end(103)
    roster.insert_at_front(100)

    # 3) Display the list to verify insertion
    print("Employee ID roster:")
    roster.display()

    # 4) Call recursive_sum and print the result
    print(f"\nSum of all IDs: {roster.recursive_sum()}")

    # 5) Call recursive_search with a target and print result
    for target in (102, 999):
        found = roster.recursive_search(target)
        print(f"Is ID {target} on the roster? {'Yes' if found else 'No'}")

    # 6) Call recursive_reverse, then display the reversed list
    roster.recursive_reverse()
    print("\nRoster after reversing:")
    roster.display()
