def main():
    x0 = 1
    a = 13
    c = 0
    m = 64
    N = 50000

    nums = random_number(x0, a, c, m, N)

    print("Random Numbers: ")
    print(nums)
    

def random_number(x0, a, c, m, N):
    nums = [x0]
    for i in range(N):
        x_temp = (a * nums[-1] + c) % m
        nums.append(x_temp)
    
    return nums

if __name__ == '__main__':
    main()