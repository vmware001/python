import requests
import random
import string
from concurrent.futures import ThreadPoolExecutor

url_template = "https://82k3.work/wd/lateron.asp?ud=1882&t5={}&t3={}&zt=on"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Referer": "https://82k3.work/wd/?ud=1882",
    "Sec-Ch-Ua": '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Platform": '"Android"',
    "Sec-Fetch-Dest": "iframe",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "no-cache"
}

def generate_t5():
    first_digit = random.choice(string.digits[1:])
    remaining_digits = ''.join(random.choices(string.digits, k=9)) 
    return first_digit + remaining_digits

def generate_t3():
    allowed_chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    length = random.randint(8, 14)
    return ''.join(random.choices(allowed_chars, k=length))

def generate_random_cookie():
    return f"ASPSESSIONIDAABRTATD={''.join(random.choices(string.ascii_uppercase + string.digits, k=16))}; path=/"

def send_request(index, session):
    t5 = generate_t5()
    t3 = generate_t3()
    url = url_template.format(t5, t3)
    session.cookies.set('ASPSESSIONIDAABRTATD', generate_random_cookie())

    try:
        response = session.get(url, headers=headers)
        print(f"Request {index} sent with t5={t5} and t3={t3}, Status Code: {response.status_code}")
    except Exception as e:
        print(f"Request {index} failed with error: {e}")

def main():
    loop_count = 1000000
    session = requests.Session()
    with ThreadPoolExecutor(max_workers=20) as executor:
        for i in range(1, loop_count + 1):
            executor.submit(send_request, i, session)

if __name__ == "__main__":
    main()
