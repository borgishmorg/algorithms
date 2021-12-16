class BinaryHeap:
    def __init__(self) -> None:
        self._data = []

    def add(self, value: int):
        self._data.append(value)

        i = len(self._data) - 1
        while i and self._data[(i - 1) // 2] < self._data[i]:
            self._data[(i - 1) // 2], self._data[i] = (
                self._data[i],
                self._data[(i - 1) // 2],
            )
            i = (i - 1) // 2

    def get(self) -> int:
        value = self._data[0]

        if len(self._data) > 1:
            self._data[0] = self._data.pop()
            i = 0
            while True:
                ni = i * 2 + 1
                if ni >= len(self._data):
                    break
                if ni + 1 < len(self._data) and self._data[ni + 1] > self._data[ni]:
                    ni += 1
                if self._data[i] >= self._data[ni]:
                    break
                self._data[ni], self._data[i] = self._data[i], self._data[ni]
                i = ni
        else:
            self._data = []

        return value
