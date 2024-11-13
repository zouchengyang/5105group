


function SatrJIsuan() {
    var q213 = document.getElementById('Calculate');
    q213.scrollIntoView({ behavior: 'smooth' });
}
function Toresult() {
    var q213 = document.getElementById('result_and_compare');
    q213.scrollIntoView({ behavior: 'smooth' });
}

function move_to_Aboutua() {
    var q213 = document.getElementById('aboutus');
    q213.scrollIntoView({ behavior: 'smooth' });
}

function move_to_misson() {
    var q213 = document.getElementById('result_and_compare');
    q213.scrollIntoView({ behavior: 'smooth' });
}
function move_to_Calculate() {
    var q213 = document.getElementById('Calculate');
    q213.scrollIntoView({ behavior: 'smooth' });
}
function move_to_home() {
    var q213 = document.getElementById('home');
    q213.scrollIntoView({ behavior: 'smooth' });
}



function closeRes() {
    var res = document.getElementById('form-ct');
    res.style.display = 'none';

    var res = document.getElementById('address_and_Contact');
    res.style.display = 'none';

    var res2 = document.getElementById('userInfo');
    res2.style.display = 'block';

    var res22 = document.getElementById("total");
    res22.style.opacity =1;

}

function openRes() {
    var res = document.getElementById('form-ct');
    res.style.display = 'block';

    var res22 = document.getElementById("total");
    res22.style.opacity = 0.1;
}

function address_and_conatct() {
    var res = document.getElementById('address_and_Contact');
    res.style.display = 'block';

    var res2 = document.getElementById('userInfo');
    res2.style.display = 'none';


}

function userifrom() {
    var res = document.getElementById('address_and_Contact');
    res.style.display = 'none';

    var res2 = document.getElementById('userInfo');
    res2.style.display = 'block';
}

function To_transportation_page() {
    var res = document.getElementById('house_page');
    res.style.display = 'none';

    var res2 = document.getElementById('transportation_page');
    res2.style.display = 'block';
}

function To_house_page() {
    var res = document.getElementById('house_page');
    res.style.display = 'block';

    var res2 = document.getElementById('transportation_page');
    res2.style.display = 'none';
}
function To_food_page() {
    var res = document.getElementById('transportation_page');
    res.style.display = 'none';

    var res2 = document.getElementById('food_page');
    res2.style.display = 'block';
}

function baclk_trans_page() {
    var res = document.getElementById('transportation_page');
    res.style.display = 'block';

    var res2 = document.getElementById('food_page');
    res2.style.display = 'none';
}
function To_cum_page() {
    var res = document.getElementById('consume_page');
    res.style.display = 'block';

    var res2 = document.getElementById('food_page');
    res2.style.display = 'none';
}


function back_food() {
    var res = document.getElementById('food_page');
    res.style.display = 'block';

    var res2 = document.getElementById('consume_page');
    res2.style.display = 'none';
}




function updateWaterOutput(slider) {
    const value = slider.value;
    const max = slider.max;
    const percentage = (value / max) * 100;
    slider.style.background = `linear-gradient(to right, #fdd49b ${percentage}%, #f78e1e ${percentage}%, white ${percentage}%)`;
    document.getElementById('water-output').innerText = value;
}

function WasteOutput(slider) {
    const value = slider.value;
    const max = slider.max;
    const percentage = (value / max) * 100;
    slider.style.background = `linear-gradient(to right, #fdd49b ${percentage}%, #f78e1e ${percentage}%, white ${percentage}%)`;
    document.getElementById('waste-output').innerText = value;
}

function eleOutput(slider) {
    const value = slider.value;
    const max = slider.max;
    const percentage = (value / max) * 100;
    slider.style.background = `linear-gradient(to right, #fdd49b ${percentage}%, #f78e1e ${percentage}%, white ${percentage}%)`;
    document.getElementById('ele-outpu').innerText = value;
}

function traOutput(slider) {
    const value = slider.value;
    const max = slider.max;
    const percentage = (value / max) * 100;
    slider.style.background = `linear-gradient(to right, #fdd49b ${percentage}%, #f78e1e ${percentage}%, white ${percentage}%)`;
    document.getElementById('tra-output').innerText = value;
}

