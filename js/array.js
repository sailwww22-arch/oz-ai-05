//배역 (array)
//여러 값을 하나로 묶은 자료
//인덱스(index): 배열 내에서의 데이터의 번호

let numbers = [ 10, 20, 30, "40"];

console.log(numbers[0]);
console.log(numbers[1]);
console.log(numbers[10]);
console.log(numbers.at(-1))

for (const [i, n] of numbers.entries()) {
     console.log(i, n);
}