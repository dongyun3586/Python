#region 매개 변수가 없는 생성자 
class Calculator1:
    # 생성자: 클래스가 생성될 때 호출됨.
    def __init__(self):     # 클래스에 포함된 것임을 표시하기 위해 항상 self 매개변수 사용
        self.result = 0     

# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다. 
# 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self를 사용한 것인데 self말고 다른 이름을 사용해도 된다.
    def add(self, num):     # 첫 번째 매개변수 self에는 add메서드를 호출한 객체 cal1, cal2가 자동으로 전달된다.
        self.result += num  
        return self.result
# ※ 메서드의 첫 번째 매개변수 self를 명시적으로 구현하는 것은 파이썬만의 독특한 특징이다. 

cal1 = Calculator1()
cal2 = Calculator1()

print(cal1.add(1))  # 1
print(cal1.add(2))  # 3
print(cal2.add(3))  # 3
print(cal2.add(4))  # 7
#endregion

#region 매개 변수가 있는 생성자
class Calculator2:
    def __init__(self, operator):
        self.operator = operator
         
    def calc(self, *args):
        self.result = 0             # 메서드를 호출한 객체에 result 변수가 생성되고 0이 저장된다. ※ 객체에 생성되는 객체만의 변수를 객체변수라고 부른다.
        if self.operator == 'sum':
            for i in args:
                self.result += i
        elif self.operator == 'mul':
            self.result = 1
            for i in args:
                self.result *= i
        return self.result

cal3 = Calculator2('sum') 
print(cal3.calc(1,2,3,4,5))     # 15
print(cal3.result)              # 15

cal4 = Calculator2('mul')
print(cal4.calc(1,2,3,4,5))     # 120
print(cal4.result)              # 120
#endregion

#region 사칙연수 클래스 
class Calculator3:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

calc = Calculator3(5, 10)
print(calc.add())           # 15
print(calc.subtract())      # -5
print(calc.multiply())      # 50
print(calc.divide())        # 0.5
#endregion

#region 상속

class ExtendedCalc(Calculator3):
    def pow(self):
        return self.num1 ** self.num2

calc = ExtendedCalc(4, 2)
print(calc.add())           # 6
print(calc.subtract())      # 2
print(calc.multiply())      # 8
print(calc.divide())        # 2.0
print(calc.pow())           # 16

#endregion

#region 메서드 오버라이딩
class SafeCalc(Calculator3):
    def divide(self):
        if(self.num2 == 0):
            return 0
        else:
            return self.num1 / self.num2
        
calc = SafeCalc(5, 0)
print(calc.divide())    # 0
#endregion

#region 클래스 변수
class Family:
    lastname = '이'

    def __init__(self, firstname):
        self.firstname = firstname

dongyun = Family('동윤')
print(f"{dongyun.lastname}{dongyun.firstname}") # 이동윤

jimin = Family('지민')
print(f"{jimin.lastname}{jimin.firstname}") # 이지민

# ※ id 함수는 객체의 주소를 돌려주는 파이썬 내장 함수이다.
# id 값이 모두 같으므로 Family.lastname, a.lastname, b.lastname은 모두 같은 메모리를 가리키고 있다.
print(id(Family.lastname), id(dongyun.lastname), id(jimin.lastname))    # 2589678882288 2589678882288 2589678882288

#endregion
