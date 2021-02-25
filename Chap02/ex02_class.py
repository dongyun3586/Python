# 클래스
class FishCakeMaker:
    # 생성자: 클래스가 생성될 때 호출됨.
    # 클래스에 포함된 것임을 표시하기 위해 항상 self 매개변수 사용
    def __init__(self, **kwargs):
        self._flavor = "팥"
        self._size = 10
        self._price = 100
        
        if "flavor" in kwargs:
            self._flavor = kwargs.get("flavor")
        if "size" in kwargs:
            self._size = kwargs.get("size")
        if "price" in kwargs:
            self._price = kwargs.get("price")

    # print() 재정의
    def __str__(self):
        return f"flaver={self._flavor}, size={self._size}, price={self._price}"

    def show_name(self):
        print("붕어빵 종류 {}".format(self._flavor))
        print("붕어빵 크기 {}".format(self._size))
        print("붕어빵 가격 {}".format(self._price))
        print("*" * 60)

# 객체 생성
fish1 = FishCakeMaker()  
fish2 = FishCakeMaker(size=20, price=1000)  
fish3 = FishCakeMaker(size=15, price=2000, flavor="초콜릿")  

fish1.show_name()
fish2.show_name()
fish3.show_name()

print(fish1)
print(fish2)
print(fish3)

