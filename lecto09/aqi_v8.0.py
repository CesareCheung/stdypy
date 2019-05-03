"""
    _author=Cesare
    功能：获取所有城市AQI
    版本：7.0
    日期：03/05/2019
"""
import csv

import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    '''获取城市AQI'''
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url,timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list=soup.find_all('div',{'class':'span1'})

    city_aqi=[]
    for i in range(8):
        div_content=div_list[i]
        caption=div_content.find('div',{'class':"caption"}).text.strip()
        value=div_content.find('div',{'class':"value"}).text.strip()

        # city_aqi.append((caption,value))
        city_aqi.append(value)

    return city_aqi


def get_all_citys():
    '''获取所有城市AQI'''
    url='http://pm25.in/'
    city_list=[]
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    city_div=soup.find_all('div',{'class':'bottom'})[1]
    city_link_list=city_div.find_all('a')
    for city_link in city_link_list:
        city_name=city_link.text
        city_pinyin=city_link['href'][1:]
        city_list.append((city_name,city_pinyin))
    return city_list


def main():
    '''
    主函数
    :return:
    '''

    city_list=get_all_citys()

    #     print(city_name,city_aqi)
    header=['City','AQI','PM2.5/1h','CO/1h','NO/1h','O3/1h','O3/8h','SO2/1h']
    with open('china_city_aqi.csv','w',encoding='utf-8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)
        for i, city in enumerate(city_list):
            if (i+1)%10==0:
                print(f'已处理{i+1}条记录,共处理{len(city_list)}条记录')
            city_name=city[0]
            city_pinyin=city[1]
            city_aqi = get_city_aqi(city_pinyin)
            row=[city_name]+city_aqi
            writer.writerow(row)



if __name__ == '__main__':
    main()