function areaOutput(slider) {
    const value = slider.value;
    const max = slider.max;
    const percentage = (value / max) * 100;
    slider.style.background = `linear-gradient(to right, #fdd49b ${percentage}%, #f78e1e ${percentage}%, white ${percentage}%)`;
    document.getElementById('area-output').innerText = value;
}

function peopleOutput(slider) {
    const value = slider.value;
    const max = slider.max;
    const percentage = (value / max) * 100;
    slider.style.background = `linear-gradient(to right, #fdd49b ${percentage}%, #f78e1e ${percentage}%, white ${percentage}%)`;
    document.getElementById('people-output').innerText = value;
}

 


function To_ele_ca() {
    var waterCalculator = document.getElementById('water-calculator');
    var eleCalculator = document.getElementById('ele-calculator');

    // 移除水资源计算器的 active 类
    waterCalculator.classList.remove('active');


    setTimeout(function() {
        eleCalculator.classList.add('active');
    }, 700); 
}

function To_water_ca() {
    var waterCalculator = document.getElementById('water-calculator');
    var eleCalculator = document.getElementById('ele-calculator');


    eleCalculator.classList.remove('active');

    setTimeout(function() {
        waterCalculator.classList.add('active');
    }, 700); 
}

function To_waste1() {
    var wastCalculator = document.getElementById('waste1-calculator');
    var eleCalculator = document.getElementById('ele-calculator');

    // 移除水资源计算器的 active 类
    eleCalculator.classList.remove('active');


    setTimeout(function() {
        wastCalculator.classList.add('active');
    }, 700); 
}


function To_ele_ca2(){
    var wastCalculator = document.getElementById('waste1-calculator');
    var eleCalculator = document.getElementById('ele-calculator');


    wastCalculator.classList.remove('active');


    setTimeout(function() {
        eleCalculator.classList.add('active');
    }, 700); 

}

function To_tr(){
    var wastCalculator = document.getElementById('waste1-calculator');
    var trCalculator = document.getElementById('tr-calculator');


    wastCalculator.classList.remove('active');


    setTimeout(function() {
        trCalculator.classList.add('active');
    }, 700); 
}

function To_waste2(){
    var wastCalculator = document.getElementById('waste1-calculator');
    var trCalculator = document.getElementById('tr-calculator');


    trCalculator.classList.remove('active');


    setTimeout(function() {
        wastCalculator.classList.add('active');
    }, 700); 
}

function To_area1(){
    var areaCalculator = document.getElementById('area-calculator');
    var trCalculator = document.getElementById('tr-calculator');


    trCalculator.classList.remove('active');


    setTimeout(function() {
        areaCalculator.classList.add('active');
    }, 700); 
}


function To_tr2(){
    var areaCalculator = document.getElementById('area-calculator');
    var trCalculator = document.getElementById('tr-calculator');


    areaCalculator.classList.remove('active');


    setTimeout(function() {
        trCalculator.classList.add('active');
    }, 700); 
}


function To_second(){
  

    var homeSection = document.getElementById('home-section');
    var calculatorSection = document.getElementById('second_calculator-section');
    homeSection.classList.add('out');

     
         
    calculatorSection.classList.add('active');

 

     
}

 





function startCalculator() {
    var homeSection = document.getElementById('home-section');
    var calculatorSection = document.getElementById('calculator-section');
    homeSection.classList.add('out');

     
         
    calculatorSection.classList.add('active');
    

    // 添加类，触发滑动动画
      
}

function backToHome() {
    var homeSection = document.getElementById('home-section');
    var calculatorSection = document.getElementById('calculator-section');
 

    calculatorSection.classList.remove('active');
    homeSection.classList.remove('out');
 
     
}


function backToHome1() {
    var homeSection = document.getElementById('home-section');
    var calculatorSection = document.getElementById('second_calculator-section');
 

    calculatorSection.classList.remove('active');
    homeSection.classList.remove('out');
 
     
}



