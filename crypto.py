def isCryptSolution(crypt, solution):
        mapping = {}
        for s in solution:
                mapping.setdefault(s[0], s[1])
        
        def decrypt(crypt):
                if len(crypt) == 1:
                        return int(mapping[crypt]), True

                dec = ''
                is_valid = True

                for i, c in enumerate(crypt):
                        d = mapping[c]
                        dec += d
                        if i == 0 and d == '0':
                                is_valid = False
                                break

                return int(dec), is_valid

        n0, is_valid = decrypt(crypt[0])
        if not is_valid:
                return False
        
        n1, is_valid = decrypt(crypt[1])
        if not is_valid:
                return False
        
        n2, is_valid = decrypt(crypt[2])
        if not is_valid:
                return False
        
        return n0 + n1 == n2

def main():
        crypt = ["SEND", "MORE", "MONEY"]
        solution = [['O', '0'],
                ['M', '1'],
                ['Y', '2'],
                ['E', '5'],
                ['N', '6'],
                ['D', '7'],
                ['R', '8'],
                ['S', '9']]

        print isCryptSolution(crypt, solution)

if __name__ == "__main__":
        main()
