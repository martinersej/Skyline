def AddBuildingToExistingSkyline(S, l, h, r):
    if len(S) == 0 or S == None:
        return [l, h, r]
    
    sizeOfS = len(S)
    combined = []
    i = 0

    while i < sizeOfS - 1 and S[i] < l:
        combined.append(S[i])
        combined.append(S[i+1])
        i = i + 2

    if i == 0:
        combined.append(l)
        combined.append(h)
        if r < S[i]:
            combined.append(r)
            combined.append(0)
    elif h > S[i+1]:
        combined.append(l)
        combined.append(h)

    while i < sizeOfS-1 and S[i] < r:
        if h < S[i+1]:
            combined.append(S[i])
            combined.append(S[i+1])
        elif h > S[i+1]:
            if h != combined[len(combined)-1]:
                combined.append(S[i])
                combined.append(h)
        i = i + 2

    while i < sizeOfS:
        combined.append(S[i])
        i = i + 1

    if r < S[i-2]:
        if l > S[sizeOfS-1]:
            combined.append(0)
            combined.append(l)
        combined.append(h)
        combined.append(r)

    return combined


def divideAndConquer(S):
    return mergeConmbine(S, 0, len(S)-1)


def mergeConmbine(S, s):
    if ((len(S)-1)-s) == 0:
        return S[s]
    else:
        mid = (((len(S)-1)-s)//2)+s
        S1 = mergeConmbine(S, s, mid)
        S2 = mergeConmbine(S, mid+1, len(S))
    return MergeSkylines(S1, S2)
