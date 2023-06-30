class Cashier(object):

    cash = 50000

    def top_up(self, x):
        self.cash += x
        return self.cash

    def count_1000(self):
        return self.cash % 1000


    def take_away(self, x):
        if x <= self.cash:
            self.cash -= x
            return self.cash
        else:
            return("Oh-oh")


bank = Cashier()

bank.top_up(5500)


print(bank.cash, bank.take_away(200000), bank.count_1000())

