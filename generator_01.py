def generate_numbers_1(max_number : int):
    print("generate_numbers_1 함수 호출")
    numbers = []
    for i in range(1, max_number + 1):
        numbers.append(i)
    return numbers

# Generator 객체를 생성하는 함수
def generate_numbers_2(max_number = int):
    print("generate_numbers_2 함수 호출")
    for i in range(1, max_number + 1):
        yield i
        #yield : 함수 내에 yield 키워드를 실행 시 generator 객체를 만들어내는 코드이다.


numbers_1 = generate_numbers_1(10)
numbers_2 = generate_numbers_2(10)
print(numbers_1)
print(numbers_2)

gen1 = (i**2 for i in [1,2,3,4,5]) 

def make_numbers():
    for i in [1,2,3,4,5]:
        yield i

gen2 = make_numbers()