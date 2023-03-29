from random import randint


class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, "value"):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        if not isinstance(new_account, Account):
            return (False)
        for acc in self.accounts:
            if acc.name == new_account.name:
                return (False)
        self.accounts.append(new_account)

    def transfer(self, origin, dest, amount):
        accounts = [[None, None], [None, None]]
        for index in range(0, len(self.accounts)):
            if hasattr(self.accounts[index], "name")\
               and origin == self.accounts[index].name:
                accounts[0][0] = self.accounts[index]
                accounts[0][1] = index
            if hasattr(self.accounts[index], "name")\
               and dest == self.accounts[index].name:
                accounts[1][0] = self.accounts[index]
                accounts[1][1] = index
        if not isinstance(accounts[0][0], Account)\
           or not isinstance(accounts[1][0], Account)\
           or self.security_check(accounts)\
           or amount < 0 or accounts[0][0].value < amount:
            return False
        if (origin != dest):
            accounts[0][0].transfer(-amount)
            accounts[1][0].transfer(amount)
        return True

    def fix_account(self, acc):
        for i in range(0, len(self.accounts)):
            if hasattr(self.accounts[i], "name")\
               and acc == self.accounts[i].name:
                acc = self.accounts[i]
                index = i
        if not isinstance(acc, Account):
            return False

        ret = self.security_check([[acc, index]])
        while ret is not None:
            if ret == "odd":
                setattr(acc, "odd", 21)
            elif ret == "b":
                acc_inf: dict = acc.__dict__
                for ele, value in acc_inf.items():
                    if ele.startswith("b"):
                        setattr(acc, "_"+ele, value)
                        delattr(acc, ele)
            elif ret == "zip":
                setattr(acc, "zip", f"{randint(99, 999)}-{randint(99, 999)}")
            elif ret == "name":
                setattr(acc, "name", "Unknow")
            elif ret == "id":
                setattr(acc, "id", Account.ID_COUNT)
                Account.ID_COUNT += 1
            elif ret == "value":
                setattr(acc, "value", 0)
            ret = self.security_check([[acc, index]])

    def security_check(self, accounts):
        for acc in accounts:
            start_with = False
            acc_inf: dict = self.accounts[acc[1]].__dict__

            for ele, value in acc_inf.items():
                if ele in ["name", "id", "value"]:
                    if ((ele == "name" and not isinstance(value, str))
                        or (ele == "id" and not isinstance(value, int))
                        or (ele == "value" and (not isinstance(
                                value, (int, float)) or value < 0))):
                        return ele
                if ele.startswith("b"):
                    return "b"
                if ele.startswith("zip") or ele.startswith("addr"):
                    start_with = True

            for attr in ['name', 'id', 'value']:
                if not hasattr(acc[0], attr):
                    return attr
            if not start_with:
                return "zip"
            if (len(acc_inf) % 2 == 0):
                return "odd"
        return None
