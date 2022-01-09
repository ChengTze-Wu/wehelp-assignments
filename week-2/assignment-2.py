def calculate(min, max):
    total = 0
    for num in range(min, max+1):
        total+=num
    print(total)
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30 


def avg(data):
    data_count = data["count"]
    data_total_salary = 0
    for employee in data["employees"]:
        data_total_salary += employee["salary"]
    print(data_total_salary / data_count)
avg({
    "count":3,
    "employees":[
    {
    "name":"John",
    "salary":30000 },
    {
    "name":"Bob",
    "salary":60000 },
    {
    "name":"Jenny",
    "salary":50000 }
    ]
}) # 呼叫 avg 函式


def maxProduct(nums):
    product_nums = []
    for num in nums:
        other_nums = nums[nums.index(num)+1:]
        for other_num in other_nums:
            product_nums.append(num*other_num)
    print(max(product_nums))
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30 
maxProduct([-1, 2]) # 得到 -2 
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2


def twoSum(nums, target):
    result = []
    for num in nums:
        other_nums = nums[nums.index(num)+1:]
        for other_num in other_nums:
            if (num+other_num) == target:
                result.append(nums.index(num))
                result.append(nums.index(other_num))
                break
    return result
result = twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


def maxZeros(nums):
    count_zero = 0
    max_count = 0
    for num in nums:
        if num == 0:
            count_zero += 1
            if count_zero > max_count:
                max_count = count_zero
        elif num == 1:
            count_zero = 0
    print(max_count)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
maxZeros([1, 1, 1, 1, 1]) # 得到 0 
maxZeros([0, 0, 0, 1, 1]) # 得到 3