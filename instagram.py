import browser_cookie3

def find_cookie_instagram(browser):
    if browser == "Chrome":
        cookies = browser_cookie3.chrome()
    elif browser == "Firefox":
        cookies = browser_cookie3.firefox()
    elif browser == "Opera":
        cookies = browser_cookie3.opera()
    elif browser == "Edge":
        cookies = browser_cookie3.edge()
    elif browser == "OperaGX":
        cookies = browser_cookie3.opera_gx()
    elif browser == "Brave":
        cookies = browser_cookie3.brave()
    else:
        return "Navegador no válido"

    session_id = cookies._cookies.get('.instagram.com', {}).get('/', {}).get('sessionid')
    if session_id:
        session_cookie = cookies._cookies['.instagram.com']['/']['sessionid']
        cookie_value = session_cookie.value
        return cookie_value