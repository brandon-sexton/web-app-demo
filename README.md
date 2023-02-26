# web-app-demo
Simple example repo for running a web application with Dash

## "Git" started
- If not already created, create a folder on your machine used for development (ex. C:\dev\)
- Open a terminal and navigate to this folder
- Once inside the folder, issue the following command in the terminal
```shell
git clone https://github.com/brandon-sexton/web-app-demo
```

## Dependencies
- Open a terminal and issue the following command
```shell
pip install dash dash-bootstrap-components
```
- Wait for a terminal message that says packages were successfully installed

## Run example
- Open a terminal and navigate to the project director where app.py resides
- Issue the following command in the terminal
```shell
python ./app.py
```
- A browser should automatically open where results can be referenced with code

## Structure
- src\web_app_demo may seem unnecessary, but it makes the project more distributable if you so choose
- src\web_app_demo\assets is empty but should hold custom style sheets or images
