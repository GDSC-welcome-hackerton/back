# 기사님 어디가세요??
<a href="https://github.com/features/actions"><img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white"/></a>

## Getting Started  

### Installation
<pre><code>git clone https://github.com/GDSC-welcome-hackerton/back.git
pip install -r requirements.txt
</code></pre>

### Request Example

<pre><code>fetch("https://rich-taxi.kro.kr:444/random-location", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    LoactionCount: 3
  }),
})
.then((response) => response.json())
.then((data) => console.log(data));
</code></pre>

## LICENSE

[MIT License](./LICENSE)
