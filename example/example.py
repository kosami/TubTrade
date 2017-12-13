import alpha_live_trade
import time

if __name__ == "__main__":
    #alpha_live_trade.SetServer("ip or host", 58899)
   
    ret = alpha_live_trade.StartSDK("")
    ret = alpha_live_trade.LiveTradeLogin("132000015998", "152428", "465609", "stock_huatai")
    live_trade_id = ret.result
    
    # 查询账户状态
    # ret = alpha_live_trade.GetAccountState(live_trade_id)
    #     # # 返回结果
    #     #     ret_code    =>  0:成功
    #     #     state       =>  账户状态
    #     #         logining    正在登录
    #     #         login       登录成功
    #     #         logout      已登出
    #     #         failed      登录失败
    #     #         idle        空闲状态
    #     #     desc字       =>  状态补充说明




      
    # 查询账户余额
    # ret = alpha_live_trade.GetAccountBalance(live_trade_id)
    # total_value = ret.result.total_value
    # money_left  = ret.result.money_left    
    # print('{0:12f} {1:12f}'.format(total_value , money_left)) 
    

    #查询持仓
    # ret = alpha_live_trade.GetHoldingStock(live_trade_id)
    # print(ret.ret_code)

    # for item in ret.result:
    #     print(item)
        
    #查询账号信息
    # ret = alpha_live_trade.GetAccountInfo(live_trade_id,"ipo")    
    # print(ret.ret_code)
    # json_info = ret.result
    # print(json_info)

    #查询账号所有订单
    # ret = alpha_live_trade.GetAllOrder(live_trade_id)
    # print(ret.ret_code)
    # for i in ret.result:
    #     print(i)

    #实盘买入
    ret = alpha_live_trade.LiveTradeBuy(live_trade_id,'601313',51.0,100,orderType="limit")
        #   orderType:    limit  => 限价； 
        #                 market => 市价;
        #                     market.cns.0  对手方最优价格委托       深
        #                     market.cns.1  五档即时成交剩余转限价   沪
        #                     market.cns.2  本方最优价格委托         深
        #                     market.cns.3  即时成交剩余撤销         深
        #                     market.cns.4  五档即时成交剩余撤销     沪，深
        #                     market.cns.5  全额成交或撤销申报       深 
        #                 ipo    => 申购新股；
    print(ret.ret_code)
    orderID = ret.result
    print(orderID)

    #实盘卖出
    # ret = alpha_live_trade.LiveTradeSell(live_trade_id,'601313',52.0,100,orderType="limit")
    # orderID = ret.result

    #查询订单状态
    ret = alpha_live_trade.GetOrderState(live_trade_id,orderID)
        # 返回result字段:
        #     sid         =>  股票ID
        #     operation   =>  buy:买，sell:卖
        #     direction   =>  open:开仓，close:平仓
        #     price       =>  下单价格
        #     deal_quant  =>  成交数量
        #     deal_price  =>  成交价格
        #     state       =>  订单状态
        #         waiting     尚未发送到券商服务器
        #         sending     正在发送到券商服务器 
        #         pending     挂单成功但未成交
        #         failed      下单失败
        #         fulfilled   全部成交
        #         partfilled  部分成交
        #         canceling   正在撤单
        #         canceled    撤单成功
        #     desc        =>  状态说明
    print(ret.result.state , ret.result.desc)

    #取消订单
    ret = alpha_live_trade.CancelOrder(live_trade_id, orderID)


        
    #退出登录
    alpha_live_trade.LiveTradeLogout(live_trade_id)


