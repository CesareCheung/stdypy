"""
    _author=Cesare
    功能：AQI计算
    版本：2.0
    日期：03/05/2019
"""
import json


def process_json_file(filepath):
    '''
    解析json文件
    :param filepath:
    :return:
    '''
    f=open(filepath,'r',encoding='utf-8')
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
    top5_list=city_list[:5]
    f=open('top5.json','w',encoding='utf-8')
    json.dump(top5_list,f,ensure_ascii=False)
    f.close()
    print(city_list)

if __name__ == '__main__':
    main()