def cal_fact_rec(n):
    if(n==1 or n==0):
        return 1
    return n*cal_fact_rec(n-1)

print(cal_fact_rec(6))  # Output: 120