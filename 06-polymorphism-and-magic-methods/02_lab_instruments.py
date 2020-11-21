from abc import ABC, abstractmethod


class Instrument(ABC):
    @abstractmethod
    def play(self):
        type_name = type(self).__name__
        return f"playing the {type_name.lower()}"


def play_instrument(instrument: Instrument):
    return instrument.play()


class Guitar(Instrument):
    def play(self):
        print("playing the guitar")


guitar = Guitar()
play_instrument(guitar)
