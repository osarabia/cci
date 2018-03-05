from linkedlist import LinkedList

def kth_last(number, ll):
    if ll.head is None:
        return

    i = 1
    back = front = ll.head

    while i <= number:
        if front is not None:
            front = front.next
        i += 1

    while front.next is not None:
        front = front.next
        back = back.next

    return back

ll = LinkedList()
ll.generate(10, 0, 9)
print(ll)
print(kth_last(2, ll))
print(kth_last(3, ll))


