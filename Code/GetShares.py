from pickle import dump, load
from time import sleep

from path import Path as Pth

from Include.Announcer import speak_thread
from Include.Except import Except
from Include.Log import filename_exists, log
from Include.Requests import Requests


class Shares:
    def __init__(self):
        self.filename = Pth(".\\Bin\\Config\\Shares.txt")
        self.shares = []
        self.trader = Requests()
        self.alter = {}

    def init_shares_config(self):
        filename_exists(self.filename.parent)
        if not self.filename.exists():
            log(f'没有配置需要监控的股票，请配置')
            speak_thread(f'没有配置需要监控的股票，请配置')
            sleep(3600 * 24)
        self.shares = self.filename.lines()
        self.shares = [i.strip() for i in self.shares]

    def get_price(self, share):
        data = self.trader.get_last(share)
        if data:
            self.load()
            rate = (data['ask1']/data['prev_close'] - 1) * 100
            pre_rate = self.alter.get(share, 0)
            if rate >= 3 > pre_rate:
                log(f'{data["name"]}涨{rate}')
                rate = int(rate)
                speak_thread(f'{data["name"]}涨{rate}、涨{rate}')
            elif rate >= 5 > pre_rate:
                log(f'{data["name"]}涨{rate}')
                rate = int(rate)
                speak_thread(f'{data["name"]}涨{rate}、涨{rate}')
            elif rate >= 6 > pre_rate:
                log(f'{data["name"]}涨{rate}')
                rate = int(rate)
                speak_thread(f'{data["name"]}涨{rate}、涨{rate}')
            self.alter[share] = rate
            self.dump()

    def dump(self):
        with open('Bin\\Config\\alter.lc', 'wb') as f:
            dump(self.alter, f)

    def load(self):
        if Pth('Bin\\Config\\alter.lc').exists():
            with open('Bin\\Config\\alter.lc', 'rb') as f:
                self.alter = load(f)
        else:
            self.alter = {}

    def run(self):
        for share in self.shares:
            self.get_price(share)
            sleep(.2)

    def loop(self):
        self.welcome()
        self.init_shares_config()
        # while 1:
        #     self.run()
        #     sleep(0.2)
        sleep(3)
        while 1:
            try:
                self.run()
            except:
                log(Except())
            else:
                sleep(2)

    @staticmethod
    def welcome():
        log('博弈资产盯盘软件V1.0开始运行')
        speak_thread('博弈资产盯盘软件V1.0开始运行')
