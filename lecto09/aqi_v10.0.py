"""
    _author=Cesare
    功能：获取所有城市AQI
    版本：7.0
    日期：03/05/2019
"""
import pandas as pd

from matplotlib import pyplot as plt
# 解决中文输出乱码
plt.rcParams['font.sans-serif'] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False

def main():
    '''
    主函数
    :return:
    '''
    aqi_data=pd.read_csv("china_city_aqi.csv")
    # print(aqi_data.head(5))  # 查看前5行,数据预览
    # print(aqi_data['AQI'])
    # print(aqi_data[['City','AQI']])   #多列数据，放入列表
    print('基本信息：')
    print(aqi_data.info())    # 基本信息
    print("数据预览：")
    print(aqi_data.head(5))

    # 数据清洗
    # 只保留AQI>0的数据
    #
    # filter_condition=aqi_data['AQI']>0
    # clean_aqi_data=aqi_data[filter_condition]

    clean_aqi_data=aqi_data[aqi_data['AQI']>0]



    # 基本统计

    print('AQI最大值：',clean_aqi_data['AQI'].max())
    print('AQI最小值：',clean_aqi_data['AQI'].min())
    print('AQI均值：',clean_aqi_data['AQI'].mean())

    # 空气质量最好的10个城市
    top50_cities=clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar',x='City',y='AQI',title='空气质量最好的50个城市',
                      figsize=(20,10)
                      )
    plt.savefig('top50.png')
    plt.show()










if __name__ == '__main__':
    main()
