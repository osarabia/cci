from linkedlist import LinkedList

def remove_duplicates(ll):

    if ll.head is None:
        return

    values = set([ll.head.value])
    prev = ll.head
    current = ll.head.next

    while current is not None:
        if current.value in values:
            tmp = current.next
            prev.next = tmp
            current = tmp
        else:
            values.add(current.value)
            prev = current
            current = current.next
    print("-----")
    print(ll)

def remove_duplicates_follow_up(ll):
    if ll.head is None:
        return

    current = ll.head

    while current is not None:
        prev = current
        one_ahead = current.next

        while one_ahead is not None:
            if current.value == one_ahead.value:
                prev.next = one_ahead.next
                one_ahead = one_ahead.next
            else:
                prev = one_ahead
                one_ahead = one_ahead.next

        current = current.next
    print("----")
    print(ll)

ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)
remove_duplicates(ll)
ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)
remove_duplicates_follow_up(ll)
