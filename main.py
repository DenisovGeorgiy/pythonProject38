class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list
        self.new_list = []

    def __iter__(self):
        self.list_iter = iter(self.list)
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        if len(self.list) == self.counter:
            self.list = None
            self.counter = 0
            if self.list is None:
                self.list = next(self.list_iter)
        return self.list[self.counter]


        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    print(list(FlatIterator(list_of_lists_1)))


if __name__ == '__main__':
    test_1()