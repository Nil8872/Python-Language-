f = open("Nilesh.txt")
# a = f.read()
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell()) # tell() is used for find location of file handller
print(f.readline())
f.seek(10) # seek() is used for reset file handler
print(f.readline())