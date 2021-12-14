def wordcount(fname):
    try:
        fhand=open(fname)
    except:
        print('File can not be opened')
        exit()

    count=dict()
    for line in fhand:
        words=line.split()
        for word in words:
            if word not in count:
                count[word]=1
            else:
                count[word] += 1
    return count


if __name__=='__main__':
    count=wordcount('sample3.txt')
    filtered = {key:value for key, value in count.items() if value<10 and value>2}
    print(filtered)