from openpyxl import load_workbook
import math

def get_data_from_excel(filename):# 함수 이름만 봐도 어떤 작용을 하는지 알아야 한다.
    """
    get_data_from_excel(filename)->{'name1' : score1, 'name2' : score2, ...}
    엑셀 파일에서 raw_data를 가져옵니다.
    반환값은 key가 학생 이름 이고 value가 점수인 딕셔너리입니다.
    """
    raw_data={}
    wb = load_workbook(filename)
    ws = wb.active
    g = ws.rows
    for name_cell,score_cell in g:
        raw_data[name_cell.value]= score_cell.value
    return raw_data

def get_avrg(scores):
    """
    get_average(scores)->integer
    scores : list of score
    반환값은 평균입니다.
    """
    s=0.0
    for score in scores:
        s+= score
    return s/len(scores)

def get_var(scores,avrg):
    s=0.0
    for score in scores:
        s+= (score-avrg)**2
    return round(s/len(scores),1)

def get_std_dev(var):
    return round(math.sqrt(var),1)

def evaluate_class(avrg,total_avrg,std_dev,sd):
    """                       
    evaluate_class(avrg,total_avrg,std_dev,sd)->None       #시그니처 인터페이스 라고 한다?
    avrg: 반평균                                            
    total_avrg: 학년 전체 평균
    std_dev : 반 표준 편차
    sd : 원하는 표준 편차 기준
    """
    if avrg < total_avrg and std_dev > sd:
        print('성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.')
    elif avrg > total_avrg and std_dev > sd:
        print('성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!')
    elif avrg < total_avrg and std_dev < sd:
        print('학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!')
    elif avrg > total_avrg and std_dev < sd:
        print('성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.')
