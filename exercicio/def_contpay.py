def computpay(h,r):
    if h <= 40.0:
        return h * r
    else:
        hx = h - 40
        h = hrs - hx

    return (h * r) + (hx * (r * 1.5))

hrs = float(input("Enter Hours: "))
rate = float(input("Enter te rate: "))

p = computpay(hrs,rate)

print("Pay",p)
