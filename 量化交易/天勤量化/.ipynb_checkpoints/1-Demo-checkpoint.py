#%%

from tqsdk import TqApi
# 创建API实例
api = TqApi()
# 获得上期所 cu2001 的行情引用，当行情有变化时 quote 中的字段会对应更新
quote = api.get_quote("SHFE.cu2001")
while True:
    # 调用 wait_update 等待业务信息发生变化，例如: 行情发生变化, 委托单状态变化, 发生成交等等
    api.wait_update()
    # 每当业务信息有变化时就输出 cu2001 的最新行情时间和最新价
    # 注意：其他合约的行情的更新也会触发业务信息变化，因此这里可能会将同一笔行情输出多次
    print(quote.datetime, quote.last_price)