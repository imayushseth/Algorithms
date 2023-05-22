
test0 = {
  'input' : {
    'nums' : [1,2,3,4,5,6,7],
    'find' : 6
  },
  'output' : 5
}

test1 = {
  'input' : {
    'nums' : [1,2,3,4,5,6,7],
    'find' : 2
  },
  'output' : 1
}

test2 = {
  'input' : {
    'nums' : [1,2,3,4,5,6,7],
    'find' : 4
  },
  'output' : 3
}

test3 = {
  'input' : {
    'nums' : [111],
    'find' : 111
  },
  'output' : 0
}

test4 = {
  'input' : {
    'nums' : [1,2,3,4,5,6,7],
    'find' : 7
  },
  'output' : 6
}

test5 = {
  'input' : {
    'nums' : [],
    'find' : 6
  },
  'output' : -1
}

test6 = {
  'input' : {
    'nums' : [1,2,3,4,5,6,7],
    'find' : 8
  },
  'output' : -1
}

test7 = {
  'input' : {
    'nums' : [1,1,1,1,1],
    'find' : 1
  },
  'output' : 0
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7]


def binary_search(lo, hi, condition):
  while lo <= hi:
    mid = (lo + hi)//2
    result = condition(mid)
    if result == 'found':
      return mid
    elif result == 'left':
      hi = mid - 1
    else:
      lo = mid + 1
  return -1


def locate(nums, find):
  def condition(mid):
    if nums[mid] == find:
      if nums[mid-1] == find and mid-1 >= 0:
        return 'left'
      return 'found'
    elif nums[mid] > find:
      return 'left'
    else:
      return 'right'
  return binary_search(0, len(nums) - 1, condition)


for test in tests:
  print(locate(**test['input']) == test['output'])





