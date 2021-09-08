# JSON(JavaScript Object NMotation)

- 더글라스 크록포드(Douglas Crockford)가 널리 퍼뜨린 JavaScript 객체 문법을 따르는 문자 기반의 데이터 포맷이다.
- JavaScript 객체 문법과 유사하지만 JavaScript가 아니어도 JSON을 읽고 쓸 수 있는 기능이 다양한 프로그래밍 환경에서 제공된다.

  - **Note**: 문자열에서 네이티브 객체로 변환하는 것을(Parsing)이라고 한다. 네트워크를 통해 전달할 수 있게 객체를 문자열로 변환하는 과정은 문자열화(Stringification)이라고 한다.

## JSON 구조

- JSON안에 JavaScript의 기본 데이터 타입인 문자열, 숫자, 배열, 불리언 그리고 다른 객체를 포함할 수 있다.
- "property": object 형태로 값이 들어간다.

```json
{
  "majorName": "Computer Engineering",
  "univName": "JSON University",
  "active": true,
  "students": [
    {
      "name": "shin",
      "age": 24,
      "studentNumber": 20211234,
      "grade": 4.3,
      "objects": [
        "Deep Learning1",
        "Deep Learning2",
        "Data Analysis with python"
      ]
    },
    {
      "name": "kim",
      "age": 25,
      "studentNumber": 20215678,
      "grade": 3.7,
      "objects": ["Algorithm", "Computer Basic", "C Language"]
    }
  ]
}
```

## JSON 작성 시 주의 사항

- JSON은 순수히 데이터 포맷이다. 오직 프로퍼티만을 담으며, 메서드는 담을 수 없다.
- JSON은 문자열과 프로퍼티의 이름 작성시 큰 따옴표만을 사용해야한다. 작은 따옴표는 사용이 불가능하다.
- JavaScript에서는 객체의 프로퍼티로 큰 따옴표로 묶인 문자열 외에도 사용 가능했지만 JSON에서의 프로퍼티는 큰 따옴표로 묶인 문자열만 사용 가능하다.
- 콤마나 콜론을 잘못 배치할 경우 JSON파일이 잘못돼 작동하지 않을 수도 있다. 이럴 경우를 대비해 JSONLint같은 앱을 이용해 JSON 유효성을 검사할 수 있다.
