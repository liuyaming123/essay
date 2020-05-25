# -*- coding:utf-8 -*-


import asyncio
import aiohttp

from bs4 import BeautifulSoup
import re


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'kztoken=nJail6zJp6iXaJqWl3FnZGpvZJeT; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3FnZGpvYZiY%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3FnZGpvYZmU%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3FnZGpvYZmZ%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3FnZGpvYZqa%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3FnZGpvYZuW%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3FnZGpvYZyb%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3FnZGpvYpOW%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3FnZGpvYpWY%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3FnZGpvYpaU%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3FnZGpvZJeT%22%3B%7D; _ga=GA1.3.348911860.1582772329; _ga=GA1.2.348911860.1582772329; UtzD_f52b_saltkey=E9D5he9g; UtzD_f52b_lastvisit=1585059288; UtzD_f52b_auth=3897GcibZR1IvyvzEukXIuEtizAph4jg2UgBC2fYArsm55l6Pg3Soil2f%2B4T3ZPXLUEEmjR1fuudLYy%2FRyP3rqKOtp0; acw_tc=2f624a7015854968975406187e4ea88c277f92340789ca6ba7fcf79ba5054d; think_language=zh-CN; PHPSESSID=li8iq207kgpc55vkfeic8jvp80; _gid=GA1.2.1424451159.1585496898; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1583148945,1585496898; kztoken=nJail6zJp6iXaJqWl3FnZGpuapOa; his=a%3A2%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3FnZGpuaZyZ%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3FnZGpuapOa%22%3B%7D; hmap_show=true; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1585497133',
    'Host': 'db.yaozh.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
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
