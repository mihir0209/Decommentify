# Decommentify
Decomment the whole file in vscode with a simple shortcut <br>
Currently, this supports languages given below:<br>
Python, C, C++, H, Java, JavaScript, C#, SQL, HTML, Ruby, Haskell <br> <br>
#Usage:
----
You have to follow these steps to copy and paste some additional things to your VSCode settings:
Important: You have to change the path mentioned below to where you have downloaded the file.
## If you want to run the exe directly (with no personal modifications of yours):
1. Download the `decommentify.exe` file directly
2. If you'd like to change the file's location, please do it in this step only.
3. Steps for tasks and Keybinding editing in vscode:
     1.  In VSCode, press `Ctrl + Shift + P` to open the command palette.
     2.  Type `Tasks` and find `Configure default build task` and click on it [This should open tasks.json, if it isn't opening one, create with a `template` directly and select `others` in it.]
     3.  After opening tasks.json paste the below given tasks.json there:<br>
          Don't forget to add extra {} if there exists one task already and also add a comma after the {} (as per the JSON file format) <br>
     4. After pasting this, add keybindings for vscode:
          1. In VSCode, press `Ctrl + Shift + P` to open the command palette.
          2.  Type `Preferences` and find `Open Keyboard Shortcuts (JSON)` and click on it [This should open keybindings.json]
          3.  Paste the given for keybindings.json with the same instructions:

## Tasks.json

```json
{
    "label": "Decommentification",
    "type": "shell",
    "command": "cmd",
            "args": [
                "/c", 
                "echo Author: MiHiR && C:\\Path To Your\\decommentify.exe",
                "${file}"
            ],
    "group": {
        "kind": "build",
        "isDefault": true
    },
    "problemMatcher": [],
    "presentation": {
        "reveal": "always",
        "panel": "shared",
        "clear": true
    }
}
```
## Keybindings.json
```json
{
        "key": "ctrl+h",
        "command": "workbench.action.tasks.runTask",
        "args": "Decommentification",
        "when": "editorTextFocus"
    }
```


## If you want to have the python code (with personal modifications for the code):
1. Download the `decommentify.py` file directly
2. If you'd like to change the file's location, please do it in this step only.
3. You can change the behaviour of the code in the python file directly.
4. Steps for tasks and Keybinding editing in vscode:
     1.  In VSCode, press `Ctrl + Shift + P` to open the command palette.
     2.  Type `Tasks` and find `Configure default build task` and click on it [This should open tasks.json, if it isn't opening one, create with a `template` directly and select `others` in it.]
     3.  After opening tasks.json paste the below given tasks.json there:<br>
          Don't forget to add extra {} if there exists one task already and also add a comma after the {} (as per the JSON file format) <br>
     4. After pasting this, add keybindings for vscode:
          1. In VSCode, press `Ctrl + Shift + P` to open the command palette.
          2.  Type `Preferences` and find `Open Keyboard Shortcuts (JSON)` and click on it [This should open keybindings.json]
          3.  Paste the given for keybindings.json with the same instructions
          4.  Well, you can change the shortcut for this task on your own, just change the key: ctrl+e to something you would like to have.

## Tasks.json

```json
{
    "label": "Decommentify",
    "type": "shell",
    "command": "cmd",
            "args": [
                "/c", 
                "echo Author: MiHiR && C:\\Path To Your\\decommentify.py",
                "${file}"
            ],
    "group": {
        "kind": "build",
        "isDefault": true
    },
    "problemMatcher": [],
    "presentation": {
        "reveal": "always",
        "panel": "shared",
        "clear": true
    }
}
```
## Keybindings.json
```json
{
        "key": "ctrl+e",
        "command": "workbench.action.tasks.runTask",
        "args": "Decommentify",
        "when": "editorTextFocus"
    }
```
 
