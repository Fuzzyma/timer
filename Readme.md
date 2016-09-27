# timer (designed for "tribal wars")

A handy tool, to simplify time calculations - in special: Addition and subtraction of time. 

## Install

### Clone repository

```bash
git clone https://github.com/Fuzzyma/timer
```

### Check Requirements

- do you have linux? Read [Step 2](#2-install-python-on-linux)
- do you have Win10 64bit? Read [Step 3](#3-install-win-bash-only-64-bit)
- do you have any other windows? Read [Step 1](#1-install-python-on-windows)

### 1. Install Python on windows

In order to execute python files you need python installed on your computer. This script needs python 2.7.
You can download it [here](https://www.python.org/downloads/).
Follow the instructions and add python to your path (should be checked automatically).

You can now run the script with `python timer.py param1 param2 param3`.
Read more at [Usage](#usage).


### 2. Install Python on linux

First check if it is already installed with `python --version`. It should print your python version which has to be 2.7.
In case you have a newer python you may install 2.7. in parallel.
Linux user can do that on their own :P.
Proceed at [step 4](#4-setup-a-bash-alias)

### 3. Install Win Bash (only 64 bit)

You did that already? Go to [step 4](#4-setup-a-bash-alias)

- Install the newest update (version 1607).
- Go to Settings > Update & Security > For Developers > Activate the "Developer Mode"
- Go to Control Panel > Programs > Turn Windows Features On or Off > Check "Windows Subsystem for Linux (Beta)"
- Wait until its installed
- Go to [step 4](#4-setup-a-bash-alias)

### 4. Setup a bash alias

Open a bash terminal and type

```
vim ~/.bashrc
```

Press "i" for insert mode and add the following line:

```
alias t="python /path/to/timer.py"
```

Press `Esc` and `:x` to save. Source your `.bashrc` with `. ~/.bashrc`.

In win10 bash your filesystem is mounted in `/mnt` so e.g. `C:\\Program Files\timer\timer.py` gets translated to
`/mnt/c/Program\ Files\timer.py`


## Usage

Open a bash terminal.

_When you don't have linux or win10 bash, you have to replace "t" with "python /path/to/timer.py"_

```bash
# Addition

t 12:00:00 + 10:10:00 + 1:1:2
# you can skip the +
t 12:00:00 10:10:00 1:1:2
# you can also skip minutes and seconds if you dont need them
t 12 10:10 1:1:2

# All prints: 23:11:02

# Subtraction
t 12:00:00 - 10:10:00  # prints 1:50:00

# All together of course (not that we dont have to write the +)
t 12 - 2:30 4:0:20 - 4:50 3  # prints 11:40:20
```

**You can also use one of `[.,/-_]` as separator instead of `:` (e.g. `h,m,s` instead of `hh:mm:ss`)**
