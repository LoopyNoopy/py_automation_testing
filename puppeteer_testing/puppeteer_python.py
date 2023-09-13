import js2py
import subprocess
import os

#code_2 = "function f(x) {return x+x;}"
#res_2 = js2py.eval_js(code_2)

#print(res_2(5))

#eval_res, tempfile = js2py.run_file("hey.js")
#tempfile.wish("GeeksforGeeks")

print("Installing nodeJS LTS")
os.system("winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements")
print("Upgrading Node Package Manager to latest")
os.system("npm install --global npm")
print("Installing Node Package eXecute")
os.system("npm install -g npx")
print("Installing puppeteer")
os.system("npm i puppeteer")
print("Installing puppeteer browsers cli")
os.system("npm i @puppeteer/browsers")
print("Installed packages")
os.system("npm list")
print("Installing Firefox through puppeteer")
os.system("npx @puppeteer/browsers install firefox")
print("Installing Chrome through puppeteer")
os.system("npx @puppeteer/browsers install chrome")
print("Installing Chrome through puppeteer")
os.system("npx @puppeteer/browsers install chromedriver")
#subprocess.call("cmd","ls")