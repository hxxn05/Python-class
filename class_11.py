# f = open("C:/미래모빌리티학과/DongHyunYOON/윤동현 Python/newfile2.txt",'x')
# f.close()


# f = open('ex_memo.txt','w') 
# students = ['깅지원', '좋아요', '구독', '알림설정'] 
# for student in students: 
#     msg = student 
#     f.write(msg+"\n") 
# f.close()


# file = open('hello.txt', 'w')
# file.write('Hello, world!')
# file.close()


# a: 쓰기 
# f = open('test.txt','w', encoding='UTF-8') 

# for i in range(4,10):
#     data = "%d 번째 줄입니다. \n"%i
#     f.write(data) 
# f.close()


# dict1 = {'hello' : 1, 'brother' : 2}
# file1 = open("Original.txt", "w") 

# str1 = repr(dict1)
# file1.write("dict1 = " + str1 + "\n")

# file1.close()

# test_file = open("DH1test.txt","w")

# a = 1 
# b = 2 
# test_file.write('%d + %d = %d' %(a, b, a+b))

# test_file.close
# from random import randint  #난수 생성 랜덤 int를 가져옴


# with open('DH2text.txt', 'w') as f:
#    f.write('이번주 로또 번호는 ->')   
#    for lotto in range(6):
#       f.write(str(randint(0,50)) +' , ') 

# f.close()

# lines = ['안녕하세요.\n', '유튜버\n', '깅지원입니다\n']

# with open('hellodh.txt', 'w') as file:
#     for msg in lines:
#         file.write(msg)
#         print(msg)
# file.close()

# # w: 쓰기
# f = open('ex_memoDH1.txt','w')
# students = ['깅지원', '혜원진', '취요남', '띱']
# for student in students:
#      msg = student
#      f.write(msg+"\n")
# f.close()

# f = open('ex_memoDH2.txt','w')
# students = ['핫소스', '눈물의 여왕', '캔위성', '언제 해']
# f.writelines('\n'.join(students))
# f.close()

# #파일 r 모드로 열기
# f = open('t2.txt', 'r')

 
# # read() 함수 이용해서 하나씩 읽어오기
# print('\n1. read()')
# print(f'위치 : {f.tell()}')
# s1 = f.read(1)
# print(s1)
 
# # readline() 함수 이용해서 한 라인씩 읽어오기
# print('\n2. readline()')
# print(f'위치 : {f.tell()}')
# f.seek(3)
# line = f.readline()
# line = line.strip() 
# s2 = f.readline()
# print(s2)
 
# # readlines() 함수 이용해서 모두 읽어오기
# print('\n3. readlines()')
# print(f'위치 : {f.tell()}')
 
# s3 = f.readlines()
# print(s3)

#파일 r 모드로 열기
# f = open('test.txt','r', encoding = 'UTF-8') 
# line = f.readline() #파일의 라인 끝에 줄 바꿈 (\n) 이 있을 경우 줄바꿈을 포함합니다.
# line = line.strip() #줄 바꿈 (\n) 제거
# print(line) #1번째 줄입니다.
# line = f.readline()
# line = line.strip() 
# print(line) #2번째 줄입니다.
# line = f.readline()
# line = line.strip() 
# print(line) #3번째 줄입니다.
# line = f.readline()
# line = line.strip()
# print(line) #4번째 줄입니다.

# f.close()

# readline() 함수 이용해서 한 라인씩 읽어오기
# print('\n2.readline()')
# print(f'위치 : {f.tell()}')

# s2 = f.readline()
# print(s2)

# s2 = f.readline()
# print(s2)\

f = open('test.txt', 'r', encoding='UTF-8')
line = f.readline()  # 파일의 라인 끝에 줄 바꿈 (\n) 이 있을 경우 줄 바꿈을 포함합니다.
line = line.strip()  # 줄 빠굼 (\n) 제거
print(line) # 1번째 줄입니다.
line = f.readline()
line = line.strip()
print(line) # 2번째 줄입니다.
line = f.readline()
line = line.strip()
print(line) # 3번째 줄입니다.
f.seek(0)
line = f.readline()
line = line.strip()
print(line) # 4번째 줄입니다.

f.close()






