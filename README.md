# 프로젝트의 목적
* 주식의 일봉, 분봉 데이터를 이용하여 Machine Learning을 구상하고, 실제로 투자에 적용시켜 보기 위함
* 컴퓨터 성능의 제한으로 인해 colab을 이용한 multiprocessing을 최대한 활용하는 방안으로 구상

# 주로 사용된 기술
* 언어 : python
  * 멀티프로세싱
  * tensorflow
  * keras
  * pymysql
  * pandas
  * numpy
* DB : Mysql

# 업데이트 연혁

## 일자별 업데이트 파일
* 2021-05-16 : 주식_데이터_인공지능_학습_모델.ipynb
* 2021-05-19 : DB_데이터_크롤링.ipynb

## 주식_데이터_인공지능_학습_모델.ipynb
* 2021-05-16
  1. 구글 드라이브 Mount
  2. Framework 및 Library 추가
  3. Function 추가 (db_connecting_aws, db_connecting_local, my_pbar, input_making, data_making, minute_frame, day_frame)
  4. Multiprocessing 및 processbar 표시를 위한 공유 메모리 관리 (Manager) 추가
  5. 데이터 추출 추가 (input_data, train_data)
  6. 추출한 데이터를 인공지능에 맞게 일정하게 가공하는 과정 추가 (Framing)

## DB_데이터_크롤링.ipynb
* 2021-05-19
  1. 구글 드라이브 Mount
  2. Framework 및 Library 추가
  3. Function 추가 (my_pbar, db_connecting_aws, insert_data, ftbl_input
  4. Multiprocessing 및 processbar 표시를 위한 공유 메모리 관리 (Manager) 추가
  5. comtbl 및 ftbl 데이터 input 기능 추가
