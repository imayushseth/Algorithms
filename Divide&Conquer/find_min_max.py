test0 = {
  'input' : [5,2,9,0,12,3,-1,-56,744,67],
  'output' : [-56,744]
}

test1 = {
  'input' : [5000,2,9,0,12,3,-1,-56,744,-667],
  'output' : [-667,5000]
}

test2 = {
  'input' : [-555,2,9,0,12,3,-1,-56,744,6700],
  'output' : [-555,6700]
}

test3 = {
  'input' : [5,5,5],
  'output' : [5,5]
}

test4 = {
  'input' : [6,8],
  'output' : [6,8]
}

test5 = {
  'input' : [80,60],
  'output' : [60,80]
}

test6 = {
  'input' : [5],
  'output' : [5,5]
}

test7 = {
  'input' : [],
  'output' : []
}

test8 = {
  'input' : [0],
  'output' : [0,0]
}

tests = [test0,test1,test2,test3,test4,test5,test6,test7,test8]

def find_min_max(nums, start=0, end=None):

  if end is None:
    nums = list(nums)
    end = len(nums)-1

  if start > end:
    return []

  if start == end:
    return nums[start],nums[start]
  
  if end == start+1:
    return min(nums[start],nums[end]),max(nums[start],nums[end])

  mid = (start+end)//2

  left = find_min_max(nums,start,mid)
  right = find_min_max(nums,mid,end)

  return min(left[0],right[0]),max(left[1],right[1])

print(list(find_min_max(test0['input'],0,None)) == test0['output'])

for test in tests:
  print(list(find_min_max(test['input'],0,None)) == test['output'])

