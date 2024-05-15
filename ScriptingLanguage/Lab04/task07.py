def test_set_operations():
    my_set = set()

    my_set.add(1)
    my_set.add(2)
    my_set.add(3)

    print("Set after adding elements:", my_set)
    print("Length of the set:", len(my_set))

    my_set.remove(2)
    print("Set after removing an element:", my_set)

    popped_element = my_set.pop()
    print("Removed element:", popped_element)
    print("Set after removing a random element:", my_set)


# Test the function
test_set_operations()
