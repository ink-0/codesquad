#단어하나, 정수 숫자 하나,문자구현 하나 입력 받음
word,cnt,type=map(str,input("영단어,정수,방향 공백 구분하여 입력:").split())
#문장 길이로 나눠 최소한의 문자 밀어내기 구현
cnt=int(cnt)
wordlen=len(word)
turn=abs(cnt)%wordlen
word=list(map(str,word))

#정수가 문자 길이의 배수라면 밀어내기 없이 그대로 출력
if turn==0:
    print('밀어낸 결과:',''.join(word))
#문자밀어내기 turn횟수만큼 문자 밀어내기
else:
    while turn!=0:
        if type.upper()=='L':
            if cnt<0:
                word.append(word.pop())  #오른쪽으로 밀어내기
            else:
                word.append(word.pop(0)) #왼쪽으로 밀어내기
        else:
            if cnt<0:
                word.append(word.pop(0))
            else:
                word.append(word.pop())
        turn-=1
    print('밀어낸 결과:',"".join(word)) #word 배열 함수 join 출력



