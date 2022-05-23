from creon.apis import code_manager as cm
from creon.models.enums.cpe_market_kind import CPE_MARKET_KIND

code = "A005930"  # 삼성전자

# print("get_code_list_of_KOSPI", len(cm.get_code_list_of_KOSPI()))
# print("get_code_list_of_KOSDAQ", len(cm.get_code_list_of_KOSDAQ()))
# print("get_name_by_code", cm.get_name_by_code(code))
# print("get_yesterday_close_price_by_code", cm.get_yesterday_close_price_by_code(code))
# print("get_industry_code_by_code", cm.get_industry_code_by_code(code))
# print("get_market_by_code", cm.get_market_by_code(code))
# print("get_status_by_code", cm.get_status_by_code(code))
# print("get_group_code_by_code", cm.get_group_code_by_code(code))
# print("get_section_by_code", cm.get_section_by_code(code))

print("----- FREEBOARD -----")
freeboard_stocks = cm.get_code_list_by_market_kind(CPE_MARKET_KIND.FREEBOARD)
for code in freeboard_stocks:
    print(code, cm.get_name_by_code(code))
print("---------------------")

print("------- KONEX -------")
konex_stocks = cm.get_code_list_by_market_kind(CPE_MARKET_KIND.KONEX)
for code in konex_stocks:
    print(code, cm.get_name_by_code(code))
print("---------------------")
