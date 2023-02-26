"""
File: anagram.py
Name: Yu-Shan Cheng
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant 

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    start = time.time()
    ####################
    print('Welcome to stanCode"Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        word = input('Find Anagrams for: ')
        if word==EXIT:
            break
        else:
            find_anagrams(word)

        #print(str(anagram_num) + " anagrams: ", end='')
        #print(anagram_list)

    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    global dict_list
    dict_list=[]
    with open(FILE,'r')as f:
        for line in f:
            line=line.strip()
            dict_list.append(line)



def find_anagrams(s):
    #Transform s string into list
    letter_list=[]
    for i in range(len(s)):
        letter_list.append(s[i])

    return find_anagrams_helper(s,letter_list,[],'',[])


def find_anagrams_helper(s,letter_list,trans_list,trans_str,anagram_list):

    #BASE CASE
    if len(trans_str)==len(letter_list) and exact_word(trans_str)==True: #檢查字典#
        print(has_prefix(trans_str))

        print('Searching...')
        print('Found:' + trans_str)

        #global anagram_list
        #global anagram_num
        #print(anagram_list)

        anagram_list.append(trans_str)
        anagram_num = len(anagram_list)

        print(str(anagram_num) + " anagrams: ", end='')
        print(anagram_list)

        return trans_list,anagram_list

    #RECURSIVE
    else:

        for ltr in letter_list:
            if ltr not in trans_list:

                #CHOOSE
                trans_list.append(ltr)
                trans_str = "".join([str(_) for _ in trans_list])

                if has_prefix(trans_str)is True:

                    #EXPLORE
                    find_anagrams_helper(s, letter_list, trans_list, trans_str, anagram_list)

                #UNCHOOSE
                trans_list.remove(ltr)


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """

    for word in dict_list:
        if word.startswith(sub_s):
            return True
    return False

def exact_word(trans_str):
	for word in dict_list:
		if word.startswith(trans_str) and len(word) == len(trans_str):
			return True
	return False



if __name__ == '__main__':
    main()
