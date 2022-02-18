# DOM 선택함수별 이벤트 등록시 차이점

- `document.querySelector(selector)`

  - 가장 첫 번째로 selector와 일치하는 element를 하나 반환한다.
  - selector와 일치하는 element가 존재한다면 제대로 element를 반환한다.
  - selector와 일치하는 element가 존재하지 않는다면 null을 반환한다.
  - 이벤트 등록(addEventListener)할 시에 selector와 일치하는 element가 존재하는 경우 문제가 없지만 **존재하지 않는다면 null에 이벤트 등록을 하게 돼서 타입 에러(TypeError)가 발생한다.**

- `document.querySelectorAll(selector)`
  - selector와 일치하는 모든 element들을 모두 갖고있는 NodeList를 반환한다.
  - 따라서 NodeList를 `forEach`문을 이용해 모든 element에 이벤트 등록을 한다.
  - `forEach`문을 사용하는 과정에서 빈 노드리스트는 자연스럽게 무시되기 때문에 타입 에러(TypeError)가 발생하지 않는다.
