// All of the Node.js APIs are available in the preload process.
// It has the same sandbox as a Chrome extension.

// DESTINY Autonimous Artificial Intelligence Programme (Python 3).
// Copyright (c) 2012 - End Of Times | OUR DESTINY (A.A.I) Research And Development Labs,Inc.
// All rights reserved. This software or any portion thereof may not be reproduced or used in any manner whatsoever without the development permission of the ODRE Labs, Inc.
// Permission for the development of the software is Authorized ONLY for the developers of ODRD Labs, Inc.
// Author: OUR DESTINY (A.A.I) Research And Development Labs <hariprasad@ODRDLabs>|<ribin@ODRDLabs>'''

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
