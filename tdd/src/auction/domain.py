from sys import float_info


class Bidder:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Bid:

    def __init__(self, user, value):
        self.user = user
        self.value = value


class Auction:

    def __init__(self, description):
        self.description = description
        self.__bids = []

    @property
    def bids(self):
        return self.__bids


class Evaluator:

    def __init__(self) -> None:
        self.highest_bid = float_info.min
        self.lowest_bid = float_info.max

    def evaluate(self, auction: Auction):
        for bid in auction.bids:
            if bid.value > self.highest_bid:
                self.highest_bid = bid.value

            if bid.value < self.lowest_bid:
                self.lowest_bid = bid.value
