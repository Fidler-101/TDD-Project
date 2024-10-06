def sum_of_even(nums: list) -> int:
    tot: int = 0
    for i in nums:
        if i % 2 == 0:
            tot += i

    return tot


def calculate_median(nums=None) -> int:
    # Check if the list empty or not
    if nums is not None:
        length: int = len(nums)
        nums.sort()

        # Checking if the list is even or odd
        if length % 2 == 0:
            med_1 = nums[length // 2]
            med_2 = nums[length // 2 - 1]
            median = (med_1 + med_2) / 2
        else:
            median = nums[length // 2]
    else:
        median = -1

    return median


# def find_missing_number(nums: list):
#     global value
#     length: int = len(nums)
#     e_nums: list = []
#     for i in range(1, length + 1):
#         if i in nums:
#             e_nums.append(i)
#         else:
#             value = i
#
#     for y in range(len(nums)):
#         if e_nums[y] in nums:
#             value = 'none'
#
#     return value

def find_missing_number(nums: list) -> int or str:
    length = len(nums)
    expected_numbers = set(range(1, length + 1))
    actual_numbers = set(nums)
    missing_numbers = expected_numbers - actual_numbers

    if missing_numbers:
        return missing_numbers.pop()
    return 'none'

def remove_duplicates(string: str):
    nums = []
    no_dupl = set()

    for i in string:
        if i not in no_dupl:
            nums.append(i)
            no_dupl.add(i)

    return ''.join(nums)


def first_non_repeating_char(string=None):
    if string is not None and string != "":
        dup = []
        nums = []

        for i in string:
            nums.append(i)

        # Check for duplicates
        for y in nums:
            if nums.count(y) > 1 and y not in dup:
                dup.append(y)

        # Check the first non-repeating character
        for a in nums:
            if nums.count(a) == 1:
                return a

        # If no non-repeating character is found, return None
        return None
    else:
        # Handle None or empty string
        return None




