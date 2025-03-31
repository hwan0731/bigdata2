import requests

def get_melon_chart():
    url = "https://www.melon.com/chart/index.htm"  # 멜론 차트 페이지 URI
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Referer": "https://www.melon.com/",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 요청이 성공했는지 확인

        print("요청 성공!")
        # 응답 내용을 출력하거나 처리
        print(response.text[:500])  # 응답 내용의 처음 500자를 출력

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP 에러 발생: {http_err}")
    except Exception as err:
        print(f"기타 에러 발생: {err}")

if __name__ == "__main__":
    get_melon_chart()

#lst50 
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a

import requests
from bs4 import BeautifulSoup

def get_melon_chart():
    url = "https://www.melon.com/chart/index.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 차트 리스트 찾기
        chart_list = soup.find_all('tr', class_=['lst50', 'lst100'])

        for song in chart_list:
            rank = song.find('span', class_='rank').text
            title = song.find('div', class_='ellipsis rank01').find('a').text
            artist = song.find('div', class_='ellipsis rank02').find('a').text
            
            print(f"Rank: {rank}, Title: {title}, Artist: {artist}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP 에러 발생: {http_err}")
    except Exception as err:
        print(f"기타 에러 발생: {err}")

if __name__ == "__main__":
    get_melon_chart()

#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a

