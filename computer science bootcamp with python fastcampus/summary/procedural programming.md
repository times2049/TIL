### 절차지향(procedural programming)

- 프로그래밍 패러다임의 한 종류. 
- 패러다임: 어떤 사물을 바라보는 사고의 틀이나 체계. 
- 프로그래밍 패러다임: 프로그래밍을 어떻게 바라볼 것인지, 어떻게 프로그래밍할 것인지에 대한 인식 혹은 체계. 
- 절차를 의미하는 프로시저(procedure)는 서브 루틴, 메서드,그리고 **함수**라고도 불립니다. 
- 함수(procedure)는 입력을 받아 일련의 연산 과정을 거쳐 출력을 내보냅니다. 
  - 한 번 정의해 두면 어디서든 다시 호출해 사용할 수 있다. 
  - 이름만 봐도 이 함수가 어떤 일을 하는지 쉽게 알 수 있습니다. 
  - 사용하는 사람은 함수의 내부 구현은 알 필요 없이 사용법(인터페이스)만 익혀 사용하면 됩니다. 
  - 긴 코드를 기능별로 나누어 함수로 정의하고, 함수 호출을 사용해 코드를 작성하면 다른 프로그래머도 쉽게 프로그램을 이해하고 유지·보수할 수 있습니다.
- 절차 지향 프로그래밍: “이 프로그램은 어떤 일을 하는가?”에 대한 질문에 쉽게 답할 수 있도록 함수(프로시저)를 사용해 프로그래밍하기. 



TIP: 파일을 찾지 못할 때

파이썬의 현재 작업 디렉터리에 파일이 없다면 다음과 같은 오류가 발생합니다.

FileNotFoundError: [Errno 2] No such file or directory: 'exam.xlsx'

이때는 두 가지 방법으로 해결할 수 있습니다. 



1) 파이썬의 현재 작업 디렉터리를 확인합니다.

```python
>>> import os
>>> os.getcwd()
'C:\Users\User'
```

getcwd( ) 메서드를 통해 현재 작업 디렉터리를 확인합니다. 이 디렉터리에 파일을 복사해서 넣으면 됩니다.



2) os 모듈의 chdir( ) 메서드를 이용합니다. 

```python
>>> os.chdir('C:\Users\User\Desktop')
```

파일이 어느 디렉터리에 있는지 확인한 후 해당 디렉터리를 현재 작업 디렉터리로 만들면 됩니다.



TIP: 발생자(generator)는 반복자(iterator)의 일종으로 next( ) 함수를 호출할 때마다 데이터를 차례대로 반환합니다. 모든 데이터가 반환되면 StopIteration 오류가 발생합니다. 

TIP: 딕셔너리 컴프리헨션

기존에 있던 데이터에서 딕셔너리를 생성할 때 유용합니다. 

```python
>>> tu_li = [('a', 97), ('b', 98), ('c', 99), ('d', 100)]          #1
>>> dic = {k : v for k, v in tu_li}                                #2
>>> dic
{'a': 97, 'b': 98, 'c': 99, 'd': 100}
```



1) 함수를 전혀 사용하지 않고 코드를 작성. 

```python
import openpyxl
import math
# 학년 전체 학생의 평균: 50점

raw_data = {}
wb = openpyxl.load_workbook('class_2_3.xlsx')
ws = wb.active
g = ws.rows
for name, score in g:
    raw_data[name.value] = score.value

scores = list(raw_data.values())

s = 0
for score in scores:
    s += score

avrg = round(s/len(scores), 1)

s= 0
for score in scores:
    s += (score - avrg) ** 2

variance = round(s/len(scores), 1)

std_dev = round(math.sqrt(variance),1)

print("평균: {0}, 분산: {1}, 표준편차: {2}".format(
    avrg, variance, std_dev))

if avrg <50 and std_dev >20:
    print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
elif avrg > 50 and std_dev >20:
    print("성적은 평균 이상이지만 학생들이 실력 차이가 크다. 주의 요망!")
elif avrg < 50 and std_dev <20:
    print("학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!")
elif avrg > 50 and std_dev <20:
    print("성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.")
```

이 프로그램을 절차 지향으로 바꿔 보겠습니다.



functions.py

```python
import openpyxl
import math

def get_data_from_excel(filename):
    '''
    get_data_from_excel(filename) -> {'name1' : 'score1', 'name2' : 'score2', ...}
    엑셀 파일에서 데이터를 가져옵니다
    반환값은 key가 학생 이름이고 value가 점수인 딕셔너리입니다
    '''
    dic = {}
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    g = ws.rows

    for name, score in g:
        dic[name.value] = score.value
        
    return dic
    
def average(scores):
    s = 0
    for score in scores:
        s += score
    return round(s/len(scores), 1)

def variance(scores, avrg):
    s= 0
    for score in scores:
        s += (score - avrg) ** 2
    return round(s/len(scores), 1)

def std_dev(variance):
    return round(math.sqrt(variance),1)
    
def evaluateClass(avrg, total_avrg, std_dev, sd):
    '''
    evaluateClass(avrg, total_avrg, std_dev, sd) -> None
    avrg: 반 성적 평균
    total_avrg: 학년 전체 성적 평균
    std_dev: 반의 표준편차
    sd: 원하는 표준편차 기준
    '''

    if avrg <total_avrg and std_dev >sd:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avrg > total_avrg and std_dev >sd:
        print("성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!")
    elif avrg < total_avrg and std_dev <sd:
        print("학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!")
    elif avrg > total_avrg and std_dev <sd:
        print("성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.")
```



절차 지향의 특징과 장점

- \#1부터 #5까지 함수 이름만 봐도 이 프로그램이 무슨 일을 하는지 알 수 있습니다. 
- 다른 프로그래머가 봐도 프로그램의 실행 흐름을 매우 쉽게 파악할 수 있습니다. 
- 인터페이스만 알면 필요한 함수를 가져다 쓰면 되므로 다른 프로그램도 쉽게 작성할 수 있습니다.



main.py

```python
from functions import *

# 학년 전체 학생의 평균 : 50점

if __name__ = = "__main__":
    raw_data = get_data_from_excel('class_2_3.xlsx') #1
    scores = list(raw_data.values())

    avrg = average(scores)                           #2
    variance = variance(scores, avrg)                #3
    standard_deviation = std_dev(variance)           #4

    print("평균: {0}, 분산: {1}, 표준편차: {2}".format(
        avrg, variance, standard_deviation))
    evaluateClass(avrg, 50, standard_deviation, 20)  #5
```

