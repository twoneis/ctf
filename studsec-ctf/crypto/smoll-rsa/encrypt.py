from flag import p, q, flag


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
    return gcd, x, y


def do_rsa():
    e = 65537

    # compute n
    n = p * q

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    gcd, d, b = egcd(e, phi)

    # Decrypt ciphertext
    ct = pow(int(flag.encode("ascii").hex(), 16), e, n)
    pt = pow(ct, d, n)

    return hex(n), hex(ct), hex(pt)


if __name__ == "__main__":
    n, ct, pt = do_rsa()

    print(pt)

    with open("output.txt", "w") as f:
        f.write(f"n={n}\n")
        f.write(f"ct={ct}\n")
