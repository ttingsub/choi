#p.72 리스트 자료형
# 배열(array) - 시퀀스
# 빈 리스트
# 빈 리스트 <-- mutable 변겨 ㅇ가능한 데이터 타입
a = []
b = [1,2,3,'AA','BB',['Life','is','egg']]
print('AA' in b)
# list() - 리스트 타입으로 캐스팅(casting) <-->형변환

#1. 인덱싱(index) - 값을 가리키는
# index 0 1 2 3 4
str1 = '안녕하세요'
print(str1[0])
print(str1[1])
#print(b[5][0] + b[0])

# 2. 슬라이싱(p.75) : .slice() <-->[시작:끝값:단계]
a = [1,2,3,4,5]
b = [4,5,6]
print(a+b)
print(b*3)
#>>>: 명령 프롬프트 (CLI)
#print(a[2:])

empty_list = []
for i in range(10):
    empty_list.append(i**2)
    print(empty_list)
#리스트의 수정
empty_list[0]='감'
empty_list[-1]=100
print('------수정된 리스트의 값------')
print(empty_list)

'''
1.del
2. .remove()
3. .pop()
'''
#리스트의 맨 마지막 요소를 돌려주고, 그 요소는 삭제한다.
empty_list.pop()
#.pop(x) : x번째 요소를 돌려주고 그 요소는 삭제한다.
#empty_list.remove(1)
print(empty_list)

'''
git init 로컬 저장소 생성
git status 이력관리 상태를 확인
git add. 모든파일폴더 이력관리 시작
git add filename.foramt 지정관리 파일 폴더 이력관리 시작
git commit -m "commit msg-메세지" 변경을 승인
'''