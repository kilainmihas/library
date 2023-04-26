const btnEl = document.querySelector(".btn-el");
const showTimeEl = document.querySelector(".showtime");
const tableEl = document.getElementById("table-el");
const countEl = document.getElementById("count-el")
const changecolorEl = document.querySelector(".changecolor");

/*一般有兩種寫法 
一種在index上用onclick
一種如下 在javascript使用addEventListener去監控是否觸發
*/
btnEl.addEventListener("click", function () {
    const count = countEl.value;
    tableEl.innerHTML = "";
    //特別動畫呈現
    if (count == 1) {
        for (let i = 0; i < 10000; i++) {
            setTimeout(function () {
                tableEl.innerHTML = "";
                insertRow(0);
            }, 100);
        }
        return;
    }

    for (let i = 0; i < count; i++) {
        insertRow(i);
    }
    getTime();
});

function insertRow(rowIndex = 0) {
    numbers = getLottoNumber(1, 49);

    const row = tableEl.insertRow(rowIndex);
    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] < 10) {
            numbers[i] = "0" + numbers[i];
        }
        row.insertCell(i).textContent = numbers[i];
    }
}

changecolorEl.addEventListener("click", function () {

    changeColor();
});


let colorIndex = 0;
function changeColor() {

    colors = ["#ba55d3", "#87cefa", "#1e90ff", "#3cb371", "#fafad2", "#8a002e"];
    document.querySelector("body").style.background = colors[colorIndex++];
    if (colorIndex >= colors.length) {
        colorIndex = 0;
    }

}



function getLottoNumber(start, end, maxcount = 6, specialNumber = true) {
    //一般號碼
    let numbers = [];
    let count = 0;
    while (true) {
        const number = getRandnumber(start, end);
        if (!numbers.includes(number)) {
            numbers.push(number);
            count++;
            if (count == maxcount) {
                break;
            }
        }
    }
    numbers.sort(function (a, b) {
        //下列回傳1.-1.0其中之一 大體上a-b true a會往後挪 為正排序 false 則為反排序
        return a - b;
    });
    // for(let i =0; i<6 ;i++){
    //     const number = getRandnumber(1,49);
    //     numbers.push(number);
    // }
    //特別號
    if (specialNumber) {
        numbers.push(getRandnumber(start, end));

    }
    return numbers;
}



function getRandnumber(start, end) {
    return Math.floor(Math.random() * (end - start + 1)) + start;
}

function getTime() {
    let date = new Date();
    //取0-10個字元
    let day = date.toISOString().substring(0, 10);
    let hour = date.getHours();
    let minute = date.getMinutes();
    let sec = date.getSeconds();

    showTimeEl.textContent = `${day} :${hour} :${minute} :${sec}`;

    setTimeout("getTime()", 1000); // setTimeout("函式",毫秒) 1000毫秒=1秒
    console.log(date.toDateString());
}
