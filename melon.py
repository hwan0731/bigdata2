from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Chrome 드라이버 경로 설정
chrome_driver_path = '/path/to/chromedriver'

# ChromeOptions 객체 생성
chrome_options = Options()
chrome_options.add_argument('--headless')  # 브라우저 창을 띄우지 않음

# 드라이버 서비스 객체 생성
service = Service(chrome_driver_path)

# 웹 드라이버 생성
driver = webdriver.Chrome(service=service, options=chrome_options)

# 멜론 차트 페이지로 이동
driver.get('https://www.melon.com/chart/index.htm')

# 순위, 곡명, 아티스트를 담을 리스트 초기화
rankings = []

# 100위까지의 데이터를 수집
for i in range(1, 101):
    # 순위 번호
    rank = i
    
    # 곡명
    song_xpath = f'//*[@id="lst50"]/td[4]/div/div/div[1]/span/a'
    song_title = driver.find_elements(By.XPATH, song_xpath)[i-1].text
    
    # 아티스트명
    artist_xpath = f'//*[@id="lst50"]/td[4]/div/div/div[2]/a'
    artist_name = driver.find_elements(By.XPATH, artist_xpath)[i-1].text
    
    # 리스트에 정보 추가
    rankings.append({'rank': rank, 'title': song_title, 'artist': artist_name})

# 웹 드라이버 종료
driver.quit()

# 수집한 데이터 출력
for ranking in rankings:
    print(f"{ranking['rank']}위: {ranking['title']} - {ranking['artist']}")
    pip install selenium

ai_song = random.choice(songs)
print(f"추천곡은 {ai_song[1]} - {ai_song[2]} 입니다."