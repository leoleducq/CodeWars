def snail(snail_map):
    output = []
    while snail_map:
        output.extend(snail_map.pop(0))
        if snail_map and snail_map[0]:
            for row in snail_map:
                output.append(row.pop())
        if snail_map:
            output.extend(snail_map.pop()[::-1])
        if snail_map and snail_map[0]:
            for row in snail_map[::-1]:
                output.append(row.pop(0))
    return output