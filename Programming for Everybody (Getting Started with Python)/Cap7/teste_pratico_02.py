fname = "mbox-short.txt"
fh = open(fname)
count = 0
totalizador = 0.00
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    sbegin = line.find(".") - 1
    send = float(line[sbegin:])
    totalizador = totalizador + send
    count = count + 1
media = (totalizador / count)
print('Average spam confidence: ',media)
