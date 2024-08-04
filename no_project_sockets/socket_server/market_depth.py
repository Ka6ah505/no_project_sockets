import operator
from collections import defaultdict

class MarketDepth():

    def __init__(self, data=None) -> None:
        self.bid = defaultdict(float)
        self.ask = defaultdict(float)
        for key, value in data.items():
            if value < 0:
                self.ask[key] = -value
            else:
                self.bid[key] = value

    def max_volume_ask(self):
        a = max(self.ask.items(), key=operator.itemgetter(1))[0]
        return {a: self.ask.get(a)}
    
    def max_volume_bid(self):
        key = max(self.bid, key=lambda x: self.bid[x])
        return {key: self.bid.get(key)}

    def __str__(self) -> str:
        res = "======\n"
        for key, val in self.bid.items():
            res += f'{key}: {val}\n'
        
        res += "-------\n"
        for key, val in self.ask.items():
            res += f'{key}: {val}\n'
        res += "======"
        return res
