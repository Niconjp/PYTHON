# https://www.codewars.com/kata/55de6173a8fbe814ee000061

# 7 kyu

# Filter unused digits

def unused_digits(*args):
    nums = [0,1,2,3,4,5,6,7,8,9]
    lst = []
    for x in args:
        lst.append([int(d) for d in str(x)])
  
    for l in lst:
        for i in l:
            if (i in nums):
                nums.remove(i)
    
    a = ''.join(str(i) for i in nums)
    
    print(f"'{a}'")
    
    return "".join(number for number in "0123456789" if number not in str(args))
