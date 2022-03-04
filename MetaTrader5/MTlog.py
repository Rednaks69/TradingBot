###########################################################
# MetaTrader5 login with python
# author: Azer hasnaoui
#
###########################################################
#
# MetaTrader5 docummentation for python
# https://www.mql5.com/en/docs/integration/python_metatrader5

import MetaTrader5 as mt  # pip install MetaTrader5
# import pandas as pd  # pip install pandas
# import plotly.express as px  # pip install plotly
from datetime import datetime

# star the platform with initialization
mt.initialize()

# login to traade account with login()
#  make sure that trade server is enabled in ml5 client terminal
login = "login"   # int
pasword = 'paswor'  # chat
server = 'server name'  # char

mt.login(login, pasword, server)

# get account info
accout_info = mt.account_info()
print(accout_info)

# get specific account data
login_number = accout_info.login
balance = accout_info.balance
equity = accout_info.equity

print(login_number, balance, equity)
