def main(n):
    r=0
    last=0
    while (n > 0):
        last = n%10
        r = r*10 + last
        print("rem:%d res:%d n:%d" % (last, r, n))
        n=n//10
        print("Rev : %d" %r)
    return

main(1223)
