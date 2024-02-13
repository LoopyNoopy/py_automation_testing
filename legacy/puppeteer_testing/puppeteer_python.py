import js2py
import subprocess
import os

#code_2 = "function f(x) {return x+x;}"
#res_2 = js2py.eval_js(code_2)

#print(res_2(5))

#eval_res, tempfile = js2py.run_file("hey.js")
#tempfile.wish("GeeksforGeeks")
def install_browsers():
    install_puppeteer_commands = ["winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements",
                              "npm install --global npm",
                              "npm install -g npx",
                              "npm i puppeteer",
                              "npm i @puppeteer/browsers",
                              "npx @puppeteer/browsers install firefox",
                              "npx @puppeteer/browsers install chrome",
                              "npx @puppeteer/browsers install chromedriver"]
    for command in install_puppeteer_commands:
        os.system(command)

#subprocess.call("cmd","ls")