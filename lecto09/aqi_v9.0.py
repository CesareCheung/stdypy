"""
    _author=Cesare
    功能：获取所有城市AQI
    版本：7.0
    日期：03/05/2019
"""
import pandas as pd


def main():
    '''
    主函数
    :return:
    '''
    aqi_data = pd.read_csv("china_city_aqi.csv")
    # print(aqi_data.head(5))  # 查看前5行,数据预览
    # print(aqi_data['AQI'])
    # print(aqi_data[['City','AQI']])   #多列数据，放入列表
    print('基本信息：')
    print(aqi_data.info())  # 基本信息
    print("数据预览：")
    print(aqi_data.head(5))

    # 基本统计

    print('AQI最大值：', aqi_data['AQI'].max())
    print('AQI最小值：', aqi_data['AQI'].min())
    print('AQI均值：', aqi_data['AQI'].mean())

    # 空气质量最好的10个城市
    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好的10个城市：')
    print(top10_cities)

    # 空气质量最差的10个城市
    # bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)
    bottom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('空气质量最差的10个城市：')
    print(bottom10_cities)

    # 保存csv文件

    top10_cities.to_csv('top10_cites.csv', index=False, encoding='utf-8')

    bottom10_cities.to_csv('bottom10_cities.csv', index=False, encoding='utf-8')


if __name__ == '__main__':
    main()
