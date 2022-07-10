# Reactive Programming

**변화의 전파**와 **데이터 흐름**과 관련된 **선언적 프로그래밍** 패러다임이다.

- 변화의 전파와 데이터 흐름: 데이터가 변경(state change)될 때 마다 이벤트를 발생시켜 데이터를 계속적으로 전달한다.
- 선언적 프로그래밍: 실행할 동작을 구체적으로 명시하는 명령형 프로그래밍과 달리 선언형 프로그래밍은 단순히 목표를 선언한다.

## 리액티브의 개념이 적용된 예

Push 방식 : 데이터의 변화가 발생했을 떄 변경이 발생한 곳에서 데이터를 보내주는 방식

- RTC(Real Time Communication)
- 소켓 프로그래밍
- DB Trigger
- Spring의 ApplicationEvent
- Angular의 데이터 바인딩

스마트폰의 Push 메시지

- Pull 방식 : 변경된 데이터가 있는지 요청을 보내 질의하고 변경된 데이터를 가져오는 방식
- 클라이언트 요청 & 서버 응답 방식의 애플리케이션
- Java와 같은 절차형 프로그래밍 언어

## 리액티브 프로그래밍의 이점

- 간결해진 Thread 사용
- 간단한 비동기 연산
- 콜백 지옥의 제거

## 리액티브 프로그래밍의 주요 구성 요소

Reactive 프로그래밍의 주요 구성 요소는 아래와 같이 세 가지로 구분된다.

- **Observable**
  Observable은 **데이터 스트림**으로, Observable은 하나의 스레드에서 다른 스레드로 전달 할 데이터를 압축한다. 주기적 또는 설정에 따라 생애 주기동안 데이터를 방출한다. Observable은 데이터를 처리하고 다른 구성요소에 전달하는 역할을 수행한다.

- **Observers**
  Observers는 Observable에 의해 방출된 **데이터 스트림을 받아서 처리**한다. Observers는 subscribe() 메서드를 사용해서 observable을 구독하고 observable이 방출하는 데이터를 수신할 수 있다. observable이 데이터를 방출할 때 마다 등록된 모든 observer는 onNext() 콜백으로 데이터를 수신하고 데이터 방출이 완료되면 onComplete() 에러가 발생하면 onError() 콜백으로 수신한다.

- **Schedulers**
  Reactive 프로그래밍은 비동기 프로그래밍을 위한 것으로, 개발자는 스레드를 관리해야할 필요가 있다. Schedulers는 Observable과 Observers 에게 그들이 **실행되어야 할 스레드를 알려주는 구성요소**이다. observeOn() 메서드로 observers에게 관찰해야 할 스레드를 알려줄 수 있고, scheduleOn() 메서드로 observable이 실행해야 할 스레드를 알려줄 수 있다.

## 리액티브 프로그래밍을 위해 알아야 될 것들

- Observable : 데이터 소스 (변경되는 데이터 관찰)
- 리액티브 연산자(Operators) : 데이터 소스를 처리하는 함수
- 스케쥴러(Scheduler) : 스레드 관리자
- Subscriber : Observable이 발행하는 데이터를 구독하는 구독자
- 함수형 프로그래밍 : RxJava에서 제공하는 연산자(Operator) 함수를 사용
- doOnNext : 데이터가 발생한 후 onNext 함수가 호출된 후 호출되는 메소드
- subscribeOn : 데이터가 발행, 데이터의 흐름을 결정짓는 스레드를 결정
- observeOn : 발행된 데이터를 가공하고 구독해서 처리하는 스레드를 결정
- 리액티브 기본 동작 흐름 : 데이터 발행 -> 데이터 가공 -> 데이터 구독 -> 결과 처리

## 참고 자료

- [Reactive 프로그래밍이란?](https://als2019.tistory.com/71)
- [RxJava - 리엑티브(Reative) 프로그래밍이란](<https://yunzai.dev/posts/RxJava_%EB%A6%AC%EC%97%91%ED%8B%B0%EB%B8%8C(Reative)_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%B4%EB%9E%80/>)