function startRes() {
    var calculatorSection = document.getElementById('calculator-section');
    var ress = document.getElementById('res-section');
 
     

    var a = document.getElementById('home-section');
    a.style.display = 'none';
    
     
  setTimeout(function() {
    ress.classList.add('active');
    showContent('chart'); 

 }, 1200); 

 

//
}
 




// 获取按钮和弹出窗口的元素
const registerBtn = document.getElementById('register-btn');
const overlay = document.getElementById('overlay');
const closeBtn = document.getElementById('close-btn');
const fileInput = document.getElementById('file-input');
const submitBtn = document.getElementById('submit-btn');
const errorMessage = document.getElementById('error-message');

// 显示上传界面
registerBtn.addEventListener('click', () => {
    overlay.style.display = 'flex';
});

// 关闭上传界面
closeBtn.addEventListener('click', () => {
    overlay.style.display = 'none';
    fileInput.value = ''; // 重置文件输入
    errorMessage.textContent = ''; // 清除错误信息
});

// 提交CSV文件
 














// 提交文件

function extractValues(rows) {
   

    // 去除标题行，获取实际数据
    const data = rows.slice(1) // 去掉标题行
        .filter(row => row.trim() !== '') // 去掉空行
        .map(row => row.split(',').map(col => col.trim())); // 分割列并去除多余空格

    // 提取各列数据
    const waterUse = data.map(row => parseFloat(row[0])); // 第1列：Water Use
    const electricityUse = data.map(row => parseFloat(row[1])); // 第2列：Electricity Use
    const waste1 = data.map(row => parseFloat(row[2])); // 第3列：Waste
    const gas1 = data.map(row => parseFloat(row[3])); // 第4列：Gas
    const area1 = data.map(row => parseFloat(row[4])); // 第5列：Area
    const people1 = data.map(row => parseInt(row[5])); // 第6列：People

 

    water = waterUse*0.57 ,ele = electricityUse*0.4733,waste=waste1*0.3,gas=gas1*0.244;

    area = area1,people = people1;
    const sum1 = water+ele+waste+gas;
 

    per_quare =  Math.floor(sum1 / area);
    per_people =Math.floor( sum1 / people);

     
 
}





        // 定义期望的CSV列模板
const expectedColumns = ['Water Use m3', 'Electricity Use kWh/M', 'Waste Usd T', 'Gas kWh/M', 'Area m2', 'People'];

// 读取并验证CSV文件
function validateCSV(file) {
    const reader = new FileReader();

    reader.onload = (e) => {
        const content = e.target.result.trim(); // 读取内容并去除多余空格
        if (!content) {
            alert('The file is empty, please upload a valid CSV file.');
            return;
        }

        const rows = content.split('\n'); // 分割每一行
        const header = rows[0].split(',').map(col => col.trim().toLowerCase()); // 提取标题并标准化为小写

        // 标准化期望列为小写
        const expectedLowerCaseColumns = expectedColumns.map(col => col.toLowerCase());

        // 检查标题是否符合模板
        const isValid = expectedLowerCaseColumns.every((column, index) => header[index] === column);

        if (isValid) {
        
            extractValues(rows); // 调用提取函数（需实现）
            alert(
                `result：
        Water Use: ${water}
        Electricity Use: ${ele}
        Waste: ${waste}
        Gas: ${gas}
        Area: ${area}
        People: ${people}`
            );

            document.getElementById('prediction-value').innerText = (water+ele+waste+gas).toFixed(2);

            
             


            showContent();
            getrepot();

            startRes();
             

        } else {
            // 显示错误信息
            alert(`CSV format is incorrect, please use the correct template to upload the file.\n\nActual column names: ${header.join(', ')}\nExpectation of listing: ${expectedColumns.join(', ')}`);
        }
    };

    reader.onerror = () => {
        alert('Cannot read the file, please check the file format or content.');
    };

    reader.readAsText(file); // 读取文件内容
}




submitBtn.addEventListener('click', () => {
    const file = fileInput.files[0];
    if (file) {
        // 调用validateCSV()函数来验证CSV文件
        validateCSV(file);
    } else {
        alert('Please upload a CSV file.');
    }
});
// 提交文件

 

