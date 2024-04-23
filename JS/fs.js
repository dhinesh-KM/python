const fs = require('fs').promises;
let buf = new Buffer.alloc(1024)


console.log("opening file!");
fs.open("input.txt", 'r+')
    .then(() => {
        console.log("File open successfully");  
        console.log("reading file");
        return fs.readFile('input.txt','utf8');
    })
    .then((data) => { 
        console.log("data:", data.toString())
        console.log("Data readed successfully")
        console.log("Data  writing")
        return fs.writeFile("input.txt", "W3 schools", 'utf8');
    })
    .then(() => {
        console.log("Data written successfully");
        return fs.readFile('input.txt','utf8');
    })
    .then((data) => {
        console.log("new written data: " + data.toString());
        return fs.appendFile('input.txt', "\nLearn Node.js", 'utf8');
    })
    .then(() => { 
        console.log("Data is appended to file successfully.");
        return fs.readFile('input.txt','utf8');
    })
    .then((data) => {
        console.log("appended data: " + data.toString());
        return fs.unlink('input.txt');
    })
    .then(() =>  {
        console.log("File deleted successfully!");
    })
    .catch((err) => {
        console.error(err);
    });



