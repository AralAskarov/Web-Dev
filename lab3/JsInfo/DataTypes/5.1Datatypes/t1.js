TypeError/undefined
"use strict";

let str = "Hello";

str.test = 5; // TypeError


let str = "Hello";

str.test = 5; // Никакой ошибки, но операция не имеет эффекта

alert(str.test); // undefined, так как свойство 'test' не было сохранено