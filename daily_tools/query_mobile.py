# coding=utf-8
import requests

from bs4 import BeautifulSoup


def query_mobile_with_ip138(mobile):
    """
    :param mobile: mobile number,should be
    :return: True/False: success or failed;
             ISP_ID: 1:移动, 2:联通, 3: 电信
             PROVINCE_ID：
    """
    try:
        mobile_str = str(mobile)
    except:
        return False, 0, 0

    if not mobile_str:
        return False, 0, 0
    url = 'http://www.ip138.com:8080/search.asp?mobile={}&action=mobile'.format(mobile_str)
    resp = requests.get(url)
    resp.encoding = 'gb2312'
    content = resp.text.strip()

    soup = BeautifulSoup(content, 'html.parser')
    data = soup.find_all('table')[1].find_all('tr')
    location_info = data[2].find_all('td')[1].text.strip()
    province_name, city_name = location_info.split()

    isp_str = data[3].find_all('td')[1].text
    isp_name = [u'移动', u'联通', u'电信']

    # 判断isp_str里面是否含有 移动，联通，电信关键字，如果只有一个则确定运营商，如果多个抛出异常
    isp_possible = [i + 1 for i, v in enumerate(map(lambda x: x in isp_str, isp_name)) if v]
    if len(isp_possible) != 1:
        raise Exception

    isp = isp_possible[0]

    return True, isp, province_name, city_name