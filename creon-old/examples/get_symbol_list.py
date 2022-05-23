from creon.utils.creon_code_manager import (
    get_code_list_of_KOSPI,
    get_code_list_of_KOSDAQ,
)


def example():
    KOSPI = get_code_list_of_KOSPI()
    KOSDAQ = get_code_list_of_KOSDAQ()

    print("-----------------------------------")
    print("KOSPI 종목 리스트\n")
    for code in KOSPI:
        print(code)

    print("-----------------------------------")
    print("KOSDAQ 종목 리스트\n")
    for code in KOSDAQ:
        print(code)
