# AChurch Interpreter by Hugo Aranda Sánchez

## Description

This is a lambda calculus interpreter telegram bot named @AChurch_HugoBot developed for a project recuested at the LP (Programming Languages) course taken on spring 2022-23 using antlr4 and python.

As the initial description tells this telegram bot will be able to recive some lambda calculus expressions and evaluate them with the needed alpha and beta reductions.

If you are not familiar with lambda calculus I recommend giving a thorough look to this [lambda calculus](http://www-cs-students.stanford.edu/~blynn/lambda/) webpage.

It has some simple features like macros (and infix macros for some limited non-alphabetic characters) and expression tree printing via `pydot`.



## Installation

For installation we will need a bunch of python packages all managed by the package manager [pip](https://pip.pypa.io/en/stable/) and some other programs installed by normal means.

The installation rundown will be described for linux users (ubuntu/debian in particular) since it's the machine on which I developed the app.

### Requirements

Some basic (and to be expected) requirements are `python3` and `pip`

### Install instructions

For antlr4 support you will need(the project runs on version `4.13.0` of `antlr4`):

```bash
sudo apt install antlr4
pip install antlr4-tools
pip install antlr4-python3-runtime
```

On my course slides they didn't specify installing antlr through sudo apt but without it it wouldn't work

One problem you can encounter (I did) is having a different version of antrl4 than the version installed by pip of the runtime, to correct that you need to reinstall the pip packages with:

```bash
pip uninstall antlr4-python3-runtime
pip install antlr4-python3-runtime==<ANTLR version>
```
You can check the antlr4 version that you are running with `antlr4`

For telegram support you will need (the project runs on version `20.3`):

```bash
pip install python-telegram-bot
```

Finally for pydot support you will need (the project runs on version `1.4.2` of `pydot`):

```bash
pip install pydot
sudo apt install graphviz
```


## Usage

### Launching and generating files

When you unpack the directory you'll be greeted by only 4 files (including this `README.md`):

`achurch.py` with all the python programming needed for this project to work.

`lc.g4` with the grammar that describes the expressions accepted by the interpreter.

`Makefile` with a couple of ways to execute the project and a clean method (to simplify working on the app and make working with git easier)

As strongly recommended by the course (LP) on my submission I will skip the Makefile and describe the needed instructions to execute the project here.

To execute you will need:

```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor lc.g4
python3 achurch.py
```

The first instruction will generate the Lexers, Parsers and Visitors automatically with the grammar description at `lc.g4`.

And the second one will execute the `python` code that will launch the telegram bot.

Also to clean all the trash generated this will help you a lot:

```bash
rm -rf *.interp *.tokens *Parser.py *Visitor.py *Lexer.py __pycache__ .antlr *.png
```

### Interacting with the bot

While the python code is running you can interact with the bot via the telegram chat `@AChurch_HugoBot`.

In order to start communicating with the bot you'll need to use the `/start` command

The bot has a self explainatory `/help` command that hints all the commands and inline options the bot offers but I will explain them here in more detail.

There is an `/author` command that shows as it is to be expected the author of the bot and date of latest relase.

There is a `/macros` command to show the macros that the interpreter has on memory at the moment.

There is a `/maxsteps` command to show how many beta steps will be done untill giving up on the expression and a `/setsteps <NUM_STEPS>` commands to change that setting.

There are `/showsteps` and `/hidesteps` commands in order to set up if you want to see the middle steps of a given evaluation or keep them private (if you are maybe using this to study or just check and don't want the process to be spoiled to you)

Finally the inline options (no command) are basically two:
    -A lambda calculus expression to be evaluated with variables as [a-z] characters and lambdas as `\` or `λ`
    -A macro or infix macro to be registered with sintax `MACROINCAPS =|≡ lambda calculus expression


## Project status

Might develop a bit further into the interpreter later on the summer if I feel like it to add some more complex tools

