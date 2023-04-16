# python3

def read_input():
    inpt = input()
    if 'I' in inpt:
        pattern = input().strip()
        text = input().strip()
    elif 'F' in inpt:
        with open('./tests/06')as file:
            data = file.read().split("\n")
            pattern = data[0].strip
            text = data[1].strip
    return (pattern, text)
   

def print_occurrences(output):
    
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash(pattern)
    t_hash = hash(text[:p_len])
    occurrances = []

    for i in range(t_len-p_len+1):
        temp = text[i:i+p_len]
        if hash(temp) == hash(pattern):
            occurrances.append(i)
   
    return occurrances



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))



