str = input()
symbols = set(str)

for s in sorted(symbols):
    print(f"{s}: {str.count(s)} time/s")
 