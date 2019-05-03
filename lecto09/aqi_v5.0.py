"""
    _author=Cesare
    功能：AQI计算
    版本：5.0
    日期：03/05/2019
"""
import requests

def get_html_text(url):
    '''返回url文本'''
    r=requests.get(url,timeout=30)
    # r.status_code()
    return r.text


def main():
    '''
    主函数
    :return:
    '''
    city_pinyin=input('请输入城市拼音：')
    url='http://pm25.in/'+city_pinyin
    url_text=get_html_text(url)

    aqi_div='''    <div class="span12 data">
        <div class="span1">
          <div class="value">
            '''

    index=url_text.find(aqi_div)
    begin_index=index+len(aqi_div)
    end_index=begin_index+2
    aqi_val=url_text[begin_index:end_index]
    print(f"空气质量AQI为：{aqi_val}")





if __name__ == '__main__':
    main()
