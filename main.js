// Modules to control application life and create native browser window

// DESTINY Autonimous Artificial Intelligence Programme (Python 3).
// Copyright (c) 2012 - End Of Times | OUR DESTINY (A.A.I) Research And Development Labs,Inc.
// All rights reserved. This software or any portion thereof may not be reproduced or used in any manner whatsoever without the development permission of the ODRE Labs, Inc.
// Permission for the development of the software is Authorized ONLY for the developers of ODRD Labs, Inc.
// Author: OUR DESTINY (A.A.I) Research And Development Labs <hariprasad@ODRDLabs>|<ribin@ODRDLabs>

const {app, BrowserWindow, Tray} = require('electron')
const path = require('path')

function createWindow () {
  const appIcon = new Tray('./GUI/images/icon.png')
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 400,
    height: 650,
    center: true,
    icon: './GUI/images/icon.png',
    transparent:true,
    frame: false,
    resizable: false,
    webPreferences: {
      preload: path.join(__dirname, '/GUI/js/', 'preload.js'), nodeIntegration: true}
  })

  
  // and load the index.html of the app.
  mainWindow.loadFile('./GUI/index.html')

  // Open the DevTools.
  // mainWindow.webContents.openDevTools()
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', function () {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', function () {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) createWindow()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
