
# This function should return the sum of all even numbers in the list, but it returns the wrong value. Find the bug.
# you returned if the number was not even wich stops the function
# logic error
def sum_even_numbers(numbers):

     summ = 0

     for num in numbers:

          if num % 2 == 0:

               summ += num

          else:

               continue

     return summ
print(sum_even_numbers([1,2,3,4,5,6,7,8,9,10]))