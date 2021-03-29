from src.auction.domain import Bidder, Bid, Auction, Evaluator


[print(f'{bid.user.name} bid ${bid.value}') for bid in auction.bids]

evaluator = Evaluator()
evaluator.evaluate(auction)

print(f'The lowest bid was {evaluator.lowest_bid} and the highest bid was {evaluator.highest_bid}')