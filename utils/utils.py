def by_to_st(msg):
    print(str(msg)[2:-1])


def hexdump(src, length=16):
    FILTER = "".join([(len(repr(chr(x))) == 3) and chr(x) or "." for x in range(256)])
    lines = []
    for c in range(0, len(src), length):
        chars = src[c : c + length]
        hex = " ".join(["%02x" % ord(x) for x in chars])
        printable = "".join(
            ["%s" % ((ord(x) <= 127 and FILTER[ord(x)]) or ".") for x in chars]
        )
        lines.append("%04x  %-*s  %s\n" % (c, length * 3, hex, printable))
    return "".join(lines)


def group(a, *ns):
    for n in ns:
        a = [a[i : i + n] for i in range(0, len(a), n)]
    return a


def join(a, *cs):
    return [cs[0].join(join(t, *cs[1:])) for t in a] if cs else a


def hexdump_file(data):
    toHex = lambda c: "{:02X}".format(c)
    toChr = lambda c: chr(c) if 32 <= c < 127 else "."
    make = lambda f, *cs: join(group(list(map(f, data)), 8, 2), *cs)
    hs = make(toHex, "  ", " ")
    cs = make(toChr, " ", "")
    for i, (h, c) in enumerate(zip(hs, cs)):
        print("{:010X}: {:48}  {:16}".format(i * 16, h, c))


def bcdDigits(chars, num):
    """converte caracter numerico para bcd digit"""
    for char in chars:
        char = ord(char)
        for val in (char >> num, char & 0xF):
            if val == 0xF:
                return
            print(val)
