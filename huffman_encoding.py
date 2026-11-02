import heapq

def huffman(ch, freq):
    heap = [[freq[i], i, ch[i]] for i in range(len(ch))]
    heapq.heapify(heap)

    count = len(ch)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        heapq.heappush(heap, [
            a[0] + b[0],
            count,
            [a[2], b[2]]
        ])

        count += 1

    def codes(node, code=""):
        if isinstance(node, str):
            print(node, ":", code if code else "0")
        else:
            codes(node[0], code + "0")
            codes(node[1], code + "1")

    codes(heap[0][2])


# Main Program
ch = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [50, 10, 30, 5, 3, 2]

huffman(ch, freq)