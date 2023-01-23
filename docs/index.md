# Welcome to spuring documentation

Spuring creates predefined folder setups. It is mainly mend to be a project folder scaffolder for python projects, but thanks to the template ans plugin system you can customize it for your needs.

## Install

```bash
py -m pip install spruing
```

## How to use it

### Help
```bash
spruing -h
```

shows a list commands

### List Templates
```bash
spruing -l
```

list all templates that are in your template folder (more later)

### Create a Template
```bash
spruing -t default -o MyProject
```

Creates the content of the default template in the folder MyProject.

This will create the following folder tree
```bash
│─── README.md
│─── requirements-dev.txt
│
├─── .venv
├─── MyProject
│       __init__.py
│
└─── test
        TestMyproject.py
```
You only can just start the virtual environment and start coding.
All the packages in the requirements-dev.txt already downloaded and ready to use.  

### Find the template folder

As i said, you can customize your own template. 

First thinks first. Lets locate the template folder.

Type the following in you terminal
```bash
spuring -tp
```

The result should be on windows like that

`C:\Users\%user%\AppData\Local\Programs\Python\Python3%$\Lib\site-packages\spuring\templates`

For later - You will found the plugin folder (here named "scripts") on the parent directory. 

`C:\Users\%user%\AppData\Local\Programs\Python\Python3%$\Lib\site-packages\spuring\scripts`

## Create a simple template

There are 4 main sections for a template. Lets create a toml file and lets right the "head" section.

```toml
# The name for your template
name = "my_template"

# a short description. 
description = "A project setup that i like"

# In the narrative you can write a little bit more, so that you know late what going on.
narrative = "I use a src folder. It's much better!"

```

That was the first part. Now lets dive in the second section. Its the folder section.

```toml
# Here can you list all folders
# now we start with the folder flag. That wasn't needed in the first section
[folders]
# the name of the key isn't important
src = "src"
# you can create multi layers
test = "test/test-reports"
```

Just start the section with `[folders]`.
After that choose any key, it is not important for the creation of the project file. Only double occurrence play a role. This could be important if you work with more advance stuff. But now low go forward to the files. Now it will be interesting.



