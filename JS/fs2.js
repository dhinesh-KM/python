const fs = require('fs').promises;

(async () => {
    try {
        console.log("opening file!");
        await fs.open("input.txt", 'r+');

        console.log("File open successfully\nreading file");

        let data = await fs.readFile('input.txt','utf8');
        console.log("data:", data.toString(),"\nData readed successfully")

        await fs.writeFile("input.txt", "W3 schools", 'utf8');
        console.log("Data written successfully");

        data = await fs.readFile('input.txt','utf8');
        console.log("new written data: " + data.toString());

        await fs.appendFile('input.txt', "\nLearn Node.js", 'utf8');
        console.log("Data is appended to file successfully.");

        data = await fs.readFile('input.txt');
        console.log("appended data: " + data.toString());

        await fs.unlink('input.txt');
        console.log("File deleted successfully!");
    } catch (err) {
        console.error(err);
    } finally {
        console.log("Finally statement!!!")
    }
})();
