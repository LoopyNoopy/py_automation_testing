import js2py
import subprocess
import os

#code_2 = "function f(x) {return x+x;}"
#res_2 = js2py.eval_js(code_2)

#print(res_2(5))

#eval_res, tempfile = js2py.run_file("hey.js")
#tempfile.wish("GeeksforGeeks")

install_puppeteer_commands = ["winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements",
                              "npm install --global npm",
                              "npm install -g npx",
                              "npm i puppeteer",
                              "npm i @puppeteer/browsers"]
for command in install_puppeteer_commands:
    os.system(command)
print("Installing Firefox through puppeteer")
os.system("npx @puppeteer/browsers install firefox")
print("Installing Chrome through puppeteer")
os.system("npx @puppeteer/browsers install chrome")
print("Installing Chrome through puppeteer")
os.system("npx @puppeteer/browsers install chromedriver")
#subprocess.call("cmd","ls")