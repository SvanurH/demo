import requests
import json
import time
import random


class Spider:

    def __init__(self):
        cookie = "SECKEY_ABVK=wQ7p79aUwKNaUa533rPglgF0TE9+wdqG5/7r487VOPA%3D; BMAP_SECKEY=F6CKONr3LSc9Lg5HA4vX8FNp-QvMB_RaHxQFZCxTLA--NZFjX6jmdhRac6uSHS2R-ULafYO8-xjoaZF3H_Eu4mvPuj-oDEtUNR9sA-tWSFjJhc1iQXGWbsGDbEQN7Q1SHuCPzeybrNJT4pbvX3O8Aq2SE-0ms0rL_F6-uSvn-7vJISDW1Ey9m7-gATqzTWP9; QN1=00007f002eb4481be438fb17; QN71=MTEyLjUzLjc5LjExOua1juWNlzox; QN300=link.zhihu.com; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=V3b9uwm1tkJLHElQnEoVCKZMf4qW3cpt; _i=VInJOvrefHAwSN1qYTcfx2zUBjcq; QN57=16659882367210.4659870198755234; QN269=339474104DE511ED9817FA163EC7A7C8; Hm_lvt_15577700f8ecddb1a927813c81166ade=1665988237; fid=a97dd24b-3dac-4c4e-9bfd-9cea4eb68530; QN67=11869; _vi=bCOyy_hLD3hPfzqw2_psu6YVxCYxg60bm7VxiZ1FrlXbpDE9rdZynHMXSUfOPUQlviZVC5Wsvk5H1ZMRjSJKfPjv1uvrjTr7WuSjevy9nxPIpSDmFCqazxLbZKh9BK3lc9AZ827fZ3i_Cm0NxFwm6buk2g5KusukwqR1HHXC1sSY; ariaDefaultTheme=null; QN63=%E7%83%AD%E9%97%A8%E6%99%AF%E7%82%B9%7C%E5%8C%97%E4%BA%AC; QN267=01760818849781eee9e; QN58=1665988236720%7C1665989692095%7C5; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1665989692; QN271=5004f41d-a378-482a-be04-dff6a1d95c5c; JSESSIONID=14FB70A95DB77E81966F1858E6363D01; __qt=v1%7CVTJGc2RHVmtYMSswZ0RuZmFRMnRST1NIVkhjTnlmZlBrV0N3UGNuc0xaRHNLR3A4MGsvRFIzT0NpR0FzbjdEU3FiVy9kWnNwMDBmeDdxaThtaUlEUHgyS1c2NjR5T1RBRXlnNVA1UlpHQUZ0TmdHZXBDOFVEcEpXWGx2cmU1WWFZL0V1T05ndTcxS1lJUTNhMUhZdHg0YmpsY2JmTytlZk9mWUR2VGZZRDFVPQ%3D%3D%7C1665990483842%7CVTJGc2RHVmtYMTgzV2NSQ2EyVHRhQlh5TTlCNWFrME9KaGRzV2ZHSnA0R1IzcVZNc3BLVWl0dktBY2VkTmFweWk4TlBzU2t2QkQyRkJjM2g2elBQY0E9PQ%3D%3D%7CVTJGc2RHVmtYMStxWmZXL01EMVFUcnN6eGZWTFM3VmN1czRHSWNiSU9CSkZnM3dyV1ozL205UzR2NTBlT1lBbGlrNEtxRS9vL3hnUlp2R3NvTlF2ZTJTbkNjQTRhWXBlQ3ZJK0RHM1FZdjRibzFOVlVwUEpOZGw3bVFXSUlJbHZwK2ZtM0pqeG9GanJjRXJEWmtoNTl3WXRXaVVzUU03K2dXNEUyS3V0V3BhQXBBbm1MTTNPbHdOZk5TaGR3N0NPSkhTTk9SeXpOOW9FUmVNWWxBUUxmS0dMRDMybEpOenRQY21HeEJjODNCd1F4TVBpRDVoTWo1aXY3SWwxekFOdG5IbDdUNzhwVzR0Wm9JUmtDdnpMcUljYW5MaDJrbUZVdVZvMC90V0Vwd3Q0V0JBQjBuV25PdHk3Z1NQNm1BNjBnUXdvZmdhbEtiekVrc1ljRHdsR21Sd0N3WjJ6T01DSmpwR21iVy9uTDQ2OEVuNm1WNFZ0UVIrbVViZ09OSkhYMER3dHpZNzk3TFBoZ3poclEzc2srdFNHQ3AyV09pV21NajBUMzVpeFlQalE2VkVERDZhSnFqa0hkamh6aDhvaENLNlVINGl5aWMvcERFeDBCMGJOZXVPZEZSZVp4SFRhSnI3aldmSnNZVlVYRjBvUjV3OEw2Mk1mdVM5cEtHMXJuaWJ5ZndJeWltK0ozTFp3UnNKcUVacFNuY2RlWVp0OEh5OWFMVkpJMzM3VGlrK01RUWI5S1FUbjJwU1VPVG1XaDNSb0JRUW5uOUJ1V3ZGamxmeW0yN0VsMUlFRjZmSUNjSCtwOEo3dGgxYU9vYUpZQ0lLV09oV1o4Rnh4bXBpNTN1dC9EcXJiZS94b0dFaUdSaXVIOEJQM3loVThIVElxbkIyTi9nSCtqTWpPMHc0ZUt3UEZZdFZ5MG9wQU9Xb1poUWlCOGFoSkxaTnR5VC9MMnFrdWk0ZVIxb3NXQ2pReG5HWlB1aGw2Y1Njak5KWXczZDN4MnI1Z3dVSnA4MXhUeExmVjdVVHB1eEV2VGJQZGhYRm1IZm50bnBSTm9KWTN0MUt4c1BCNk5LT0hzVmszWCs3YnFhbG5yamhRSDQ5eQ%3D%3D"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            "cookie": cookie
        }
        self.proxies = {}
        self.num = 0

    def get_city_info(self, city, page):
        print("=" * 20)
        print(f"[*]开始爬取{city}的第{page}页")
        url = f"https://piao.qunar.com/ticket/list.json?keyword={city}&region=&from=mpl_search_suggest&sort=pp&page={page}"
        res = requests.get(url, headers=self.header, proxies=self.proxies)
        print("-" * 20)
        print(f"[+]爬取成功--{city}-{page}")
        print('-' * 20)
        if 'ret=false' in res.text:
            print(res.text)
            print("[-]ip被封")
            raise ZeroDivisionError("ip error")
        return res.json()

    def get_data(self, result):
        print('-' * 20)
        print("[*]正在处理城市数据")
        for data in result['data']['sightList']:
            address = data['address']
            try:
                star = data['star']
            except KeyError:
                star = ""
            try:
                score = data['score']
            except KeyError:
                score = ""
            sightName = data['sightName']
            districts = data['districts']
            is_free = data['free']
            point = data['point']
            qunarPrice = data['qunarPrice']
            sightId = data['sightId']
            saleCount = data['saleCount']
            data = {
                "sightName": sightName,
                "saleCount": saleCount,
                "address": address,
                "start": star,
                "score": score,
                "districts": districts,
                "is_free": is_free,
                "point": point,
                "qunarPrice": qunarPrice,
                "sightId": sightId
            }
            print('[+]处理成功')
            yield data

    def get_comment(self, sightId):
        print("-" * 20)
        print("[*]正在爬取评论")
        print("-" * 20)
        comments = []
        for page in range(1, 10):
            url = f"https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId={sightId}&index=1&page={page}&pageSize=10&tagType=0"
            result = requests.get(url, headers=self.header, proxies=self.proxies)
            print(self.proxies)
            if 'ret=false' in result.text:
                print("[-]ip被封")
                print(result.text)
                raise ZeroDivisionError("ip error")
            result = result.json()
            commentList = result['data']['commentList']
            for comment in commentList:
                comments.append({
                    "author": comment['author'],
                    "date": comment['date'],
                    "content": comment['content']
                })
        return comments

    def sava_data(self, data, content):
        print("-" * 20)
        print(f"[*]准备保存数据--{data['address']}")
        data["content"] = content
        with open("data.json", "a+", encoding='utf-8') as f:
            f.write(json.dumps(data) + ",")
        print(f"[+]数据保存成功--{data['address']}")
        print(f"[+]目前已经爬取了{self.num}个景点")
        self.num += 1
        print("=" * 20)

    def main(self):
        cities = ['山东', '北京', '上海', '天津', '重庆', '云南', '黑龙江', '内蒙古', '吉林',
                  '宁夏', '安徽', '山西', '四川', '广西', '新疆', '江苏', '江西',
                  '河北', '河南', '浙江', '海南', '湖北', '湖南', '澳门', '甘肃',
                  '福建', '西藏', '贵州', '辽宁', '陕西', '青海', '香港', '台湾']
        with open("data.json", "w+") as f:
            f.write("[")
        for city in cities:  # 遍历每一个省份
            for page in range(1, 20):  # 省份下10页景点
                try:
                    for data in self.get_data(self.get_city_info(city, page)):  # 获取每页的景点
                        comments = self.get_comment(data['sightId'])  # 获取每个景点的评论
                        self.sava_data(data, comments)
                        time.sleep(random.randint(1, 3))
                except ZeroDivisionError:
                    print("[*]ip被封,休眠中--5min")
                    time.sleep(300)
                    print("[+]休眠结束-再次尝试")
                    continue
                except Exception as e:
                    print("[-]未知错误，准备休眠跳过--5min" + str(e))
                    time.sleep(300)
        with open("data.json", "a+") as f:
            f.write("]")


if __name__ == '__main__':
    Spider().main()
