from doublex import Spy
from doublex_expects import have_been_called
from expects import expect

from src.auction import AuctionMessageTranslator


class TestAuction:
    def test_notifies_auction_closed_when_close_message_received(self) -> None:
        message = "SOLVersion: 1.1; Event: CLOSE;"
        auction_listener = Spy()
        auction = AuctionMessageTranslator(auction_listener)

        auction.process_message(message)

        expect(auction_listener.auction_closed).to(have_been_called)

    def test_notifies_bid_details_when_price_message_received(self) -> None:
        message = "SOLVersion: 1.1; Event: PRICE; CurrentPrice: 192; Increment: 7; Bidder: Someone else;"

        # TODO: write a test for this message translation
