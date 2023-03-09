// All of the Node.js APIs are available in the preload process.
// It has the same sandbox as a Chrome extension.
console.log("preload started");
let {PythonShell} = require('python-shell')
 let options = {
        mode: 'text',
        encode: 'utf8',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: './Destiny_Mainframe/',
        args: []
    };
      
    let shell = new PythonShell('Destiny_Intro.py', options);
    shell.on('message', function (message) {
        //console.log(message)// handle message (a line of text from stdout)
    });

window.onload = function() {
    const {remote} = require('electron');
    const {BrowserWindow} = remote;
    const win = BrowserWindow.getFocusedWindow();
    
    document.getElementById("close-window-button").onclick = function() {
      win.close();
    }
    document.getElementById("minimize-window-button").onclick = function() {
      win.minimize();
      console.log("window minimized");
   }
  }