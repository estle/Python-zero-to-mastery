import zlib

string = "hello world!hello world!hello world!hello world!"
comp = zlib.compress(string.encode())
print(comp)
print(zlib.decompress(comp))