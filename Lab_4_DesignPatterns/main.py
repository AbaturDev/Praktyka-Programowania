from iterator import Iterator

list = [1, 2, 3, 4, 5, 6]

if __name__ == "__main__":
    iterator = Iterator(list)
    iterator.edit_current_element(8)
    print(iterator.get_current_element())
    iterator.next_element()
    iterator.next_element()
    iterator.next_element()
    iterator.next_element()
    iterator.next_element()
    print(iterator.get_next_element())








