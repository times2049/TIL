문자와 문자열! 자주 접하는 만큼 중요합니다.

그런데 컴퓨터는 문자를 어떻게 표현할 수 있는 걸까요? 0과 1밖에 모르는데 말입니다.

'a' 라는 문자를 어떻게 메모리에 저장하는거죠?

설명에 앞서 몇가지 용어를 정리하겠습니다.



- 문자 집합(character set): 문자를 모아 둔것 ex) 라틴문자

- 문자 인코딩(character encoding): 문자 집합을 메모리에 저장하거나 통신할 때 사용하기 위해 부호화하는 방식. ex) 모스 부호

- 부호화된 문자 집합(Coded Character Set, CCS):문자와 문자에 매핑된 코드 포인트를 모아둔 집합.

  +) 코드 포인트(code point)? 

  컴퓨터에 문자를 인식시키려면 문자를 0과 1로 이루어진 2진수로 나타내야 합니다. 문자 하나에->정수 하나를 mapping해 두면 이 정수는 특정 문자를 표현하게 됩니다. 이렇게 mapping된 정수를 코드 포인트(code point)라고 합니다.

## ASCII, UNICODE

#### ASCII가 뭔가요?!

- American Standard Code for Information Interchange, 미국정보교환표준부호 
- 대표적인 문자 인코딩 방식 중 하나 입니다.
- 7 bit 로 표현. 따라서 문자를 총 128개 표현합니다. (0~127)
- 코드 포인트 수도 128개 라는 말이죠.
- 0~127인 정수(코드 포인트)에 128개의 문자가 매핑되어 있습니다.

ex)대문자 ‘A’는 10진수: 16진수: 0x41입니다. 

```python
>>> ch = 'A'
>>> bch = ch.encode()
>>> bch
b'A'
>>> bch[0]
65
```

### UNICODE 는 또 뭔데요?!

- ASCII에는 한글이 없습니다.
- 그런데 글로벌화 되면서 컴퓨터가 표현해야 하는 언어가 많아졌죠.
- 이때 나온 해결법이 7bit 표현을 16bit 표현으로 확장하기였어요.
- 16bit로 확장시 65,536개 문자를 표현합니다.
- 이 수 각각에 문자 하나씩 대응한 새로운 표가 바로 UNICODE입니다.
- 0x0000부터 0x007F 즉, 기존 아스키코드 앞에 0으로 채워진 8비트를 붙인 것)까지는 아스키 코드 방식 그대로 유지합니다.

+)사실 이러한 테이블이 16개 더 있습니다. 방금 설명한 테이블을 기본 다국어 평면(Basic Multilingual Plane, BMP) 이라 합니다.

파이썬에서도 유니코드 문자를 확인할 수 있습니다.

```python
>>> '\uAC00'
'가'
```



### UNICODE ENCODING 방식

이번에도 용어를 몇 가지 정리하고 시작하겠습니다.

- 코드 유닛(code unit): 코드 포인트를 특정한 방법으로 인코딩했을 때 변환되어 얻어지는 비트의 나열.
- 문자 인코딩 방식(Character Encoding Scheme, CES): 코드 유닛을 옥텟으로 나열하여 변환하는 방법. 
  - 옥텟(octet): 데이터의 단위로 8비트를 의미. 

+)1byte를 8bit로 표현하자고 약속한지는 얼마 안되었습니다. 따라서 옥텟이라는 용어가 따로 존재. 



유니코드는 모든 문자를 표현하려면 3byte가 필요합니다. (기본 다국어 평면을 포함, 평면이 17 개 있으므로 ) 

단순히 code unit 크기를 3byte로 해서 코드 포인트를 저장해도 되지만 좀더 효율적인 방식이 고안되었습니다.

대표적인 유니코드 인코딩 방식 UTF-8, UTF-16, UTF-32를 다루겠습니다.



- encode( ) :파이썬에서 문자를 유니코드 인코딩 방식에 따라 코드 유닛을 나열하는 방식으로 변환하는 함수. 

한글 ‘가’(유니코드 코드 포인트: U+AC00)를 각 인코딩 방식으로 변환한 결과.

```python
>>> ch = '가'
>>> ch.encode()
b'\xea\xb0\x80'
>>> ch.encode('UTF-8')
b'\xea\xb0\x80'
>>> ch.encode('UTF-16')
b'\xff\xfe\x00\xac'
>>> ch.encode('UTF-32')
b'\xff\xfe\x00\x00\x00\xac\x00\x00'
```

인코딩 방식을 각각 다르게 적용하면 결과 값과 크기가 모두 다르게 나타나는 걸 확인할 수 있습니다. 



#### 3.1 UTF-8

- Universal Coded Character Set Transformation Format–8 bit
- 문자 하나를 1byte~4byte로 표현. 
  - 코드 포인트가 U+0000 ~ U+007F일 때 1byte, 
  - U+0080 ~ U+07FF는 2byte, 
  - U+0800 ~ U+FFFF는 3byte, 
  - 나머지는 4byte로 표현. 
- 문자에 따라 바이트 수가 달라진다. -> 가변 길이 인코딩 방식
- endianless 방식.

유니코드에서 "가"의 코드포인트는 U+AC00이다. UTF-8로 인코딩하면 ea b0 80이다. 

```python
char = '\uac00'
print(char)
print(char.encode(encoding = 'utf-8'))
```

```bash
가
b'\xea\xb0\x80'
```

ex) "가"의 유니코드 코드포인트에서 UTF-8로 인코딩 과정.

1. 코드 포인트 U+ac00을 2진수로 표현한다.

$$
1010 \ 1100 \ 0000 \ 0000_{(2)}
$$

1. UTF-8에서 유니코드 코드 포인트가 U+0800에서 U+FFFF인 문자는 다음의 포맷으로 인코딩하여 코드 유닛을 생성한다.

$$
1110XXXX \ 10XXXXXX \ 10XXXXXX
$$

1. 위 포맷에 맞춰 1.의 2진수 값을 X에 앞부터 차례로 채워넣는다.

$$
11101010 \ 10110000 \ 10000000
$$

1.  위 3의 2진수를 16진수로 표현하면 0xeab080

## 3.2 UTF-16

- 유니코드 기반의 인코딩 방식 중 하나
- 2바이트 단위로 문자를 표현. 
- -해당 문자가 기본 다국어 평면에 있으면 2바이트로 인코딩, 그렇지 않으면 4바이트로 인코딩.

## 3.3 UTF-32

- 유니코드 인코딩 방식의 하나
- 모든 문자를 4바이트로 표현.

