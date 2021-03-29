from unittest import TestCase

from src.auction.domain import Bidder, Bid, Auction, Evaluator


class TestEvaluator(TestCase):
    def test_evaluate(self):
        lew = Bidder('Lew')
        feh = Bidder('Feh')

        feh_bid = Bid(feh, 150)
        lew_bid = Bid(lew, 100)

        auction = Auction('Phone')

        auction.bids.append(lew_bid)
        auction.bids.append(feh_bid)

        evaluator = Evaluator()
        evaluator.evaluate(auction)

        expected_lowest_value = 100
        expected_highest_value = 150

        self.assertEqual(expected_lowest_value, evaluator.lowest_bid)
        self.assertEqual(expected_highest_value, evaluator.highest_bid)

        print(f'The lowest bid was {evaluator.lowest_bid} and the highest bid was {evaluator.highest_bid}')