function updateButtonState(type) {
    buttons.forEach(button => {
        // 检查按钮的 data-type 属性
        if (button.getAttribute('data-type') === type) {
            button.classList.add('active'); // 选中时变浅色
        } else {
            button.classList.remove('active'); // 未选中时恢复正常颜色
        }
    });
}







const buttons = document.querySelectorAll('.toggle-btn');















var water_b = 25,water, waste, gas, area, people,ele;
var waste_b, gas_b,ele_b;
var myGlobalList = [];

var per_people,per_quare;

var lis = [25, 25,25,25]

function logInputs() {
    // 获取每个输入框的值
     water = document.getElementById('water-slider').value *0.57 ;
     waste = document.getElementById('waste1-slider').value *0.3;
     gas = document.getElementById('tr-slider').value *0.244;
     area = document.getElementById('area-slider').value;
     people = document.getElementById('people-slider').value;
     ele = document.getElementById('ele-slider').value *0.4733; 
      

 
  
}

 

function calculateProportions() {
    // 计算总量
    const total = water + ele + waste + gas;
 
    let myLocalList = [];
    document.getElementById('prediction-value').innerText = total.toFixed(2);
    // 避免除以 0 的情况
    if (total === 0) {
        alert("Error: Total is 0. All percentages will be 0.");
        return {
            water_b: 0,
            ele_b: 0,
            waste_b: 0,
            gas_b: 0
        };
    }

    // 计算每项的比例（向下取整）
    water_b = Math.floor((water / total) * 100);
    ele_b = Math.floor((ele / total) * 100);
    waste_b = Math.floor((waste / total) * 100);
    gas_b = Math.floor((gas / total) * 100);

    let sum = water_b + ele_b + waste_b + gas_b;
 

     

    per_quare =  Math.floor(total / area);
    per_people =Math.floor( total / people);
    




}

// Toggle between chart and text content
function showContent(type) {

    const chartContent = document.getElementById('chart-content');
    const textContent = document.getElementById('text-content');

    if (type === 'chart') {
        chartContent.classList.add('active');
        textContent.classList.remove('active');
        
        loadChart(); // Load charts when the 'chart' content is active
    } else {
        textContent.classList.add('active');
        chartContent.classList.remove('active');
 
    }
}


function hideChartContent() {
    const chartContent = document.getElementById("chart-content");
 
    chartContent.style.position = "absolute";
    chartContent.style.left = "-9999px";
  
}

function showChartContent() {
    const chartContent = document.getElementById("chart-content");
 
    chartContent.style.position = "absolute";
    chartContent.style.left = "50%";
    chartContent.style.transform = "translateX(-50%)"; // 确保居中
  
}


function toggleContent(type) {
    const chartContent = document.getElementById("chart-content1");
    const textContent = document.getElementById("text-content1");

    if (type === "chart") {
        if (chartContent) chartContent.style.display = "block";
        if (textContent) textContent.style.display = "none";
    } else if (type === "text") {
        if (chartContent) chartContent.style.display = "none";
        if (textContent) textContent.style.display = "block";
    }
}
































// 加载文字总结


 

// 默认显示图像内容
 

 

 






document.getElementById("generateButton").addEventListener("click", async () => {
    const apiKey = "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";  // 替换为你的 OpenAI API 密钥

    const userMessage = `Here are some data:
- Water usage (kg CO2e): ${water}
- Electricity usage (kg CO2e): ${ele}
- Waste (kg CO2e): ${waste}
- Gas usage (kg CO2e): ${gas}
- Number of people: ${people}
- Area (square meters): ${area}

Please just analyze these characteristics before giving your three points. Answers should be no more than 280 words.`;

    try {
        const response = await fetch("https://api.openai.com/v1/chat/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                model: "gpt-3.5-turbo",  // Use "gpt-3.5-turbo" or "gpt-4" if available
                messages: [
                    { role: "system", content: "You are an expert in environmental science and sustainability. Please respond in English." },
                    { role: "user", content: userMessage },
                ],
                max_tokens: 1000  // Limit the maximum number of tokens
            })
        });

        const data = await response.json();
        const content = data.choices[0].message.content || "Error: No response";

        // Format the content returned from the API
        const formattedContent = formatNumberedPoints(content);

        // Display the formatted content
        document.getElementById("result").innerHTML = formattedContent;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").textContent = "Error: " + error.message;
    }
});

