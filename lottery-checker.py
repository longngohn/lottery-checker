#!/usr/bin/env python

__doc__ = """
Yêu cầu:
Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ trang web tùy ý ví dụ ketqua.net
ketqua.vn hay tự google ra các trang khác.

Dạng của câu lệnh::

  ketqua.py [NUMBER1] [NUMBER2] [...]

Các thư viện:

- requests
- requests_html https://pp.pymi.vn/article/requests-bs4-requests-html/
hay beautifulsoup4 [tuỳ chọn]
- argparse hay sys.argv

Gợi ý:

- ``nargs`` https://docs.python.org/2/library/argparse.html
"""

import requests
import json
import sys
import log
from bs4 import BeautifulSoup
from typing import List

logger = log.get_logger(__name__)


def crawl_data():
    """
    Check lotto. Example:

    Input: 52 53
    Output: result = [(52, True), (53, False)]

    :param input_data: int
    :rtype list:
    """

    result = []

    r = requests.get("https://ketqua.vn/")
    tree = BeautifulSoup(markup=r.text)
    count = 0
    for td in tree.find_all("td"):
        try:
            for text in td.attrs["class"]:
                if "prize" in text:
                    result.append(td.text.strip("\n ")[-2:])
                    count += 1
        except KeyError:
            pass
    print(f"Total prize count: {count}")
    return result


def check_lotto(input_data, lottos):
    """
    Check lotto. Example:

    Input: 52 53
    Output: result = [(52, True), (53, False)]

    :param input_data: int
    :rtype list:
    """
    result = []
    for number in input_data:
        if str(number) in lottos:
            result.append((number, True))
        else:
            result.append((number, False))
    return result


def solve(input_data):
    """Function `solve` dùng để `test`, học viên không cần chỉnh sửa gì thêm
    Chỉ thay đổi lại tên function của mình bên dưới cho phù hợp

    Gía trị trả về của hàm `solve` và `your_function` là như nhau

    :param input_data: number
    :rtype list:
    """

    logger.debug("Find repos from username: %s", input_data)

    lottos = crawl_data()
    result = check_lotto(input_data, lottos)
    return result


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Add lotto")
    parser.add_argument("integers", metavar="N",
                        type=int, nargs="+", help="lotto")

    args = parser.parse_args()
    print(type(args.integers), args.integers)

    # sử dụng `sys.argv` hoặc `argparse` để gán gía trị yêu cầu vào biến `args`
    print(solve(args.integers))


if __name__ == "__main__":
    main()
