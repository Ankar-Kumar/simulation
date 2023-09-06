def main():
    seed=7182
    N=40
    nums=random_number(seed,N)
    print(nums)
def random_number(seed,N):
    nums=[seed]
    for i in range(N):
        if nums[-1]==0:
            break
        s=str(nums[-1]**2)
        while len(s)!=8:
            s='0'+s
        num_mid=int(s[2:6])
        nums.append(num_mid)

    return nums

if __name__ == '__main__':
    main()

