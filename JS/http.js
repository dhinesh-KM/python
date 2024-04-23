const http = require("http")

let options = {
    host: 'www.geeksforgeeks.org',
    path: '/courses',
    method: 'GET'
};

http.createServer((req,res) => {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.write(JSON.stringify({ data: 'Hello World!', }));
    res.end()
}).listen(3000, () => {
    console.log('Server running at http://localhost:3000/');
  });

http.request(options, (response) => {
 
    // Printing the statusCode
    console.log(`STATUS: ${response.statusCode}`);
}).end();