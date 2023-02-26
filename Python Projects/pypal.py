
WITHDRAW_LIMIT = 1000
BALANCE = 0


class Pypal:
    def __init__(self, username, balance = BALANCE, withdrawal = WITHDRAW_LIMIT):
        self._n = username
        self.__b = balance
        self._w_l = withdrawal

    def withdrawal(self, amount):
        if amount > self._w_l:
            print("Exceed withdrawal limit.")

        if amount > self.__b:
            print("Illegal.")

        else:
            self.__b -= amount
            print(f"{self._n} remains: {self.__b}")

    # setter
    def set_withdrawal_limit(self, new_withdrawal):
        self._w_l = new_withdrawal
        print("Updated!")
    # getter 通常會return


    def get_name(self):
        return self._n

    def __str__(self):
        return f"Name={self.n}/$={self.__m}/Limit={self._w_l}"

    def starter(self):
        jerry_account= Pypal("JERRY", money=1000, withdrawal=500)
        print(jerry_account)


def bank():
    ys_a = Pypal("YS", 2000, 500)
    ys_a.withdrawal(200)
    ys_a.set_withdrawal_limit(1500)
    ys_a.withdrawal(1600)
    print(ys_a.get_name())


if __name__=='__main__':
    bank()