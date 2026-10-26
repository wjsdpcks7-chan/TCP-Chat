# TCP를 활용한 단체 채팅 프로그램 제작 과제
**소개**: 터미널에서 여러 client들이 서로 채팅하는 프로그램

**목적**: TCP 및 Thread를 활용한 숙지를 위한 과제

## 채팅 실행 방법
1. **저장소 받기**: `https://github.com/wjsdpcks7-chan/TCP-Chat.git`

2. **server.py 실행**: `python3 server.py'

3. **client.py 실행**: 다른 터미널 열고. `python3 client.py' -원하는 수만큼'

4. **닉네임 설정 후 채팅 시작**

## 통신 규칙
- 첫 입력을 닉네임으로 받고 나머지 입력은 채팅 메세지로 구분
- encode('utf-8), decode('utf-8')

