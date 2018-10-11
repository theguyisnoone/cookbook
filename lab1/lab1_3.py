from  collections import deque

##fgfgfgg
def search(lines,pattern,history=5):
    previous_lines= deque(maxlen=history)
    for line in lines:
        for pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

if __name__ =="__main__":
    with open(r'somefile.txt') as f:
        for line,prevlines in search(f,'Python', 5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'*20)
