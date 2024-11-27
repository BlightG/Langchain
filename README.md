# LangChain

This repository is an implementation using langchain and a two models from huging face to create a CLI tool that can create SQL queries or translate a given SQL query

to start the CLI tool

clone the repo

```sh
git clone https://github.com/BlightG/Langchain
```

Install all required dependanceis
```sh
pip install -r requirments.txt
```

create an env file and add the following key with your hugging face token
```
HUGGINGFACE_TOKEN="<your HUggingFace token>"
```

then run the tool

```sh
python sqllang.py
```

it will ask you
```
Do you want to generate SQL query or translate query to english? (sql/english):
```

if you chose sql the service will generate an sql query given a text input

if you chose english the service will generate explanation of a given sql input

afte the it will ask if
```
Do you want to switch query types? (yes/no):
```

depending on your choice you can either continue with what you are doing or choose the opposite

you can exit the tool anytime by typing
```
exit
```
