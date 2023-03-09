// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.
console.log("Renderer started");
let {PythonShell} = require('python-shell')
var sqlite3 = require('sqlite3').verbose();

//const { ipcRenderer} = require('electron')

var form = document.getElementById("myForm");
function handleForm(event) { event.preventDefault();
        var x = document.getElementById("in").value;
        var y = document.getElementById("texty1");
        document.getElementById("texty0").innerHTML= y.innerHTML;
         document.getElementById("texty1").innerHTML= "___";
        run_py(x); 
        setTimeout(() => readDb(), 800);  
        document.getElementById("in").value="";
} 
form.addEventListener('submit', handleForm);


function readDb(){
    let db = new sqlite3.Database('./GUI/js/returnResp.sqlite');
    db.all("SELECT input,output FROM response", function(err, rows) {
            rows.forEach(function (row) {
                document.getElementById("texty1").innerHTML= row.output//console.log(row.input, row.output);
            })
        });	
    db.close();
}

function run_py(x){
    let options = {
        mode: 'text',
        encode: 'utf8',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: './Destiny_Mainframe/',
        args: [x]
    };
      
    let shell = new PythonShell('Destiny_User_Custom_Input.py', options);
    shell.on('message', function (message) {
        //console.log(message);// handle message (a line of text from stdout)
    });
}