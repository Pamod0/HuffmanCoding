import heapq  # To implement Priority queue using heap data structure
import pprint  # To get more clear output


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.decoding = {}

    class HeapNode:  # Heap node class
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left_child = None
            self.right_child = None

        def __lt__(self, other):  # Less than function
            return self.freq < other.freq

        def __eq__(self, other):  # Equals function
            if other is None:
                return False
            if not isinstance(other, HeapNode):
                return False
            return self.freq == other.freq

    """ Encode """

    def make_frequency_dict(self, text):  # Count frequencies of text and return
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        freq_out = pprint.pformat(frequency)
        with open("freqFile5.txt", "w") as freqf:
            freqf.write(freq_out)
        return frequency

    def make_heap(self, frequency):  # Construct Minheap
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):  # Merge two nodes one time and repeat until one node left
        while len(self.heap) > 1:  # When more than one node present
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = self.HeapNode(None, node1.freq + node2.freq)  # Create new node as parent of node1 and 2
            merged.left_child = node1
            merged.right_child = node2

            heapq.heappush(self.heap, merged)  # Push joined node to heap

    def codes_generator_helper(self, node, current_code):  # Recursive helper function to codes_generator function
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            self.decoding[current_code] = node.char
            return

        self.codes_generator_helper(node.left_child, current_code + "0")  # 0 for left branch
        self.codes_generator_helper(node.right_child, current_code + "1")  # 1 for right branch

    def codes_generator(self):
        node = heapq.heappop(self.heap)
        current_code = ""
        self.codes_generator_helper(node, current_code)

        table = pprint.pformat(self.codes)
        with open('1.Encoding Table.txt', 'w') as out1:  # output encoding table
            out1.write(table)
        table1 = pprint.pformat(self.decoding)
        with open('2.Decoding Table.txt', 'w') as out2:  # output decode table
            out2.write(table1)

    def get_encoded_text(self, text):  # encoding text
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def encode(self):
        with open("file5.txt", 'r+') as file:
            text = file.read()

            frequency = self.make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_nodes()
            self.codes_generator()

            encoded_text = self.get_encoded_text(text)

        with open("encodedFile5.txt", "w") as enc_file:  # output encoded text file
            enc_file.write(encoded_text)

        print("########## Encoded Successfully ##########")

    """  Decode  """

    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.decoding:
                character = self.decoding[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

    def decode(self):
        with open("file5.txt", 'r+') as file:
            text = file.read()

            encoded_text = self.get_encoded_text(text)
            decoded_text = self.decode_text(encoded_text)

            with open("decodedFile5.txt", "w") as dec_file:  # output encoded text file
                dec_file.write(decoded_text)

        print("########## Decoded Successfully ########## ")
