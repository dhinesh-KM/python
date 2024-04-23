const fs = require('fs');
let buf = new Buffer.alloc(1024)

console.log("opening file!");
fs.open("input.txt", 'r+', (err,fd) => {
    if (err) {
        return console.error(err);
     }
     console.log("File open successfully");  
     console.log("reading file " ,fd);

    fs.read(fd, buf, 0, buf.length, 0, (err,bytes) => {
        if (err) {
            return console.error(err);
        }
        console.log(bytes ,"bytes read");
        if (bytes>0) console.log(buf.slice(0,bytes).toString())

        fs.writeFile("input.txt", "W3 schools", 'utf8', (err,data) => {
            if (err) console.error(err)
        
            console.log("Data written successfully")
    
            fs.readFile('input.txt',(err,data) => {
                if (err) {
                    return console.error(err);
                }
                console.log("new written data: " + data.toString());
            });

            fs.appendFile('input.txt', "\nLearn Node.js", 'utf8', (err) => { 
                if (err) console.error(err) //throw err;

                console.log("Data is appended to file successfully.")

                fs.readFile('input.txt',(err,data) => {
                    if (err) {
                        return console.error(err);
                    }
                    console.log("appended data: " + data.toString());

                    fs.close(fd, (err) =>  {
                        if (err) return console.log(err);
                        console.log("File closed successfully.");

                        fs.unlink('input.txt', (err) =>  {
                            if (err) return console.error(err);
                            console.log("File deleted successfully!");
                         });
                    });
                });
            });
        });
    });
});



