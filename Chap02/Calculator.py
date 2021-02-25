# 모듈로 사용할 함수 정의
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

# python Calculator로 직접 이 파일을 실행했을 때는 __name__ == "__main__"이 참이 되어 if문 다음 문장이 수행된다. -> __name__ == __main__
# 반대로 다른 파일에서 이 모듈을 불러서 사용할 때는 __name__ == "__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다. -> __name__ == Calcuator
if __name__ == "__main__":
    print(add(1, 4))
    print(subtract(4, 2))

