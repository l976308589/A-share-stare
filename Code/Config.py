import sys

import easygui as eg
from Code.GetShares import Shares
from path import Path as Pth

from Include.Log import log, filename_exists


def run_my_config():
    while 1:
        button = eg.buttonbox(msg="请选择操作",
                              title="博弈资产自动盯盘V1.0",
                              choices=["盯盘", "配置", "退出"])
        if button == "盯盘":
            share = Shares()
            share.loop()
        elif button == "配置":
            config_file = eg.fileopenbox(msg="请选择需要监控的股票代码\n每行有且仅有一支股票",
                                         title="博弈资产自动盯盘V1.0")
            filename = Pth(".\\Bin\\Config\\Shares.txt")
            if config_file:
                filename_exists(filename.parent)
                Pth(config_file).copyfile(filename)
                shares = filename.text()
                log('配置完成')
                eg.msgbox(f'配置完成\n{shares}')
            else:
                log('未输入任何股票代码')
                eg.msgbox('未输入任何股票代码')
        else:
            sys.exit()
