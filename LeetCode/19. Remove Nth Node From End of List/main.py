class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    aux = [head]
    i = 0
    n -= 1
    current = head

    while current != None:
        i += 1
        if current.next != None:
            current = current.next
            aux.append(current)
        else:
            break

    j = i - n - 1
    if i == 1:
        return None

    aux[j].next = None
    if j - 1 >= 0:
        aux[j - 1].next = None

        if j + 1 < i:
            aux[j - 1].next = aux[j + 1]
        

    return head

def main():
    pass

main()