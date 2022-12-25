from utils import parse_input, check_pairs

if __name__ == "__main__":

    pair_packets = parse_input()
    packets = [x for y in pair_packets for x in y]
    packets.extend([
        [[2]],
        [[6]],
    ])

    relative_orders = []
    for i in range(len(packets)):
        relative_orders.append(
            sum([
                check_pairs(
                    packets[i],
                    packets[j],
                ) < 0 for j in range(len(packets))
            ]))

    packets = [
        x for _, x in sorted(zip(relative_orders, packets), reverse=True)
    ]

    result = 1
    for i, p in enumerate(packets):
        if (isinstance(p, list) and len(p) == 1 and isinstance(p[0], list) and
                len(p[0]) == 1 and (p[0][0] == 6 or p[0][0] == 2)):
            result *= (i + 1)

    print(result)
