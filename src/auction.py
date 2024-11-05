from src.auction_listener import AuctionEventListener


class AuctionMessageTranslator:
    def __init__(self, listener: AuctionEventListener):
        self.listener = listener

    def process_message(self, message: str):
        if "CLOSE" in message:
            self._close_auction()

        if "PRICE" in message:
            self._bid(message)

        # bug: should notify listener
        pass

    def _close_auction(self) -> None:
        pass
        # bug: should notify listener
        return

    def _bid(self, message) -> None:
        data = self._parse_message_data(message)

        current_price = int(data["CurrentPrice"])
        increment = int(data["Increment"])
        bidder = data["Bidder"]

        # bug: should notify listener
        return

    def _parse_message_data(self, message):
        data = {}
        for element in message.split(";"):
            if not element:
                continue
            pair = element.split(":")
            data[pair[0].strip()] = pair[1].strip()
        return data
