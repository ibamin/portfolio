const path = require('path');

console.log(__filename);
console.log(path.basename(__filename));
console.log(path.basename(__filename,'.js'));

console.log(__dirname);
console.log(path.dirname(__filename));

console.log(path.delimiter);
console.log(process.env.path);
process.env.path.split(path.delimiter);

console.log(path.extname(__filename));
