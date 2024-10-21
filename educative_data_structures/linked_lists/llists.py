from utils import LinkedList


if __name__ == "__main__":

    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")

    llist.prepend("D")

    llist.insert_after_node(llist.head.next, "E")

    llist.print_list()