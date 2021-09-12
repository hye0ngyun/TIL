# JSON-LD(JSON for Linked Data)

- JSON을 사용하여 링크드 데이터를 인코딩하는 방식이다.
- JSON-LD는 JSON->RDF 모델의 추가적인 매핑을 제공하기 위한 컨텐스트의 개념으로 설계되어 있다.
- 이 컨텐스트는 JSON 문서 내의 객체 속성을 **온톨로지**의 개념에 연결시킨다.

## JSON-LD 예시

```json-ld
{
  "@context": {
    "name": "http://xmlns.com/foaf/0.1/name",
    "homepage": {
      "@id": "http://xmlns.com/foaf/0.1/workplaceHomepage",
      "@type": "@id"
    },
    "Person": "http://xmlns.com/foaf/0.1/Person"
  },
  "@id": "https://me.example.com",
  "@type": "Person",
  "name": "John Smith",
  "homepage": "https://www.example.com/"
}
```

- **Note**: 링크드 데이터(linked data)는 웹 상에 존재하는 데이터를 개별 URI(Uniform Resource Identifier)로 식별하고, 각 URI에 링크 정보를 부여함으로써 상호 연결된 웹을 지향하는 모형이다. 링크 기능이 강조된 시멘틱 웹 모형이다.

- **Note**: 자원 기술 프레임워크(RDF; Resource Description Framework)는 웹 상의 자원 정보를 표현하기 위한 규격이다. 상이한 메타데이터 간의 어의 구문 및 구조에 대한 공통적인 규칙을 지원한다.

- **Note**: 온톨로지(Ontology)는 지식표현(knowledge representation)으로, 컴퓨터는 온톨로지로 표현된 갠며을 이해하고 지식처리를 할 수 있게 된다. 온톨로지는 시멘틱 웹을 구현할 수 있는 도구로서, 지식개념을 의미적으로 연결할 수 있는 도구로서 RDF, OWL, SWRL 등의 언어를 이용해 표현된다.
