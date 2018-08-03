# 유저 프로그래머 라고 한다.

from functions import *
raw_data=get_data_from_excel('class_1.xlsx')
#내부 구현 모르고
#사용법(시그니처, 인터페이스)만 알면 함수 사용할 수 있는 것. -> 추상화 라고 한다.
# 프로그래밍의 처음이자 끝.
# 추상화의 끝은 OOP이다.

scores = list(raw_data.values())

avrg=get_avrg(scores)
var = get_var(scores,avrg)   #함수이름만 봐도 무슨 일을 하는지 알아야 한다.
std_dev = get_std_dev(var)

#50, 20

evaluate_class(avrg,50,std_dev,20)
