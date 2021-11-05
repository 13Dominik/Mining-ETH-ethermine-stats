from datetime import datetime, timedelta, date

import requests
import json

from pycoingecko import CoinGeckoAPI

from setUp import miner_address

cg = CoinGeckoAPI()


class Miner:
    base_link = 'https://api.ethermine.org/miner/'
    price_eth = cg.get_price(ids='ethereum', vs_currencies='usd')['ethereum']['usd']

    def __init__(self, miner_address: str, *args, **kwargs):
        super(Miner, self).__init__(*args, **kwargs)
        self.miner_address = miner_address

    def get_unpaid_eth(self) -> float:
        """ Returns amount of unpaid_eth [ETH] """

        res = requests.get(self.base_link + self.miner_address + "/dashboard")
        file = json.loads(res.text)
        return round(int(str(file['data']['currentStatistics']['unpaid'])[:5]) / 100000000, 4)

    def get_sum_payouts(self) -> float:
        """ Returns sum of payouts [ETH] """

        res = requests.get(self.base_link + self.miner_address + "/payouts")
        file = json.loads(res.text)
        return round(sum([int(elem['amount']) / 10e17 for elem in file['data']]), 4)

    def get_daily_eth(self) -> float:
        """ Returns daily mined eth [ETH] """

        res = requests.get(self.base_link + self.miner_address + "/currentStats")
        file = json.loads(res.text)
        return round(float(str(file['data']['coinsPerMin'])[:6]) * 24 * 60 / 1000000, 5)

    def get_min_payment_threshold(self) -> float:
        """ Returns minimum payment threshold [ETH] """

        res = requests.get(self.base_link + self.miner_address + "/settings")
        file = json.loads(res.text)
        return file['data']['minPayout'] / 10e17

    def days_to_next_payout(self) -> int:
        """ Returns days to next payout [Days] """

        return int((self.get_min_payment_threshold() - self.get_unpaid_eth()) / (self.get_daily_eth()))

    def date_of_next_payout(self) -> date:
        """ Returns date of  next payout [Y-M-D] """
        d = datetime.now() + timedelta(days=self.days_to_next_payout())
        return date(d.year, d.month, d.day)


if __name__ == "__main__":
    m = Miner(miner_address)
    print(m.get_unpaid_eth())
    print(m.get_sum_payouts())
    print(m.get_daily_eth())
    print(m.get_min_payment_threshold())
    print(m.days_to_next_payout())
    print(m.date_of_next_payout())
