from abc import ABC, abstractmethod


class AuctionEventListener(ABC):
    @abstractmethod
    def auction_close(self) -> None:
        raise NotImplementedError
