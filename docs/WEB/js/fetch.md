# fetch
js에서 api를 호출하는 함수
## then

then을 이용한 영화 api 호출하기

```js
function App() {
  const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);
  useEffect(() => {
    fetch(
      `https://yts.mx/api/v2/list_movies.json?minimum_rating=8.5&sort_by=year`
    )
      .then((response) => response.json())
      .then((json) => {
        setMovies(json.data.movies);
        setLoading(false);
        console.log(movies);
      });
  }, []);
  return <div>{loading ? <h1>Loading...</h1> : null}</div>;
}
```

## async await

async await를 이용한 영화 api 호출하기

```js
function App() {
  const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);
  const getMoives = async () => {
    // const response = await fetch(
    //   `https://yts.mx/api/v2/list_movies.json?minimum_rating=8.5&sort_by=year`
    // );
    // const json = await response.json();
    const json = await (await fetch(
      `https://yts.mx/api/v2/list_movies.json?minimum_rating=8.5&sort_by=year`
    )).json();
    setMovies(json.data.movies);
    setLoading(false);
  };
  useEffect(() => {
    getMoives();
    // (async () => {
    //   const json = await (
    //     await fetch(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`)
    //   ).json();
    //   setDetail(json.data.movie);
    //   setLoading(false);
    //   console.log(detail);
    // })();
  }, []);
  return <div>{loading ? <h1>Loading...</h1> : null}</div>;
}
```
