# 인자 전달 방식에 대한 분류

함수는 인자(argument) 전달 방식에 따라 크게 값에 의한 전달(call by value)과 참조에 의한 전달(call by reference)로 나누어집니다. 프로그래밍을 공부할 때 꼭 한 번은 거쳐야 하는 개념입니다. 

파이썬은 값에 의한 전달과 참조에 의한 전달 방식을 이용하지 않으므로  C++ 코드로 알아보겠습니다. 

이 코드를 이해하는 데 필요한 C++ 문법은 그때그때 소개하겠습니다.



## call by value

```c++
#include <iostream>
using namespace std;

void change_value(int x, int value) // #1
{
    x = value;                      // #2
    cout << "x : " << x << " in change_value" << endl;
}

int main(void)
{
    int x = 10;                     // #3
    change_value(x, 20);            // #4
    cout << "x : " << x << " in main" << endl;

    return 0;
}
```

```c++
x : 20 in change_value
x : 10 in main
```

change_value() 함수는 인자 x와 value를 받아 x에 value를 대입합니다. 

x에 10을 대입한 다음 change_value() 함수를 호출하면서 value 인자로 20을 전달했습니다. 따라서 x 값은 20으로 바뀔 듯 합니다. 

하지만 실행 결과를 보면 다른 값이 출력됩니다.

대체 어떻게 된 일일까요? 

이유는 함수에 x가 전달될 때 값에 의한 전달 방식(call by value)으로 전달되었기 때문입니다. 

이 문장이 어떤 의미인지 자세히 알아봅시다.