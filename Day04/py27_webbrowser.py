import webbrowser

print(webbrowser.get())

url = 'http://www.naver.com'
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)