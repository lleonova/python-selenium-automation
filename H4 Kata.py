# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#
# Example:
# 348597 => [7,9,5,8,4,3]

def digitize(n):
    # n=str(n)[::-1]
    # result = []
    # for i in str(n)[::-1]:
    #     result.append(int(i))
    #
    return [int(i) for i in str(n)[::-1]]

print(digitize(12345))