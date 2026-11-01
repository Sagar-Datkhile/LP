import heapq

def huffman(ch, freq):
    heap = [[freq[i],ch[i]] for i in range(len(ch))]
    heapq.heapify(heap)

    while len(heap)>1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap,[a[0] + b[0], [a[1], b[1]]])
        

    def codes (node, code=""):
        if isinstance(node,str):
            print(node,":",code)
        else:
            codes(node[0],code+"0")
            codes(node[1],code+"1")
    codes(heap[0][1])
ch = ['a','b','c','d']
freq = [5,9,12,13]

huffman(ch, freq)