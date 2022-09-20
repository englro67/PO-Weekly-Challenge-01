from unicodedata import digit


def digitSum(N, A):
    # First let's strip out the letters
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = ''
    for i in range(N):
        letterlessList = []
        for j in range(len(A[i])):
            if A[i][j] in digits:
                letterlessList.append(int(A[i][j]))
        # letters are stripped, add sum to result string
        result = result + str(sum(letterlessList)) + '\n'
    return result

def main ():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    
    print(digitSum(N, A))

if __name__ == "__main__":
    main()
