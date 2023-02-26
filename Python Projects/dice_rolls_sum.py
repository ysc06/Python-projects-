"""
File: dice_rolls_sum.py
Name:Yu-Shan Cheng
-----------------------------
This program finds all the dice rolls permutations
that sum up to a constant TOTAL. Students will find
early stopping a good strategy of decreasing the number
of recursive calls
"""

# This constant controls the sum of dice of our interest
TOTAL = 8


def main():
    dice_sum(TOTAL)


def dice_sum(target_sum):
    counter = [0] # 用list裝可以避開stack問題，用heap存
    dice_sum_helper(target_sum, [], counter)
    print(counter)


def dice_sum_helper(target_sum, current_lst, counter):
    counter[0] += 1
    if sum(current_lst) <= target_sum:   # 必須加這個條件，否則 1,1,1,1,1,1,1,2 (3, 4, 5,...)會佔用太多記憶體，最後得到error message
        # 用sum比len 節省記憶體空間
        if sum(current_lst) == target_sum:    # sum is a python built in and it can add up lists.
            print(current_lst)

        else:
            for roll in [1,2,3,4,5,6]:  # 不斷加骰子
                if sum(current_lst) + roll > target_sum:
                    break
                else:
                    # Choose
                    current_lst.append(roll)
                    # Explore
                    dice_sum_helper(target_sum, current_lst, counter)
                    # Un-choose
                    current_lst.pop()

if __name__ == '__main__':
    main()
