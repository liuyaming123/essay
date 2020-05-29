# -*- coding:utf-8 -*-


import asyncio
import aiohttp

from bs4 import BeautifulSoup
import re
import random

user_agent = [
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
]

headers = {
    'User-Agent': random.choice(user_agent),

}
comp = re.compile('<[^>]+>')
conn = aiohttp.TCPConnector(ssl=False)  # 防止ssl报错


async def get_text(url):
    async with aiohttp.request('GET', url, headers=headers, connector=conn) as resp:
        print(resp.status)
        return await resp.text()


async def count(url):
    content = await get_text(url)
    soup = BeautifulSoup(content, 'lxml')

    lil = soup.find_all('th', class_='detail-table-th')
    lir = soup.find_all('span', class_='toFindImg')

    ls_key = [re.sub(comp, '', str(k)).strip() for k in lil]
    rs_value = [re.sub(comp, '', str(v)).strip() for v in lir]

    hospital = {}
    print(ls_key)
    for index in range(len(ls_key)):
        hospital[ls_key[index]] = rs_value[index]

    print(url, hospital)


def main():
    loop = asyncio.get_event_loop()
    tasks = [count('https://db.yaozh.com/hmap/%s.html' % num)
             for num in range(1, 10)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()
