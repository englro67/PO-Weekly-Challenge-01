from unittest import result


def secondMax(size, list):
    result = ""
    for i in range(size):
        list[i].sort()
        result = result + str(list[i][-2]) + "\n"
    return result

def main ():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split(" "))))
    
    print(secondMax(N, A))

if __name__ == "__main__":
    main()