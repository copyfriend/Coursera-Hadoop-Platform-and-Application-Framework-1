def splitShowViews(line):
    kv = line.strip().split(",")
    return (kv[0], int(kv[1]))
