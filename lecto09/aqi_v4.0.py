"""
    _author=Cesare
    功能：AQI计算
    版本：2.0
    日期：03/05/2019
"""
import json
import csv
import os


def process_json_file(filepath):
    '''
    解析json文件
    :param filepath:
    :return:
    '''
    with open(filepath, 'r', encoding='utf-8') as f:
        city_list = json.load(f)
        print(city_list)

def process_csv_file(filepath):
    '''
    处理csv文件
    :param filepath:
    :return:
    '''
    with open(filepath, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))

def main():
    '''
    主函数
    :return:
    '''
    filepath = input('请输入文件名称：')

    filename, file_ext = os.path.splitext(filepath)
    if file_ext == '.json':
        '''json文件'''
        process_json_file(filepath)

    elif file_ext == '.csv':
        '''csv文件'''
        process_csv_file(filepath)
    else:
        print('暂不支持该文件格式')

    #
    # city_list = process_json_file(filepath)
    # city_list.sort(key=lambda city: city['aqi'])
    #
    # # 列名
    # lines = []
    # lines.append(list(city_list[0].keys()))
    #
    # for city in city_list:
    #     lines.append(list(city.values()))
    #
    # with open('aqi.csv', 'w', encoding='utf-8', newline='') as f:
    #     writer = csv.writer(f)
    #     for line in lines:
    #         writer.writerow(line)


if __name__ == '__main__':
    main()
