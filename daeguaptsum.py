# 데이터 프레임
import pandas as pd
import numpy as np
import datetime

# 데이터 시각화 분석
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# 시각화 한글 문자
mpl.rc('font', family ='Malgun Gothic')
# 아파트단지 코드 수집
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random
import time
import requests
import json
import logging
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

driver = webdriver.Chrome()  
    
loc_code_list =  ["2720010200","2720010300","2720010200","2720010100","2729010100","2729010200","2729010400","2729010500","2729010600","2729010700","2729010800","2729010900","2729011000","2729011100","2729011200","2729011300","2729011400","2729011500","2729011600","2729011700","2729011800","2729011900","2729012000","2729012100","2729012200","2729012300","2729012400","2729012500","2726010100","2726010200","2726010300","2726010400","2726010500","2726010600","2726010700","2726010800","2726010900","2726011000","2726011100","2726011200","2726011300","2726011400","2726011500","2726011600","2726011700","2726011800","2726011900","2726012000","2726012200","2726012300","2726012400","2726012500","2726012600","2726012700","2714010100","2714010200","2714010300","2714010400","2714010500","2714010600","2714010700","2714010800","2714010900","2714011000","2714011100","2714011200","2714011300","2714011400","2714011500","2714011600","2714011700","2714011800","2714011900","2714012000","2714012100","2714012200","2714012300","2714012400","2714012500","2714012600","2714012700","2714012800","2714012900","2714013000","2714013100","2714013200","2714013300","2714013400","2714013500","2714013600","2714013700","2714013800","2714013900","2714014000","2714014100","2714014200","2714014300","2714014400","2714014500","2723010100","2723010200","2723010300","2723010400","2723010500","2723010600","2723010700","2723010800","2723010900","2723011000","2723011100","2723011200","2723011300","2723011400","2723011500","2723011600","2723011700","2723011800","2723011900","2723012000","2723012100","2723012200","2723012300","2723012400","2723012500","2723012600","2723012700","2723012800","2723012900","2723013000","2723013100","2717010100","2717010200","2717010300","2717010400","2717010500","2717010600","2717010700","2717010800","2717010900","2711010100","2711010200","2711010300","2711010400","2711010500","2711010600","2711010700","2711010800","2711010900","2711011000","2711011100","2711011200","2711011300","2711011400","2711011500","2711011600","2711011700","2711011800","2711011900","2711012000","2711012100","2711012200","2711012300","2711012400","2711012500","2711012600","2711012700","2711012800","2711012900","2711013000","2711013100","2711013200","2711013300","2711013400","2711013500","2711013600","2711013700","2711013800","2711013900","2711014000","2711014100","2711014200","2711014300","2711014400","2711014500","2711014600","2711014700","2711014800","2711014900","2711015000","2711015100","2711015200","2711015300","2711015400","2711015500","2711015600","2711015700","2771025000","2771025300","2771025600","2771025900","2771026200","2771026500","2771031000","2771033000","2771038000"]

apt_number_list = []
complexNo_list = []
complexName_list = []
cortarNo_list = []
realEstateTypeCode_list = []
realEstateTypeName_list = []
detailAddress_list = []
latitude_list = []
longitude_list = []
totalHouseholdCount_list = []
totalBuildingCount_list = []
highFloor_list = []
lowFloor_list = []
useApproveYmd_list = []
dealCount_list = []
leaseCount_list = []
rentCount_list = []
shortTermRentCount_list = []
cortarAddress_list = []


for loc_code in loc_code_list:
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    url = "https://new.land.naver.com/api/regions/complexes?cortarNo={}&realEstateType=APT%3AABYG%3AJGC&order".format(loc_code)
    time.sleep( random.uniform(1,3) )
    driver.get(url)

    apt_json_info = driver.find_element(By.XPATH, "/html/body/pre").text            
    apt_data = json.loads(apt_json_info)

    tmp = len(apt_data['complexList'])
    
    for number in range(len(apt_data['complexList'])):
        apt_number_list.append(number+1) 
        complexNo_list.append(apt_data['complexList'][number]['complexNo'])
        complexName_list.append(apt_data['complexList'][number]['complexName'])
        cortarNo_list.append(apt_data['complexList'][number]['cortarNo'])
        realEstateTypeCode_list.append(apt_data['complexList'][number]['realEstateTypeCode'])
        realEstateTypeName_list.append(apt_data['complexList'][number]['realEstateTypeName'])
        detailAddress_list.append(apt_data['complexList'][number]['detailAddress'])
        latitude_list.append(apt_data['complexList'][number]['latitude'])
        longitude_list.append(apt_data['complexList'][number]['longitude'])
        totalHouseholdCount_list.append(apt_data['complexList'][number]['totalHouseholdCount'])
        totalBuildingCount_list.append(apt_data['complexList'][number]['totalBuildingCount'])
        highFloor_list.append(apt_data['complexList'][number]['highFloor'])
        lowFloor_list.append(apt_data['complexList'][number]['lowFloor'])
        useApproveYmd_list.append(apt_data['complexList'][number]['useApproveYmd'])
        dealCount_list.append(apt_data['complexList'][number]['dealCount'])
        leaseCount_list.append(apt_data['complexList'][number]['leaseCount'])
        rentCount_list.append(apt_data['complexList'][number]['rentCount'])
        shortTermRentCount_list.append(apt_data['complexList'][number]['shortTermRentCount'])
        cortarAddress_list.append(apt_data['complexList'][number]['cortarAddress'])

df = pd.DataFrame(zip(apt_number_list, complexNo_list, complexName_list, cortarNo_list, realEstateTypeCode_list, realEstateTypeName_list, detailAddress_list, latitude_list, longitude_list, totalHouseholdCount_list, totalBuildingCount_list, highFloor_list, lowFloor_list, useApproveYmd_list, dealCount_list, leaseCount_list, rentCount_list, shortTermRentCount_list, cortarAddress_list), columns=('No', 'complexNo', '단지명', 'cortarNo', 'realEstateTypeCode', '아파트타입', '지번', '위도', '경도', '총세대수','동수', '최고층', '최저층', '준공일', '매매', '전세', '월세', '단기월세', '주소'))
#데이터 프레임 저장
# now = datetime.datetime.now() 
# df.to_csv('./매물통계{}.csv'.format(now.strftime('%Y%m%d')),encoding='utf-8-sig',index=False)

driver.quit()

df = df.loc[(df['주소'].str.contains('범어동'))]
df = df.loc[(df['단지명'].str.contains('두산위브더제니스'))]
df = df.groupby('단지명')['총세대수','매매','전세','월세'].sum()

# 그래프그리기
df.plot(kind='bar',figsize=(16,10))
plt.title("매물현황", fontsize=20)
plt.xlabel("단지명")
plt.ylabel("매물건수")
# plt.xlim([-1, 15])
plt.xticks(rotation= 75)
# plt.savefig("대구수성동 아파트 단지별세대수.png")
plt.show()