// Function to format numbered points in the API response
function formatNumberedPoints(content) {
    // Split the content into an array at each numbered point
    const parts = content.split(/(?=\d+\.\s)/g);

    let formattedText = '';
    for (let i = 0; i < parts.length; i++) {
        const part = parts[i].trim();
        if (part.match(/^\d+\.\s/)) {
            // If the part starts with a number, wrap it in list item tags
            formattedText += `<li>${part}</li>`;
        } else {
            // Otherwise, wrap it in paragraph tags
            formattedText += `<p>${part}</p>`;
        }
    }

    // Wrap all list items in an ordered list
    formattedText = formattedText.replace(/(<li>[\s\S]*?<\/li>)+/g, match => `<ol>${match}</ol>`);

    return formattedText;
}


function loadChart() {
    // Load Pie Chart
    const pieCtx = document.getElementById("pieChart").getContext("2d");
 
    const labels = [
        `Waste (${waste}kg C02e)`,
        `Water (${water}kg C02e)`,
        `Gas (${gas}kg C02e)`,
        `Electric (${ele}kg C02e)`
    ];

    const total = waste +water+gas+ele;
    const waste_proportion = (waste / total) * 100
    const water_proportion = (water / total) * 100
    const gas_proportion = (gas / total) * 100
    const ele_proportion = (ele / total) * 100
    new Chart(pieCtx, {
        type: "pie",
        data: {
            labels:labels ,
            datasets: [{
                data:  [waste_proportion, water_proportion,gas_proportion,ele_proportion],
                backgroundColor: [
                    "rgba(255, 99, 132, 0.6)",
                    "rgba(54, 162, 235, 0.6)",
                    "rgba(255, 206, 86, 0.6)",
                    "rgba(75, 192, 192, 0.6)"
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top'
                }
            }
        }
    });

    // Load Per Capita Chart
    const perCapitaCtx = document.getElementById("perCapitaChart").getContext("2d");
    new Chart(perCapitaCtx, {
        type: "bar",
        data: {
            labels: ["User", "Reference 1", "Reference 2"],
            datasets: [{
                label: "Per Capita Emission (tons)",
                data: [per_people, 189.17, 150.78],
                backgroundColor: ["rgba(75, 192, 192, 0.6)", "rgba(54, 162, 235, 0.6)", "rgba(153, 102, 255, 0.6)"]
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    // Load Per Square Meter Chart
    const perSquareMeterCtx = document.getElementById("perSquareMeterChart").getContext("2d");
    new Chart(perSquareMeterCtx, {
        type: "bar",
        data: {
            labels: ["User", "Reference 1", "Reference 2"],
            datasets: [{
                label: "Emission per Square Meter (kg)",
                data: [per_quare, 7.28, 9.53],
                backgroundColor: ["rgba(255, 159, 64, 0.6)", "rgba(255, 206, 86, 0.6)", "rgba(75, 192, 192, 0.6)"]
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

// 绑定按钮点击事件
buttons.forEach(button => {
    button.addEventListener('click', () => {
        const type = button.getAttribute('data-type');
        showContent(type);
    });
});




 

 

async function getrepot() {
    const apiKey = "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";  // 替换为你的 OpenAI API 密钥

    const userMessage = `Here are some data:
- Water usage (kg CO2e): ${water}
- Electricity usage (kg CO2e): ${ele}
- Waste (kg CO2e): ${waste}
- Gas usage (kg CO2e): ${gas}
- Number of people: ${people}
- Area (square meters): ${area}

Please just analyze these characteristics before giving your three points. Answers should be no more than 220 words.`;

    try {
        const response = await fetch("https://api.openai.com/v1/chat/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                model: "gpt-4o",  // Use "gpt-3.5-turbo" or "gpt-4" if available
                messages: [
                    { role: "system", content: "You are an expert in environmental science and sustainability. Please respond in English." },
                    { role: "user", content: userMessage },
                ],
                max_tokens: 1000  // Limit the maximum number of tokens
            })
        });

        const data = await response.json();
        const content = data.choices[0].message.content || "Error: No response";

        // Format the content returned from the API
        const formattedContent = formatNumberedPoints(content);

        // Display the formatted content
        document.getElementById("result").innerHTML = formattedContent;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").textContent = "Error: " + error.message;
    }
}



async function getrepot1(siteEUI, gasIntensity, floorArea, electricityIntensity, latitude, longitude, people, totalEmission) {
    const apiKey = "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"; // 替换为你的 OpenAI API 密钥

    // 构造用户消息
    const userMessage = `Here are some data:
- Site EUI (kBtu/ft²): ${siteEUI}
- Weather Normalized Site Natural Gas Intensity (therms/ft²): ${gasIntensity}
- Primary Property Use Type - Gross Floor Area (ft²): ${floorArea}
- Weather Normalized Site Electricity Intensity (kWh/ft²): ${electricityIntensity}
- Latitude: ${latitude}
- Longitude: ${longitude}
- Number of People: ${people}
- Total Emission (kg CO2e): ${totalEmission}

Please analyze these characteristics and provide three key insights. Keep the response under 220 words.`;

    try {
        // 使用 Fetch API 发送 POST 请求
        const response = await fetch("https://api.openai.com/v1/chat/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                model: "gpt-4o", // 使用 OpenAI 的模型
                messages: [
                    { role: "system", content: "You are an expert in environmental science and sustainability. Please respond in English." },
                    { role: "user", content: userMessage },
                ],
                max_tokens: 1000 // 限制最大返回 token 数
            })
        });

        // 检查响应是否成功
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // 以下代码保留原有逻辑
        const data = await response.json();
        const content = data.choices[0].message.content || "Error: No response";

        // 格式化返回的内容
        const formattedContent = formatNumberedPoints(content);

        // 显示格式化后的内容
        document.getElementById("result").innerHTML = formattedContent;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").textContent = "Error: " + error.message;
    }
}






function validateNumber(input) {
    // 仅允许数字、小数点和负号
    input.value = input.value.replace(/[^0-9.-]/g, '');
    // 确保负号只能出现在开头
    if (input.value.indexOf('-') > 0) {
        input.value = input.value.replace('-', '');
    }
    // 确保小数点只出现一次
    const parts = input.value.split('.');
    if (parts.length > 2) {
        input.value = parts[0] + '.' + parts[1];
    }
}


// 函数：收集输入值，发送 POST 请求到 API，显示返回结果
async function alertInputValues() {
    // 获取所有输入框的值
    const siteEUI = document.getElementById("site-eui").value || "0";
    const gasIntensity = document.getElementById("gas-intensity").value || "0";
    const floorArea = document.getElementById("floor-area").value || "0";
    const electricityIntensity = document.getElementById("electricity-intensity").value || "0";
    const latitude = document.getElementById("latitude").value || "0";
    const longitude = document.getElementById("longitude").value || "0";
    const occpu = document.getElementById("occupants").value || "0";

    const requestBody = {

        "Site EUI (kBtu/ft²)": parseFloat(siteEUI),
        "Weather Normalized Site Natural Gas Intensity (therms/ft²)": parseFloat(gasIntensity),
        "Primary Property Use Type - Gross Floor Area (ft²)": parseFloat(floorArea),
        "Weather Normalized Site Electricity Intensity (kWh/ft²)": parseFloat(electricityIntensity),
        "Latitude": parseFloat(latitude),
        "Longitude": parseFloat(longitude)
    };

    

    try {
        // 使用 Fetch API 发送 POST 请求
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody)
        });

        // 检查响应是否成功
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // 解析响应为 JSON
        const responseData = await response.json();
        const pie = document.getElementById("pieChart");
        pie.style.display= 'none';
        per_people = responseData.prediction/occpu;
        per_quare =  responseData.prediction/floorArea;
        document.getElementById('prediction-value').innerText =  responseData.prediction.toFixed(2);


        getrepot1(siteEUI,gasIntensity,floorArea,electricityIntensity,latitude,longitude,occpu,responseData.prediction);
         

        var calculatorSection = document.getElementById('calculator-section');
        var ress = document.getElementById('res-section');
     
         
    
        var a = document.getElementById('home-section');
        a.style.display = 'none';
        
         
      setTimeout(function() {
        ress.classList.add('active');
        showContent('chart'); 
    
     }, 1200); 
    






    } catch (error) {
        // 捕获错误并显示
        alert(`Error: ${error.message}`);
    }
}











function showPopup() {
    document.getElementById('csvPopup').style.display = 'flex';
}

// 隐藏模态弹窗
function hidePopup() {
    document.getElementById('csvPopup').style.display = 'none';
}

// 验证 CSV 文件逻辑
function validateCsvFile() {
    const uploadedFile = document.getElementById('fileUploader').files[0];
    const validationMessage = document.getElementById('validationMessage');
    validationMessage.style.display = 'none'; // 隐藏消息

    if (!uploadedFile) {
        validationMessage.textContent = 'No file selected. Please upload a CSV file.';
        validationMessage.style.display = 'block';
        validationMessage.style.color = 'red';
        return; // 如果没有选择文件，直接退出
    }

    // 检查文件扩展名是否为 .csv
    if (!uploadedFile.name.endsWith('.csv')) {
        validationMessage.textContent = 'The uploaded file is not a valid CSV file.';
        validationMessage.style.display = 'block';
        validationMessage.style.color = 'red';
        return;
    }

    // 读取文件并验证内容
    const reader = new FileReader();
    reader.onload = function (event) {
        const content = event.target.result;
        const isValid = isValidCsv(content);

        if (isValid.status) {
            validationMessage.textContent = 'CSV file is valid!';
            validationMessage.style.color = 'green';
        } else {
            validationMessage.textContent = `Error: ${isValid.message}`;
            validationMessage.style.color = 'red';
        }
        validationMessage.style.display = 'block';
    };
    reader.readAsText(uploadedFile);
}

// 检查 CSV 文件的格式
function isValidCsv(content) {
    const rows = content.split('\n').map(row => row.trim());
    const expectedHeaders = [
        'Site EUI (kBtu/ft2)',
        'Weather Normalized Site Natural Gas Intensity (therms/ft2)',
        'Primary Property Use Type - Gross Floor Area (ft2)',
        'Weather Normalized Site Electricity Intensity (kWh/ft2)',
        'Latitude',
        'Longitude',
        'People'
    ]; // 根据标准表格的列名

    const headers = rows[0].split(',').map(header => header.trim());

    // 检查表头是否匹配
    if (!expectedHeaders.every((header, index) => headers[index] === header)) {
        return {
            status: false,
            message: 'Headers do not match the expected format. Expected: ' + expectedHeaders.join(', '),
        };
    }

    // 检查数据行数是否大于 1（至少要有一行数据）
    if (rows.length < 2) {
        return {
            status: false,
            message: 'The CSV file must contain at least one data row.',
        };
    }

    // 检查每行是否符合列数要求
    for (let i = 1; i < rows.length; i++) {
        const columns = rows[i].split(',').map(col => col.trim());
        
        // 跳过空行
        if (columns.length === 1 && columns[0] === '') {
            continue;
        }

        // 检查列数是否匹配
        if (columns.length !== expectedHeaders.length) {
            return {
                status: false,
                message: `Error: Row ${i + 1} does not match the expected column count. Found ${columns.length}, expected ${expectedHeaders.length}.`,
            };
        }
    }

    return { status: true, message: 'CSV is valid.' }; // 如果通过所有检查，返回 true
}







// 定义全局变量，用于存储七个特征值
 
let  siteEUI2, gasIntensity2, grossFloorArea2, electricityIntensity2, latitude2, longitude2,oupcity2;
function handleFileSubmit() {
    const uploadedFile = document.getElementById('fileUploader').files[0];
    const validationMessage = document.getElementById('validationMessage');
     
    if (!uploadedFile) {
        alert('Please select a CSV file to upload!');
        return;
    }

    if (validationMessage.textContent.includes('valid')) {
        // 读取并解析 CSV 文件
        const reader = new FileReader();
        reader.onload = function (e) {
            const content = e.target.result.trim(); // 去除多余空格和换行
            const rows = content.split('\n').map(row => row.split(',').map(col => col.trim())); // 分割行并解析列

            if (rows.length < 2) {
                alert('The CSV file does not contain enough data.');
                return;
            } 

            siteEUI2 = rows[1][0];
            gasIntensity2 = rows[1][1];
            grossFloorArea2 = rows[1][2];
            electricityIntensity2 = rows[1][3];
            latitude2 = rows[1][4];
            longitude2 = rows[1][5];
            oupcity2 = rows[1][6];

            alert(`Extracted Values:
                Site EUI: ${siteEUI2}
                Gas Intensity: ${gasIntensity2}
                Gross Floor Area: ${grossFloorArea2}
                Electricity Intensity: ${electricityIntensity2}
                Latitude: ${latitude2}
                Longitude: ${longitude2}
                People: ${oupcity2}`);
       
                alertInputValues1(siteEUI2,gasIntensity2,grossFloorArea2,electricityIntensity2,latitude2,longitude2,oupcity2);
             

             

            // 提取数据到对应的全局变量
      

            // 生成 alert 消息
        };



        reader.onerror = function () {
            alert('Unable to read the file. Please check the file format.');
        };

        reader.readAsText(uploadedFile); // 开始读取文件内容
    } else {
        alert('The CSV file is invalid. Please fix the errors before submitting.');
    }
}

// 工具函数：根据列名获取对应数据
function getValue(header, data, columnName) {
    const index = header.findIndex(h => h === columnName);
    return index !== -1 && data[index] ? data[index] : 'N/A'; // 如果未找到或值为空，返回 'N/A'
}









// 下载示例 CSV 文件
function downloadSampleCsv() {
    const downloadLink = document.createElement('a');
    downloadLink.href = 'demo 2.csv'; // 替换为你的示例文件路径
    downloadLink.download = 'demo-2.csv';
    downloadLink.click();
}



async function alertInputValues1(siteEUI2, gasIntensity2, grossFloorArea2, electricityIntensity2, latitude2, longitude2, oupcity2) {
    // 构建请求体
    const requestBody1 = {
        "Site EUI (kBtu/ft²)": parseFloat(siteEUI2) || 0,
        "Weather Normalized Site Natural Gas Intensity (therms/ft²)": parseFloat(gasIntensity2) || 0,
        "Primary Property Use Type - Gross Floor Area (ft²)": parseFloat(grossFloorArea2) || 0,
        "Weather Normalized Site Electricity Intensity (kWh/ft²)": parseFloat(electricityIntensity2) || 0,
        "Latitude": parseFloat(latitude2) || 0,
        "Longitude": parseFloat(longitude2) || 0
    };

  

    try {
        // 使用 Fetch API 发送 POST 请求
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody1)
        });

        // 检查响应是否成功
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // 解析响应为 JSON
        const responseData = await response.json();

        // 隐藏图表
        const pie = document.getElementById("pieChart");
        pie.style.display = 'none';

        // 计算每人和每平方的值
        per_people = responseData.prediction / oupcity2;
        per_quare = responseData.prediction / grossFloorArea2;

        // 显示预测结果

  
        document.getElementById('prediction-value').innerText = responseData.prediction.toFixed(2);
     

        // 调用其他函数进行报告生成
        getrepot1(siteEUI2, gasIntensity2, grossFloorArea2, electricityIntensity2, latitude2, longitude2, oupcity2, responseData.prediction);

        // 更新页面显示
        const calculatorSection = document.getElementById('calculator-section');
        const ress = document.getElementById('res-section');
        const homeSection = document.getElementById('home-section');

        homeSection.style.display = 'none';

        // 延迟显示结果区域
        setTimeout(function () {
            ress.classList.add('active');
            showContent('chart');
        }, 1200);

    } catch (error) {
        // 捕获并显示错误
        alert(`Error: ${error.message}`);
    }
}