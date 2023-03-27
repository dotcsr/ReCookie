import browser_cookie3

def find_cookie_facebook(browser):
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

    session_cookies = []
    session_id = cookies._cookies.get('.facebook.com', {}).get('/', {}).get('c_user')
    if session_id:
        c_user_cookie = cookies._cookies['.facebook.com']['/']['c_user']
        cookie_value = c_user_cookie.value
        session_cookies.append(("c_user", cookie_value))
        
    session_id = cookies._cookies.get('.facebook.com', {}).get('/', {}).get('xs')
    if session_id:
        xs_cookie = cookies._cookies['.facebook.com']['/']['xs']
        cookie_value = xs_cookie.value
        session_cookies.append(("xs", cookie_value))

    if session_cookies:
        return session_cookies