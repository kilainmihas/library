const countEl = document.querySelector("#count");
//El ==>element
const nameEl = document.getElementById("name");
const heightEl = document.getElementById("height");
const weightEl = document.getElementById("weight");
const resultEl = document.querySelector(".result");

function calc() {
    let height = parseFloat(heightEl.value);
    let weight = parseFloat(weightEl.value);

    if (isNaN(weight) || isNaN(height)) {
        alert("數值輸入錯誤");
        return;
    }

    let bmi = weight / (height / 100) ** 2;
    console.log(nameEl.value, heightEl.value, weightEl.value, bmi.toFixed(2));

    resultEl.textContent = "BMI:" + bmi.toFixed(2);
}