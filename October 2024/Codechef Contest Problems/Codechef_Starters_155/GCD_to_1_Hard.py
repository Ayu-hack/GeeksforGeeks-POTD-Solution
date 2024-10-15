def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        matrix = [[2 for _ in range(m)] for _ in range(n)]
        if n>m:
            for i in range(n):
                matrix[i][i%m] = 3
        else:
            for i in range(m):
                matrix[i%n][i] = 3
        print_matrix(matrix)


def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()



if __name__ == "__main__":
    main()