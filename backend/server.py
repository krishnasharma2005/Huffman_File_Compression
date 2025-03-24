from flask import Flask, request, jsonify, send_file
import heapq
import os

app = Flask(__name__)

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", code_dict={}):
    if node is not None:
        if node.char is not None:
            code_dict[node.char] = prefix
        generate_codes(node.left, prefix + "0", code_dict)
        generate_codes(node.right, prefix + "1", code_dict)
    return code_dict

def compress_text(text):
    root = build_huffman_tree(text)
    huffman_codes = generate_codes(root)

    encoded_text = "".join(huffman_codes[char] for char in text)
    padding = 8 - len(encoded_text) % 8
    encoded_text += "0" * padding

    compressed_bytes = bytearray()
    for i in range(0, len(encoded_text), 8):
        byte = int(encoded_text[i:i+8], 2)
        compressed_bytes.append(byte)

    with open("compressed.bin", "wb") as f:
        f.write(bytes(compressed_bytes))

    return encoded_text, root, huffman_codes

@app.route("/compress", methods=["POST"])
def compress():
    file = request.files["file"]
    text = file.read().decode("utf-8")

    encoded_text, root, huffman_codes = compress_text(text)

    original_size = len(text.encode("utf-8"))
    compressed_size = len(encoded_text) // 8  # Convert bits to bytes
    compression_percentage = round(100 - ((compressed_size / original_size) * 100), 2)

    return jsonify({
        "original_size": original_size,
        "compressed_size": compressed_size,
        "compression_percentage": compression_percentage,
        "encoded_text": encoded_text[:500] + "..."  # Show first 500 chars to preview
    })

@app.route("/download")
def download():
    return send_file("compressed.bin", as_attachment=True)

if __name__ == "__main__":
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
