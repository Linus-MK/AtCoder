t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    if n % 2 == 1:
        print('Second')
    
    if n % 2 == 0:
        nums.sort()

        special = True
        for k in range(n // 2):
            if nums[2*k] != nums[2*k+1]:
                special = False
                break
        
        if special:
            print('Second')
        else:
            print('First')
