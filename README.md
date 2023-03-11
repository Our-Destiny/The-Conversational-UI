<a href="#"><img width="100%" height="auto" src="https://github.com/Our-Destiny/The-Conversational-UI/blob/main/Assets/The-Conversational-UI-Wall.png" height="175px"/></a>


<p align="center">
    <img src="https://img.shields.io/badge/Build%20Date-2019%20Jun%2006-blue?style=social&logo=jabber">
    <img alt="Build" src="https://img.shields.io/badge/build-passed-success">
    <img alt="Contributors" src="https://img.shields.io/badge/contributors-2-blue">
    <img alt="Status" src="https://img.shields.io/badge/status-working-success">
    <img alt="Status" src="https://img.shields.io/badge/current%20release-v0.08%20to%20v0.1.0-informational">
    <img alt="Status" src="https://img.shields.io/badge/progress-discontinued-important">
</p>


# A Conversational User Interface For Destiny

> Disclaimer : `There won't be source code releases for the newer versions.` Project Destiny is not an open-sourced Project, and you will be only witnessing the results and milestones of development that we have and are yet to be completed. Thank You.


`This repository contains the first phase of basic rule-based skeleton integrated into a simple light weight GUI for Destiny.`

---

A Python based simple Personal Assistant with majour step taken in the development of GUI for Project Destiny.
In this respo, you will be looking at the basic skelton with some shell commands and its corresponding responses integrated into a electron app build using Node.js.
In theory, Destiny is an Autonomus Artificial Intelligence Based Digital Assistant designed to
enhance human life and ensure privacy to data and security to life.
Evolution is the version control for this project. 
Introduces new terms for backend and frontend.

Backend Is Called : Destiny Mainframe.
Frontend Is Called : Destiny Framework.

---

## Code Organization

    ├── config.py          <- Configuration file with data directories and hyperparamters to train the model
    ├── data_loader.py     <- Define an iterator who collects batches of data to train the model
    ├── eval.py            <- Evaluate the model on a new pair of (context, question)
    ├── layers.py          <- Define the various layers to be used by the main BiDAF model
    ├── make_dataset.py    <- Download the SquAD dataset and pre-process the data for training
    ├── model.py.          <- Define the BiDAF model architecture
    ├── requirements.txt   <- Required Python libraries to build the project
    ├── test.py            <- Test the performance of a trained model on the DEV dataset
    ├── train.py           <- Train a model using the TRAIN dataset only
    ├── utils.py           <- Group a bunch of useful functions to process the data

---

## Built-in Commands

```
DESTINY | HONEY
WHATS THE TIME
PLAY MUSIC
THANK YOU
SHUTDOWN
RESTART
CHATTERBOT - COMMANDS (FOR NATURAL CONVERSATION) | CHATTERBOT CORPUS COMMANDS
BYE | QUIT
```
---

## Features

- `Cross-platform` targeted design configuration.
- Simple speech engine and easy to configure.
- `Sapi5` voice support.
- Uses `Ivona Text To Speech Engine` Voices.
- `Works Completely Offline.`
- Threaded Speech with Printing on command line.
- Adaptive Hotword Reply (Greet By Time).
- Added Shell Commands (Trial for system integrated functions like - Shutdown & Restart).
- GUI - `Designed For Crossplatform usages.`
- `Transparent GUI` (So it doesnt block your vision and can keep u occupied with your work).
- GUI design is clean and made compact ready with `Minimal System Resourse Usages.`
- GUI - `Responsive Buttons.`

---




## Prerequisite Installation

**Install Python Version 3.7.6 - 64Bit Interpreter**

```bash
https://www.python.org/downloads/release/python-376/

```
**Pip Command to install the Library used for Text-to-Speech**

```bash
pip install pyttsx3==2.7

```
**Download IVONA 2 Salli - US English female voice [22kHz]**
```bash
https://nextup.com/ivona/

```
**Download Node.js - For Windows**
```bash
https://nodejs.org/en/download/

```
**Download Electron.js - For Windows**
```bash
https://www.electronjs.org/

```
**Install necessary packages using NPM from the project Folder**
```bash
npm install

```
**After the complete installation of the required modules, runn the following command to Kick-Start the GUI**
```bash
npm start

```
---


## Screenshots

![App Screenshot](https://github.com/ODRDLabs/Destiny-Version-0.0.8-0.0.9-0.1.0/blob/main/Screeshots/Test_1.jpg)

**>GUI Basic Appearence**

## Feature And Performance Test Results

![App Screenshot](https://github.com/ODRDLabs/Destiny-Version-0.0.8-0.0.9-0.1.0/blob/main/Screeshots/Test_2.png)

![App Screenshot](https://github.com/ODRDLabs/Destiny-Version-0.0.8-0.0.9-0.1.0/blob/main/Screeshots/Test_3.png)

**>Responsive Buttons**

![App Screenshot](https://github.com/ODRDLabs/Destiny-Version-0.0.8-0.0.9-0.1.0/blob/main/Screeshots/Test_4.png)

**>Resources Usage Test**

![App Screenshot](https://github.com/ODRDLabs/Destiny-Version-0.0.8-0.0.9-0.1.0/blob/main/Screeshots/Test_5.png)

**>Transparency Test**

## Supported Environments

|                         |                                         |
|-------------------------|-----------------------------------------|
| **Operating systems**   | Linux & Windows                         |
| **Python versions**     | Python 3.7.6 (64-bit)                   |
| **Distros**             | Ubuntu, Windows 8, 8.1 Pro, 10 (All Distros)         |
| **Package managers**    | APT, pip                                |
| **Languages**           | English                                 |
| **System requirements** | 2GB of free RAM, Intel i3 - Any Higher  |
|                         |                                         |

---

> ***And The Journey Of Our Destiny Continues....***
