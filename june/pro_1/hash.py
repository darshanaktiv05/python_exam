# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    Tuple1 = map(int, input().split())
    t = tuple(Tuple1)
    print(hash(t));