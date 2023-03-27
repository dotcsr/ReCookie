import os

browsers_list =[]

def validateBrowsers():
    Chrome_Path = "C:\Program Files\Google\Chrome\Application"
    if os.path.isdir(Chrome_Path):
        browsers_list.append("Chrome")

    Edge_Path = "C:\Program Files (x86)\Microsoft\Edge\Application"
    if os.path.isdir(Edge_Path):
        browsers_list.append("Edge")

    firefox_Path = "C:\Program Files\Mozilla Firefox"
    if os.path.isdir(firefox_Path):
        browsers_list.append("Firefox")

    usuario_actual = os.getlogin()
    OperaGx_Path = "C:\\Users\\" + usuario_actual + "\\AppData\\Local\\Programs\\Opera GX"
    if os.path.isdir(OperaGx_Path):
        browsers_list.append("OperaGX")

    usuario_actual = os.getlogin()
    Opera_Path = "C:\\Users\\" + usuario_actual + "\\AppData\\Local\\Programs\\Opera"
    if os.path.isdir(Opera_Path):
        browsers_list.append("Opera")

    Brave_Path = "C:\Program Files\BraveSoftware\Brave-Browser\Application"
    if os.path.isdir(Brave_Path):
        browsers_list.append("Brave")

    return browsers_list