def read_info_from_txt(file_path: str) -> tuple[int, int]: # Reads file in sequence n(number of months), and m(number of lifespan)
    with open(file_path) as f: # Open the file for reading
        n, m = map(int, f.read().split())
    return n, m

def count_rabbits(n: int, m: int) -> int: # Returns total rabbit pairs alive after n months, given lifespan m
    history = {0: 1, 1: 1, 2: 1} # Pairs alive at the end of months 0, 1 and 2
    for i in range(3, n + 1):
        idx = i - m - 1 # Month whose pairs reach age m and die this month
        died = history[idx] if idx >= 0 else 0 # Pairs dying this month, 0 if none are old enough to die yet
        history[i] = history[i - 1] + history[i - 2] - died # Fibonacci growth subtracting the pairs that died
    return history[n]

if __name__ == "__main__": # Entry point of code
    n, m = read_info_from_txt("rosalind_fibd.txt")
    result = count_rabbits(n, m)
    print(result)
