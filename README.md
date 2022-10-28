# <AppName> will be named later
<AppName> is a user-friendly python script that allows users to generate an HTML file by pointing to a directory. The app works on both Windows and Linux. <AppName> is a fork of the [DiogenesList](https://github.com/ZapperDJ/DiogenesList) and [Snap2HTML](https://www.rlvision.com/snap2html/) that aims to fix bugs and improve the code in certain areas. In addition, <AppName> develop a function to identify the file status.


## Requirements

- Python 3.9+
- Works on both Linux and Windows
- Faster then Snap2HTML
- 

The script will output a html file thats similar to Snap2HTML


## Installation
First install PIP on Windows or Linux. 


###Linux
```
    #Ubuntu
    $ apt install python-pip
    
    #Fedora
    $ dnf install python3-pip
    
    #Arch
    $ pacman -S python-pip
    
    #Installing Appname
    pip install Appname
```

###Windows 
PIP is installed by default [Python](https://www.python.org/downloads/windows/) on Windows. Make sure to add python to your $PATH.
```
    pip install 'AppName'
```

## Using AppName
The app will take in two arguments. The first one is the path to the directory that you want to scan. The final argument is the output HTML file.
```
    appname -p PathToDirectory -o output
    
    #Options
    -h, --help      Help message
    -p, --path      Path to directory being scanned
    -o, --output    Name of the HTML output file (without .html)
```
    








