# -*- coding:utf-8 -*-

"""
常量

Author: HuangTao
Date:   2018/07/31
Update: None
"""


# 交易所名称
COINSUPER = "coinsuper"
BCOIN = "bcoin"
GBX = "gbx"
BITFINEX = "bitfinex"
BINANCE = "binance"
OKEX = "okex"  # OKEx现货
OKEX_FUTURE = "okex_future"  # OKEx交割合约
OKEX_SWAP = "okex_swap"  # OKEx永续合约
BITMEX = "bitmex"
HUOBI = "huobi"
HUOBI_FUTURE = "huobi_future"
OKCOIN = "okcoin"
COINBASE = "coinbase"
MXC = "mxc"
DERIBIT = "deribit"
KRAKEN = "kraken"
BITSTAMP = "bitstamp"
GEMINI = "gemini"
FOTA = "fota"
BIBOX = "bibox"

# 自定义
CUSTOM = "custom"


# 行情类型
MARKET_TYPE_ORDERBOOK = "orderbook"  # 订单薄
MARKET_TYPE_KLINE = "kline"  # K线
MARKET_TYPE_TICKER = "ticker"  # ticker
MARKET_TYPE_TRADE = "trade"  # trade


# 代理操作类型
AGENT_OPTION_AUTH = "auth"  # 账户授权
AGENT_OPTION_ASSET = "asset"  # 请求资产
AGENT_OPTION_CREATE_ORDER = "create_order"  # 创建订单
AGENT_OPTION_REVOKE_ORDER = "revoke_order"  # 撤销订单
AGENT_OPTION_ORDER_STATUS = "order_status"  # 查询订单状态
AGENT_OPTION_OPEN_ORDERS = "open_orders"  # 查询未完成订单
AGENT_OPTION_SUBSCRIBE = "subscribe"  # 订阅行情
AGENT_OPTION_UNSUBSCRIBE = "unsubscribe"  # 取消订阅行情
AGENT_OPTION_UPDATE = "update"  # 服务器推送更新


# 行情
AGENT_MSG_TYPE_MARKET           = "market"

AGENT_MSG_OPT_SUB_ORDERBOOK     = "subscribe.orderbook"     # 订阅 orderbook
AGENT_MSG_OPT_UNSUB_ORDERBOOK   = "unsubscribe.orderbook"   # 取消订阅 orderbook
AGENT_MSG_OPT_UPDATE_ORDERBOOK  = "update.orderbook"        # 更新推送 orderbook

AGENT_MSG_OPT_SUB_KLINE         = "subscribe.kline"         # 订阅 kline
AGENT_MSG_OPT_UNSUB_KLINE       = "unsubscribe.kline"       # 取消订阅 kline
AGENT_MSG_OPT_UPDATE_KLINE      = "update.kline"            # 更新推送 kline

AGENT_MSG_OPT_SUB_TRADE         = "subscribe.trade"         # 订阅 trade
AGENT_MSG_OPT_UNSUB_TRADE       = "unsubscribe.trade"       # 取消订阅 trade
AGENT_MSG_OPT_UPDATE_TRADE      = "update.trade"            # 更新推送 trade

AGENT_MSG_OPT_SUB_TICKER        = "subscribe.ticker"        # 订阅 ticker
AGENT_MSG_OPT_UNSUB_TICKER      = "unsubscribe.ticker"      # 取消订阅 ticker
AGENT_MSG_OPT_UPDATE_TICKER     = "update.ticker"           # 更新推送 ticker


# 交易
AGENT_MSG_TYPE_TRADE            = "trade"                   # 交易

AGENT_MSG_OPT_AUTH              = "auth"                    # 账户授权
AGENT_MSG_OPT_ASSET             = "asset"                   # 获取资产
AGENT_MSG_OPT_CREATE_OREDER     = "create_order"            # 创建订单
AGENT_MSG_OPT_REVOKE_ORDER      = "revoke_order"            # 撤销订单
AGENT_MSG_OPT_ORDER_STATUS      = "order_status"            # 查询订单状态
AGENT_MSG_OPT_OPEN_ORDERS       = "open_orders"             # 查询未完全成交订单号列表

AGENT_MSG_OPT_SUB_ASSET         = "subscribe.asset"         # 订阅 asset
AGENT_MSG_OPT_UNSUB_ASSET       = "unsubscribe.asset"       # 取消订阅 asset
AGENT_MSG_OPT_UPDATE_ASSET      = "update.asset"            # 更新推送 asset

AGENT_MSG_OPT_SUB_ORDER         = "subscribe.order"         # 订阅 order
AGENT_MSG_OPT_UNSUB_ORDER       = "unsubscribe.order"       # 取消订阅 order
AGENT_MSG_OPT_UPDATE_ORDER      = "update.order"            # 更新推送 order
