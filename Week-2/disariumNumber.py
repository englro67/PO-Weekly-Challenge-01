def is_disarium(number):
    total = 0
    for i in range(len(number)):
        total = total + (int(number[i]) ** (i+1))
    if total == int(number):
        return True
    else:
        return False

def main ():
    N = input("Please provide a number: ")
    print(is_disarium(N))

if __name__ == "__main__":
    main()