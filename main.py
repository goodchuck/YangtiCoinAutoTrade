
import pyupbit

access = "N9bYulRSveavOuObHwX1WxKMDHvYfROnjkEHOVEA"          # 본인 값으로 변경
secret = "1QFqv8RxRxX7NasM2l0GQW2oxQb0AWvyNAz69nEY"          # 본인 값으로 변경
test = pyupbit.Upbit(access, secret)

print(test.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(test.get_balance("KRW"))         # 보유 현금 조회

# print(test.get_current_price(["KRW-BTC", "KRW-XRP"]))
# print(test.buy_market_order("KRW-BTC", 10000))
print(test.get_balances())
print(test.get_order("KRW-BTC"))
print(test.get_order("KRW-BTC", state="done"))

