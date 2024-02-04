
class OwnHeap:
    def __init__(self, arr=[]):
        self.arr = []
        if arr is not None:
            for elem in arr:
                self.arr.append(elem)

    def __len__(self):
        return len(self.arr)

    def ins(self, elem):
        self.arr.append(elem)

    def ins_min(self, elem):
        self.arr.append(elem)
        last_idx = len(self.arr) - 1
        parent = (last_idx - 1) // 2
        cur = last_idx
        while parent >= 0 and self.arr[parent] > elem:
            cur = parent
            parent = (parent - 1) // 2
        self.arr[last_idx], self.arr[cur] = self.arr[cur], self.arr[last_idx]

    def ins_max(self, elem):
        self.arr.append(elem)
        last_idx = len(self.arr) - 1
        parent = (last_idx - 1) // 2
        cur = last_idx
        while parent >= 0 and self.arr[parent] < elem:
            cur = parent
            parent = (parent - 1) // 2
        self.arr[last_idx], self.arr[cur] = self.arr[cur], self.arr[last_idx]

    def heapify_min(self):

        size = len(self.arr)

        outter_parent = (size - 3 + size % 2) // 2

        while outter_parent >= 0:
            inner_parent = outter_parent
            inner_r_child = 2 * inner_parent + 2
            while inner_r_child < size:
                smaller_child = inner_r_child - \
                    (self.arr[inner_r_child] > self.arr[inner_r_child - 1])
                if self.arr[inner_parent] < self.arr[smaller_child]:
                    break
                else:
                    inner_parent = smaller_child
                    inner_r_child = 2 * inner_parent + 2

            self.arr[outter_parent], self.arr[inner_parent] = self.arr[inner_parent], self.arr[outter_parent]
            outter_parent -= 1

        if size > 0 and size % 2 == 0:
            elem = self.arr.pop()
            self.ins_min(elem)

    def heapify_max(self):

        size = len(self.arr)

        outter_parent = (size - 3 + size % 2) // 2

        while outter_parent >= 0:
            inner_parent = outter_parent
            inner_r_child = 2 * inner_parent + 2
            while inner_r_child < size:
                larger_child = inner_r_child - \
                    (self.arr[inner_r_child] < self.arr[inner_r_child - 1])
                if self.arr[inner_parent] > self.arr[larger_child]:
                    break
                else:
                    inner_parent = larger_child
                    inner_r_child = 2 * inner_parent + 2

            self.arr[outter_parent], self.arr[inner_parent] = self.arr[inner_parent], self.arr[outter_parent]
            outter_parent -= 1

        if size > 0 and size % 2 == 0:
            elem = self.arr.pop()
            self.ins_max(elem)

# ========================
# self testing

# a_heap = OwnHeap([70, 60, 50, 40, 80, 30, 20])
# print(a_heap.arr)
# a_heap.ins_max(90)
# print(a_heap.arr)
# a_heap.heapify_min()
# print(a_heap.arr)
# a_heap.ins_min(15)
# print(a_heap.arr)
# a_heap.heapify_max()
# print(a_heap.arr)
# a_heap.ins_min(0)
# print(a_heap.arr)
# a_heap.heapify_max()
# print(a_heap.arr)
