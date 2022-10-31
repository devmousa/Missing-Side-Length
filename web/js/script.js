let addValuesBtn = document.getElementById('submit');
let lineName = document.getElementById('lineName');
let lineLength = document.getElementById('lineLength');
let degree = document.getElementById('degree');
let minutes = document.getElementById('minutes');
let seconds = document.getElementById('seconds');

let fileName = document.getElementById('fileName');
let fileExtension = document.getElementById('fileExtension');

let container = document.getElementById('container');

let resultBtn = document.getElementById('resultBtn');

let resetBtn = document.getElementById('resetBtn');

let saveBtn = document.getElementById('saveBtn');

addValuesBtn.addEventListener('click', async (e) => {
    e.preventDefault();
    eel.addLine(lineName.value, lineLength.value, degree.value, minutes.value, seconds.value);
    lineName.value = '';
    lineLength.value = '';
    degree.value = '';
    minutes.value = '';
    seconds.value = '';
    container.innerHTML = '';
    container.innerHTML += `<div class="header">line name</div>
                            <div class="header">length</div>
                            <div class="azimuth header">azimuth</div>
                            <div class="header">vertical compound</div>
                            <div class="header">horizontal compound</div>`
    let len = await eel.getData()();
    for(let i = 0; i < len[0].length; i++){
        let data = await eel.getData()();
        console.log(data);
        container.innerHTML += `<div>${data[0][i]}</div>
                                <div>${data[1][i][0]}</div>
                                <div class="azimuth">°${data[1][i][1]} '${data[1][i][2]} "${data[1][i][3]}</div>
                                <div>${data[2][i][0]}</div>
                                <div>${data[2][i][1]}</div>`
    }
})

resultBtn.addEventListener('click', async (e) => {
    e.preventDefault();
    container.innerHTML = '';
    container.innerHTML += `<div class="header">line name</div>
                            <div class="header">length</div>
                            <div class="azimuth header">azimuth</div>
                            <div class="header">vertical compound</div>
                            <div class="header">horizontal compound</div>`
    let len = await eel.getData()();
    for(let i = 0; i < len[0].length; i++){
        let data = await eel.getData()();
        console.log(data);
        container.innerHTML += `<div>${data[0][i]}</div>
                                <div>${data[1][i][0]}</div>
                                <div class="azimuth">°${data[1][i][1]} '${data[1][i][2]} "${data[1][i][3]}</div>
                                <div>${data[2][i][0]}</div>
                                <div>${data[2][i][1]}</div>`
    }
    let resultData = await eel.seeResult()();
    container.innerHTML += `<div class="result">${resultData[0][0][0]}</div>
    <div class="result">${resultData[0][0][1]}</div>
    <div class="azimuth result">°${resultData[0][0][2]} '${resultData[0][0][3]} "${resultData[0][0][4]}</div>
    <div class="result">${resultData[0][1][0]}</div>
    <div class="result">${resultData[0][1][1]}</div>`
    
    container.innerHTML += `<div class="transparency"></div>
    <div class="transparency"></div>
    <div class="transparency azimuth"></div>
    <div class="sum">${resultData[1]}</div>
    <div class="sum">${resultData[2]}</div>`

})

resetBtn.addEventListener('click', async (e) => {
    e.preventDefault();
    container.innerHTML = '';
    container.innerHTML += `<div class="header">line name</div>
                            <div class="header">length</div>
                            <div class="azimuth header">azimuth</div>
                            <div class="header">vertical compound</div>
                            <div class="header">horizontal compound</div>`;
    await eel.reset()();
})

saveBtn.addEventListener('click', async (e) => {
    e.preventDefault();
    await eel.save(fileName.value, fileExtension.value)();
    fileName.value = ''
    fileExtension.value = 'xls'
})