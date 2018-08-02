# 180801

#### 딥러닝, 좋은친구(deep learning book,모두의 연구소, 풀잎스쿨)

#### 9.1~9.5 (CNN)

##### intro

- CNN 실제 응용에서 매우 성공.
- convolution은 linear operation의 일종임.
- CNN은 최소 한개 레이어에서 convolution 연산 사용
- best architecture은 실시간으로 갱신되지만, 다 이 장에서 설명하는 방식의 응용임.

##### 9.1 convolution이 뭔가요

- 실수인자를 가진 두 함수의 연산이다. (원래는)
- 첫 인자를 input(함수 x), 둘째 인자를 kernel(함수 w), output은 feature map이라 할 수 있다.
- 현실적으로 discrete인 데이터 convolution를 씀
- 이 discrete convolution은 matrix의 곱이라 볼 수 있다.
- 그때 어떤 제약이 걸리는데
- univariate discrete convolution일 때, 
  - Toeplitz matrix(한 row가 바로 위 row와 1요소가 이동된 패턴)
- 2차원일 때, 
  - doubly block circulant matrix(3차원 행렬식 연산마냥, 중앙 대각선끼리 같고, 블라블라 )
- convolution은 보통 매우 sparse한 matrix이다.
  - 왜냐하면 kernel이 input 보다 훨씬 작기 때문이다.

##### 9.2 convolution이 어떤 동기로 뉴럴넷에 사용될 수 있었나요

convolution이 leverage한 3가지 ideas

(sparse interactions, parameter sharing,equivariant representations)

- sparse interactions
- 전통 NN 층은 각각 output unit이 모든 input unit과 연결되어 있다.
- 그러나 CNN은 sparse interactions(또는 sparse connectivity,sparse weights)를 가진다.
  - 이것은 kernel이 input보다 작기 때문이다.
    - 예를들어 영상처리라고 하자.
    - input은 수천에서 수백만 픽셀인데, kernel은 수십에서 수백 픽셀이다.
    - kernel은 edge와 같은 의미를 가진 features이다.
    - 이는 훨씬 적은 parameter만 저장하면 됨을 이야기 한다.
    - 필요한 메모리도 적고, 통계적인 효율도 생긴다. output내는데 연산도 훨씬 적다.
    - m을 inputs, n을 output이라 두자. O(m x n) 만큼의 runtime이 필요하다.
    - 만약 output의 연결을 k만큼 제한하면, O(k x n)만큼의 runtime이 든다.
    - 실제 응용에서 k가 m보다 훨씬 작고 좋은 성능을 보인다.
  - sparse connectivity의 그래피컬 이해 (그림9.2,9.3 참고)
  - cnn블록 간의 간접적이고 복잡한 상호작용을 이해(그림9.4 참고)
- Parameter sharing이란,
  - 한 모델에서, 하나 이상의 함수가 같은 parameter를 공유함을 의미한다.
  - 전통 NN은
- 

##### 9.3 pooling이 뭔가요

##### 9.4 convolution은 일종의 infinitly strong prior로 볼 수 있어요

##### 9.5 convolution의 다양한 변형연산이 있어요

