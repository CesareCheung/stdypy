"""
    _author=Cesare
    功能：AQI计算
    版本：2.0
    日期：03/05/2019
"""
import json
import csv

def process_json_file(filepath):
    '''
    解析json文件
    :param filepath:
    :return:
    '''
    with open(filepath,'r',encoding='utf-8') as f:
        city_list=json.load(f)
    return city_list


def main():
    '''
    主函数
    :return:
    '''
    filepath= input('请输入json文件名称：')
    city_list=process_json_file(filepath)
    city_list.sort(key=lambda city:city['aqi'])

    # 列名
    lines=[]
    lines.append(list(city_list[0].keys()))

    for city in city_list:
        lines.append(list(city.values()))

    with open('aqi.csv','w',encoding='utf-8',newline='') as f:
        writer=csv.writer(f)
        for line in lines:
            writer.writerow(line)

    f.close()

if __name__ == '__main__':
    main()