/*
//Request & Response
const http = require('http');
const server = http.createServer((req, res)=>{
  console.log('Req sent');
  // console.log(req);
  console.log(req.url);
  console.log(req.method);

//response
  res.setHeader('Content-Type', 'text/html');
  res.write('<h1>hello</h1>');
  res.write('<h2>hai</h2>');
  res.end();
});

server.listen(3000, 'localhost', ()=>{
  console.log('Server is listening')
});

*/

/*
//HTML Page Manual redirection and Response Code

console.log(__filename);
const http = require("http");
const server = http.createServer((req, res) => {
  let path = './pages';
  console.log(req.url);
  if (req.url === "/") {
    path += "index.html";
  } else if (req.url === "/home") {
    res.statusCode = 301;
    res.setHeader("Location", "/");
    res.end();
  } else if (req.url === "/about") {
    path += "about.html";
  } else if (req.url == "/contact") {
    path += "contact.html";
  } else {
    path += "notFound.html";
    res.statusCode = 404;
  }

  const fs = require("fs");
  if (fs.existsSync(path)) {
    fs.readFile(path, (error, data) => {
      if (error) {
        console.log(error.message);
      } else {
        res.write(data);
        res.end();
      }
    });
  }
});

server.listen(3000, "localhost", () => {
  console.log("Server is listening...");
});
*/