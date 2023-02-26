"""
File: priority_queue_list.py
Name: Yu-Shan Cheng
----------------------------------
This program shows how to build a priority queue by
using Python list. We will be discussing 3 different
conditions while appending:
1) Prepend
2) Append
3) Append in between
"""

# This constant controls when to stop the user input
EXIT = ''


def main():
    priority_queue = []

    print('--------------------------------')
    while True:
        name = input("Patient: ")
        if name == EXIT:
            break
        priority = int(input("Priority: "))
        data = (name, priority)  #data是一顆tuple

        if len(priority_queue) == 0:
            priority_queue.append(data)   #確認是不是第一筆資料
        else:
                #Prepend
            if priority_queue[0][1] > priority:  #不是>= 因為queue
                #Tie breaking 解決平手問題
                priority_queue.insert(0, data)
            elif priority_queue[len(priority_queue)-1][1] <= priority: #平手去後面  #-1 是因為index是0, 1, 2 必須減一不然超出是3
                priority_queue.append(data)
                #in between
            else:
                for i in range(len(priority_queue)-1):  # 兩兩選取時這樣才不會漏掉揍後一個  # non-dynamic 已經決定次數，不會隨著資料結構的增加而改變次數。和C++不同。
                    if priority_queue[i][1] <= priority < priority_queue[i+1][1]:  # 去某個人的後面是允許等於的，前面不允許。
                        priority_queue.insert(i+1, data)  # 因為要插入在i 和 i+1 中間，必須i+1
                        break

    print('--------------------------------')

    print(priority_queue)


if __name__ == '__main__':
    main()
