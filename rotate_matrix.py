def print_matrix(matrix):
    print
    for row in matrix:
        for e in row:
            print e,
        print

def rotateImage(a):
    
    def swap(f, g):
        return g, f
    
    def swap_rows():
        for i in xrange(len(a)/2):
            j = len(a)-1-i
            a[i], a[j] = swap(a[i], a[j])
    
    def transpose():
        for i in xrange(len(a)):
            for j in xrange(i):
                a[i][j], a[j][i] = swap(a[i][j], a[j][i])

    def rotate():
        swap_rows()
        transpose()

    rotate()
    
    return a

def main():
    a = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    print_matrix(matrix=a)

    a = rotateImage(a)

    print_matrix(matrix=a)

if __name__ == "__main__":
    main()
