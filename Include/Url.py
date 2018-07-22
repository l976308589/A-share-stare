def url(code):
    if code.startswith('6'):
        return f'http://yunhq.sse.com.cn:32041/v1/sh1/snap/{code}?callback=hx&select=name%2Clast%2Cchg_rate%2Cvolume%2Camount%2Copen%2Chigh%2Clow%2Cprev_close%2Cask%2Cbid'
    return f'http://yunhq.sse.com.cn:32041/v1/sz1/snap/{code}?callback=hx&select=name%2Clast%2Cchg_rate%2Cvolume%2Camount%2Copen%2Chigh%2Clow%2Cprev_close%2Cask%2Cbid'