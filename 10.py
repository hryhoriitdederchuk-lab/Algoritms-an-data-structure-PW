import heapq
import os
import struct
import sys
from collections import Counter
 
MAGIC = b"HUF1"
 
 
def build_tree(freq):
    heap = []
    for index, symbol in enumerate(sorted(freq)):
        heap.append((freq[symbol], index, symbol))
    heapq.heapify(heap)
    counter = len(heap)
    while len(heap) > 1:
        w1, _, n1 = heapq.heappop(heap)
        w2, _, n2 = heapq.heappop(heap)
        heapq.heappush(heap, (w1 + w2, counter, (n1, n2)))
        counter += 1
    return heap[0][2]
 
 
def build_codes(freq):
    if len(freq) == 1:
        return {next(iter(freq)): "0"}
    codes = {}
    stack = [(build_tree(freq), "")]
    while stack:
        node, prefix = stack.pop()
        if isinstance(node, tuple):
            stack.append((node[1], prefix + "1"))
            stack.append((node[0], prefix + "0"))
        else:
            codes[node] = prefix
    return codes
 
 
def encode_text(text):
    freq = Counter(text)
    codes = build_codes(freq)
    return "".join(codes[ch] for ch in text), codes, freq
 
 
def decode_text(bits, codes):
    reverse = {code: symbol for symbol, code in codes.items()}
    result = []
    current = ""
    for bit in bits:
        current += bit
        if current in reverse:
            result.append(reverse[current])
            current = ""
    return "".join(result)
 
 
def demo(phrase):
    if not phrase:
        print("Порожня фраза.")
        return
    bits, codes, freq = encode_text(phrase)
    total = len(phrase)
    print("Фраза:", phrase)
    print("Довжина фрази:", total, "символів")
    print("Розмір словника:", len(freq))
    print()
    print("Символ | Частота | Вага   | Код")
    for symbol, count in sorted(freq.items(), key=lambda item: (-item[1], item[0])):
        print(f"{symbol!r:6} | {count:7} | {count / total:.4f} | {codes[symbol]}")
    print()
    print("Закодована фраза:", bits)
    uniform_bits = max(1, (len(freq) - 1).bit_length())
    uniform_length = uniform_bits * total
    print("Довжина коду Хаффмана:", len(bits), "біт")
    print(f"Довжина рівномірного коду: {uniform_length} біт ({uniform_bits} біт на символ)")
    print(f"Економія: {uniform_length - len(bits)} біт ({(1 - len(bits) / uniform_length) * 100:.2f}%)")
    print("Декодована фраза:", decode_text(bits, codes))
    print("Перевірка:", "успішно" if decode_text(bits, codes) == phrase else "помилка")
 
 
def compress_file(source, target):
    with open(source, "rb") as file:
        data = file.read()
    freq = Counter(data)
    header = bytearray(MAGIC)
    header += struct.pack(">QH", len(data), len(freq))
    for symbol in sorted(freq):
        header += struct.pack(">BQ", symbol, freq[symbol])
    payload = b""
    if len(freq) > 1:
        codes = build_codes(freq)
        bits = "".join(codes[byte] for byte in data)
        bits += "0" * ((-len(bits)) % 8)
        payload = int(bits, 2).to_bytes(len(bits) // 8, "big")
    with open(target, "wb") as file:
        file.write(header)
        file.write(payload)
    original = len(data)
    packed = os.path.getsize(target)
    ratio = packed / original * 100 if original else 0
    print(f"Розмір до стиснення: {original} байт")
    print(f"Розмір після стиснення: {packed} байт ({ratio:.2f}% від початкового)")
 
 
def decompress_file(source, target):
    with open(source, "rb") as file:
        blob = file.read()
    if blob[:4] != MAGIC:
        raise ValueError("Невірний формат файлу")
    position = 4
    length, unique = struct.unpack_from(">QH", blob, position)
    position += struct.calcsize(">QH")
    freq = {}
    for _ in range(unique):
        symbol, count = struct.unpack_from(">BQ", blob, position)
        position += struct.calcsize(">BQ")
        freq[symbol] = count
    payload = blob[position:]
    if length == 0:
        result = b""
    elif unique == 1:
        result = bytes([next(iter(freq))]) * length
    else:
        root = build_tree(freq)
        output = bytearray()
        node = root
        done = False
        for byte in payload:
            for shift in range(7, -1, -1):
                node = node[(byte >> shift) & 1]
                if not isinstance(node, tuple):
                    output.append(node)
                    node = root
                    if len(output) == length:
                        done = True
                        break
            if done:
                break
        result = bytes(output)
    with open(target, "wb") as file:
        file.write(result)
    print(f"Розпаковано {len(result)} байт")
 
 
def usage():
    print("Використання:")
    print("  python huffman.py                      - кодування довільної фрази")
    print("  python huffman.py demo \"фраза\"         - кодування заданої фрази")
    print("  python huffman.py compress вхід вихід  - стиснення файлу")
    print("  python huffman.py decompress вхід вихід - розпакування файлу")
 
 
def main():
    args = sys.argv[1:]
    if not args:
        try:
            phrase = input("Введіть фразу: ")
        except EOFError:
            phrase = ""
        demo(phrase or "абабагаламага")
    elif args[0] == "demo":
        demo(" ".join(args[1:]) or "абабагаламага")
    elif args[0] == "compress" and len(args) == 3:
        compress_file(args[1], args[2])
    elif args[0] == "decompress" and len(args) == 3:
        decompress_file(args[1], args[2])
    else:
        usage()
 
 
if __name__ == "__main__":
    main()