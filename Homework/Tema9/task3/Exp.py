
def count_lines(lines):
    line_count = 0

    with open(lines, 'r') as f:
        for line in f:
            line_count += 1
    return line_count

def count_char(lines):
    char_count = 0

    with open(lines, 'r') as f:
        for line in f:
            char_count += len(line)
    return char_count

lines = 'C:/Users/user/OneDrive/Desktop/exp.txt'
result1 = count_char(lines)
result2 = count_lines(lines)
print(f'Number of Lines: {result2}')
print(f'Number of Charcters: {result1}')