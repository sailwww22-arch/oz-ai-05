//timer api
// 1) settimerout
// 일정 시간이 지난 뒤에 특정 함수를 한 번 호출하는 기능
setTimeout(
 () => console.log("3초경과"),
 3000 // 3000ms = 3s
)
//  2) setinterval: 일정 시간마다 특정 함수를 반복 실행하는 기능
let counter = 0
const timerid = setInterval(() => 
{
    
    if (counter > 5) {
        clearInterval(timerid);
        
    }
    counter++;
    console.log("2초 경과");
}, 2000);