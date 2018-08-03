from openpyxl import load_workbook
import math

wb = load_workbook('class_1.xlsx')
ws = wb.active
g = ws.rows
raw_data={}
for name_cell,score_cell in g:
    raw_data[name_cell.value]= score_cell.value

scores = list(raw_data.values())


s=0.0
for score in scores:
    s+= score


avrg=s/len(scores)

s=0.0
for score in scores:
    s+= (score-avrg)**2

variance= round(s/len(scores),1)
std_dev = round(math.sqrt(variance),1)


print('평균:{}, 분산:{}, 표준편차:{}'.format(avrg,variance,std_dev))


if avrg < 50 and std_dev > 20:
    print('성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.')
elif avrg > 50 and std_dev > 20:
    print('성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!')
elif avrg < 50 and std_dev < 20:
    print('학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!')
elif avrg > 50 and std_dev < 20:
    print('성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.')