<h1 align="center">[Discord] - GroupLocker</h1>
<p align="center">
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.9-informational.svg">
  </a>
  <a href="https://github.com/AstraaDev">
    <img src="https://img.shields.io/github/repo-size/AstraaDev/Discord-GroupLocker.svg?label=Repo%20size&style=flat-square">
  </a>
</p>

<p align="center">
  [Discord] - GroupLocker allows you to Lock the entry and exit of a Discord group.
</p>

## Features

- [x] - [Lock joins](https://github.com/AstraaDev/Discord-GroupLocker) - Automatically kick the person if they join the group.
- [x] - [Lock leaves](https://github.com/moom825/Discord-GroupLocker) - Automatically re-adds the person if they leave the group.

## How To Setup/Install

#### First of all please set a prefix in the config.json file!
```json
{
    "token": "TOKEN-HERE", 
    "prefix": "PREFIX-HERE"
}
```

#### 1st・Installation (Automated installation)
```
Launch the setup.bat file. A new file will be created. You will only have to launch it.
```

#### 2nd・Installation (Manual installation)
```
$ git clone https://github.com/AstraaDev/Discord-GroupLocker.git
$ python -m pip install -r requirements.txt
$ python selfbot.py
```
