def WordListInfo(wordlist):
    shortWordLen = 0
    longWordLen = 0
    avgWordLen = 0
    sum = 0
    wordLengths = []
    wl_len = 0

    for i in range(wl_len):
        curr_len = len(wordlist[i])
        wordLengths[i] = curr_len
        sum += curr_len

        if curr_len > longWordLen:
            longWordLen = curr_len
    
    wordLengths = sorted(wordLengths)
    shortWordLen = wordLengths[0]
    avgWordLen = sum / wl_len

    return (shortWordLen, longWordLen, avgWordLen)

print(WordListInfo(['Python', 'Code', 'Computer', 'CPU', 'Algorithm', "Data"]))

        