from time import sleep

from requests import get

from Include.Log import log
from Include.Url import url
import arrow as ar
from path import Path as Pth


class Requests:
    def __init__(self):
        self.url = ''
        self.data = {'code': '',
                     'time': '',
                     'name': '',
                     'last': 1.,
                     'rate': 9.99,
                     'volume': 1.,
                     'amount': 1.,
                     'open': 1.,
                     'high': 1.,
                     'low': 1.,
                     'prev_close': 1.,
                     'ask1': 1.,
                     'ask1v': 1.,
                     'ask2': 1.,
                     'ask2v': 1.,
                     'ask3': 1.,
                     'ask3v': 1.,
                     'ask4': 1.,
                     'ask4v': 1.,
                     'ask5': 1.,
                     'ask5v': 1.,
                     'bid1': 1.,
                     'bid1v': 1.,
                     'bid2': 1.,
                     'bid2v': 1.,
                     'bid3': 1.,
                     'bid3v': 1.,
                     'bid4': 1.,
                     'bid4v': 1.,
                     'bid5': 1.,
                     'bid5v': 1.}
        self.pre_time = ar.now()

    def parser_url(self):
        return eval(get(self.url).text[3:-1])

    @property
    def parser_data(self):
        data = self.parser_url()
        self.data['code'] = data['code']
        self.data['time'] = str(data['date']) + str(data['time'])
        if self.is_trading:
            data_t = []
            for i in data['snap']:
                if isinstance(i, list):
                    data_t.extend(i)
                else:
                    data_t.append(i)
            for key, values in zip(list(self.data.keys())[2:], data_t):
                self.data[key] = values
            return self.data
        else:
            return {}

    @property
    def is_trading(self):
        if ar.get(self.data['time'], 'YYYYMMDDHHmmss').replace(tzinfo=self.pre_time.tzinfo) > self.pre_time:
            self.pre_time = ar.now()
            self.data['time'] = self.pre_time.format('YYYY-MM-DD HH:mm:ss.SSS')
            return True
        else:
            self.waiting_trading_time()
            return False

    @staticmethod
    def waiting_trading_time():
        now_time = ar.now()
        if now_time.isoweekday() >= 6:
            target_time = now_time.shift(days=8 - now_time.isoweekday()).replace(hour=9, minute=30).floor('minute')
        elif now_time < now_time.replace(hour=9, minute=30).floor('minute'):
            target_time = now_time.replace(hour=9, minute=30).floor('minute')
        elif now_time.replace(hour=11, minute=30).floor('minute') < now_time < now_time.replace(hour=13).floor('hour'):
            target_time = now_time.replace(hour=13).floor('hour')
        elif now_time > now_time.replace(hour=15).floor('hour'):
            target_time = now_time.shift(days=1).replace(hour=9, minute=30).floor('minute')
        else:
            target_time = now_time
        if target_time > now_time:
            sleep_time = target_time.float_timestamp - now_time.float_timestamp
            log(f'当前不是开盘时间，重置shares.lc并等待{sleep_time}s，再行判断')
            Pth('Bin\\Config\\alter.lc').remove_p()
            sleep(sleep_time)

    def get_last(self, code):
        self.url = url(code)
        return self.parser_data
