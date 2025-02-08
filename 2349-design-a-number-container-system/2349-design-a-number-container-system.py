class NumberContainers:
    def __init__(self):
        self.number_to_indices = defaultdict(list)
        self.index_to_numbers = {}

    def change(self, index: int, number: int) -> None:
        self.index_to_numbers[index] = number

        heapq.heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        if not self.number_to_indices[number]:
            return -1

        while self.number_to_indices[number]:
            index = self.number_to_indices[number][0]

            if self.index_to_numbers.get(index) == number:
                return index

            heapq.heappop(self.number_to_indices[number])
        return -1


