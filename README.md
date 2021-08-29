# pylance_dash_issue_demo

Demonstrates the following Pylance issue:

https://github.com/microsoft/pylance-release/issues/1255

Steps to repro:

1. Set Pylance as Python Language Server in VSCode
2. Open `app.py` in VSCode
3. Run `app.py` -> all works as expected but Pylance highlights the list concatenation step
