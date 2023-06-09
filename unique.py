def unique_in_order(sequence):
    result = []
    for i in range(len(sequence)):
        if i==0:
            result.append(sequence[i])
        elif i!=len(sequence)-1:
            if (((sequence[i]!=sequence[i+1])& (sequence[i] != result[-1])) |
                ((sequence[i]==sequence[i+1]) & (sequence[i] != result[-1]))):
                result.append(sequence[i])
        else:
            if sequence[i] != result[-1]:
                result.append(sequence[i])
    return result
