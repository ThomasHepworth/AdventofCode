with open('input.txt') as f: stream = f.read()
# stream = "bvwbjplbgvbhsrlpgdmjqwftvncz"

def find_marker(n):
    for idx in range(len(stream)-n):
        unique_chars = set(stream[idx:idx+n])
        if len(unique_chars)==n:
            return idx+n

print(find_marker(4))
print(find_marker(14))
