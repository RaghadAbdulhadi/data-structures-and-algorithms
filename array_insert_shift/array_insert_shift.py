import math

# Using built-in methods
def insert_shift_array(arr, num):
  arr_middle =  math.ceil((len(arr) / 2))
  arr.insert(arr_middle, num)
  return arr
insert_shift_array()

# Return new array
def insert_shift_array(arr, num):
  new_arr = [None] * (len(arr)+1)
  new_arr_index = 0
  arr_index = 0
  middle_index = math.ceil((len(arr) / 2))
  for element in arr:
    if arr_index == middle_index:
      new_arr[new_arr_index] = num
      new_arr[new_arr_index+1] = arr[arr_index]
    elif arr_index < middle_index:
      new_arr[new_arr_index] = arr[arr_index]
    else:
      new_arr[new_arr_index + 1] = arr[arr_index]
    arr_index += 1
    new_arr_index += 1

  return new_arr
    
insert_shift_array()

# Returning the same array
def insert_shift_array(arr, num):
  
  inserted_idx = math.ceil(len(arr) / 2)
  arr = arr + [None]
  for index, element in enumerate(arr):
    if index == inserted_idx:
      arr[index] = num
      arr[len(arr)-1] = element
      arr[len(arr)-1], arr[inserted_idx + 1] = arr[inserted_idx + 1], arr[len(arr)-1]
  return arr

insert_shift_array()

