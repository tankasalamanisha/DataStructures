from utils import LinkedList


if __name__ == "__main__":

    print("----Insertion------")

    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")

    llist.prepend("D")

    llist.insert_after_node(llist.head.next, "E")

    llist.print_list()

    print("------Deletion-----")

    # Deletion
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")

    llist.delete_node("B")
    llist.delete_node("E")

    llist.print_list()