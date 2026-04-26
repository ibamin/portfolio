let myURL = new URL('https://user:pass@sub.example.com:8080/p/a/t/h?query=string#hash');
console.log(myURL);

myURL = new URL('https://example.org/foo#bar');
console.log(myURL);

myURL.hash = 'baz';
console.log(myURL.href);

myURL = new URL('https://example.org/?user=abc&query=xyz');
console.log(myURL.searchParams.get('user'));
console.log(myURL.searchParams.has('user'));
console.log(myURL.searchParams.keys());
console.log(myURL.searchParams.values());
myURL.searchParams.append('user','admin');

console.log(myURL.searchParams.getAll('user'));
myURL.searchParams.set('user','admin');

myURL.searchParams.delete('user');
console.log(myURL.searchParams.toString());

const url = require('url');
console.log(url.parse('https://user:pass@sub.example.com:8080/p/a/t/h?query=string#hash'));
