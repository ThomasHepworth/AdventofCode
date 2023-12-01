# with open('dummy_input.txt', 'r') as file:
with open('input.txt', 'r') as file:
    content = [line.strip() for line in file.readlines()]

tracker = {"root": 0}
dir = ""
for c in content:

    if c.startswith("$"):
        # Tweak our directory...
        if c[:4] == "$ cd":
            counter=0
            dir_change = c[5:]
            if dir_change == "..":
                dir = dir.rpartition('/')[0]
            elif dir_change == "/":
                dir = "root"
            else:
                dir+=f"/{dir_change}"

    else:
        if not c.startswith("dir"):
            file_size=int(c.split(" ")[0])

            all_paths = dir.split("/")
            for n in range(len(all_paths)):
                idx = "/".join(all_paths[0:n+1])
                tracker[idx]+=file_size
        else:
            # Create a blank logger
            d = f"{dir}/{c.split()[-1]}"
            tracker[d] = 0

tracker

# Part 1 ans:
print("Solution to Part 1")
print(sum([n for n in tracker.values() if n < 100_000]))

# Part 2...
# Required space is 30_000_000
# Total space is 70_000_000
total_space = 70_000_000
required_space = 30_000_000
size_to_del = required_space-(total_space-tracker["root"])

folder, size = "root", tracker['root']
for k, v in tracker.items():
    if v > size_to_del and v < size:
        folder, size = k, v

print("Solution to Part 2")
print(folder)
print(size)
