import requests
from bs4 import BeautifulSoup

# KBO 웹사이트의 팀 순위 페이지 URL
url = 'https://www.koreabaseball.com/TeamRank/TeamRank.aspx'

# 웹 페이지에 HTTP 요청 보내기
response = requests.get(url)

# 요청이 성공적으로 완료되었는지 확인
if response.status_code == 200:
    # HTML 콘텐츠 파싱
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 팀 순위 테이블 찾기
    table = soup.find('table', {'class': 'tData'})
    
    # 테이블의 각 행을 탐색하여 데이터 추출
    if table:
        for row in table.find_all('tr')[1:]:  # 첫 번째 행은 헤더이므로 제외
            columns = row.find_all('td')
            if columns:
                rank = columns[0].get_text(strip=True)  # 순위
                team = columns[1].get_text(strip=True)  # 팀 이름
                games = columns[2].get_text(strip=True)  # 경기 수
                wins = columns[3].get_text(strip=True)  # 승
                losses = columns[4].get_text(strip=True)  # 패
                draws = columns[5].get_text(strip=True)  # 무
                win_rate = columns[6].get_text(strip=True)  # 승률

                # 추출한 데이터 출력
                print(f"순위: {rank}, 팀: {team}, 경기 수: {games}, 승: {wins}, 패: {losses}, 무: {draws}, 승률: {win_rate}")
    else:
        print('순위 테이블을 찾을 수 없습니다.')
else:
    print(f'웹 페이지 요청 실패: {response.status_code}')
import requests
from bs4 import BeautifulSoup

def fetch_kbo_rankings():
    try:
        # KBO 웹사이트의 팀 순위 페이지 URL
        url = 'https://www.koreabaseball.com/TeamRank/TeamRank.aspx'
        
        # 웹 페이지에 HTTP 요청 보내기
        response = requests.get(url)
        response.raise_for_status()  # HTTP 요청이 성공적으로 완료되지 않으면 예외 발생
        
        # HTML 콘텐츠 파싱
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 팀 순위 테이블 찾기
        table = soup.find('table', {'class': 'tData'})
        
        # 테이블의 각 행을 탐색하여 데이터 추출
        if table:
            rankings = []
            for row in table.find_all('tr')[1:]:  # 첫 번째 행은 헤더이므로 제외
                columns = row.find_all('td')
                if columns:
                    rank = columns[0].get_text(strip=True)  # 순위
                    team = columns[1].get_text(strip=True)  # 팀 이름
                    games = columns[2].get_text(strip=True)  # 경기 수
                    wins = columns[3].get_text(strip=True)  # 승
                    losses = columns[4].get_text(strip=True)  # 패
                    draws = columns[5].get_text(strip=True)  # 무
                    win_rate = columns[6].get_text(strip=True)  # 승률
                    
                    # 추출한 데이터를 딕셔너리로 저장
                    rankings.append({
                        '순위': rank,
                        '팀': team,
                        '경기 수': games,
                        '승': wins,
                        '패': losses,
                        '무': draws,
                        '승률': win_rate
                    })
            return rankings
        else:
            print('순위 테이블을 찾을 수 없습니다.')
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# 수집한 데이터 출력
rankings = fetch_kbo_rankings()
if rankings:
    for team in rankings:
        print(f"{team['순위']}위: {team['팀']} - 경기 수: {team['경기 수']}, 승: {team['승']}, 패: {team['패']}, 무: {team['무']}, 승률: {team['승률']}")
requests.exceptions.HTTPError와 requests.exceptions.RequestException
import requests
from bs4 import BeautifulSoup

def fetch_kbo_rankings():
    try:
        # KBO 웹사이트의 팀 순위 페이지 URL
        url = 'https://www.koreabaseball.com/TeamRank/TeamRank.aspx'
        
        # 웹 페이지에 HTTP 요청 보내기
        response = requests.get(url)
        response.raise_for_status()  # HTTP 요청이 성공적으로 완료되지 않으면 예외 발생
        
        # HTML 콘텐츠 파싱
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 팀 순위 테이블 찾기
        table = soup.find('table', {'class': 'tData'})
        
        # 테이블의 각 행을 탐색하여 데이터 추출
        if table:
            rankings = []
            rows = table.find_all('tr')
            if not rows:
                raise ValueError("테이블에 데이터가 없습니다.")
            
            for row in rows[1:]:  # 첫 번째 행은 헤더이므로 제외
                columns = row.find_all('td')
                if len(columns) < 7:
                    raise ValueError("테이블 구조가 예상과 다릅니다.")
                
                rank = columns[0].get_text(strip=True)  # 순위
                team = columns[1].get_text(strip=True)  # 팀 이름
                games = columns[2].get_text(strip=True)  # 경기 수
                wins = columns[3].get_text(strip=True)  # 승
                losses = columns[4].get_text(strip=True)  # 패
                draws = columns[5].get_text(strip=True)  # 무
                win_rate = columns[6].get_text(strip=True)  # 승률
                
                # 추출한 데이터를 딕셔너리로 저장
                rankings.append({
                    '순위': rank,
                    '팀': team,
                    '경기 수': games,
                    '승': wins,
                    '패': losses,
                    '무': draws,
                    '승률': win_rate
                })
            return rankings
        else:
            print('순위 테이블을 찾을 수 없습니다.')
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# 수집한 데이터 출력
rankings = fetch_kbo_rankings()
if rankings:
    for team in rankings:
        print(f"{team['순위']}위: {team['팀']} - 경기 수: {team['경기 수']}, 승: {team['승']}, 패: {team['패']}, 무: {team['무']}, 승률: {team['승률']}")
import requests
from bs4 import BeautifulSoup

def fetch_kbo_rankings():
    try:
        # KBO 웹사이트의 팀 순위 페이지 URL
        url = 'https://www.koreabaseball.com/TeamRank/TeamRank.aspx'
        
        # 웹 페이지에 HTTP 요청 보내기
        response = requests.get(url)
        response.raise_for_status()  # HTTP 요청이 성공적으로 완료되지 않으면 예외 발생
        
        # HTML 콘텐츠 파싱
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 팀 순위 테이블 찾기
        table = soup.find('table', {'class': 'tData'})
        
        # 테이블의 각 행을 탐색하여 데이터 추출
        if table:
            rankings = []
            rows = table.find_all('tr')
            if not rows:
                raise ValueError("테이블에 데이터가 없습니다.")
            
            for row in rows[1:]:  # 첫 번째 행은 헤더이므로 제외
                columns = row.find_all('td')
                if len(columns) < 7:
                    raise ValueError("테이블 구조가 예상과 다릅니다.")
                
                rank = columns[0].get_text(strip=True)  # 순위
                team = columns[1].get_text(strip=True)  # 팀 이름
                games = columns[2].get_text(strip=True)  # 경기 수
                wins = columns[3].get_text(strip=True)  # 승
                losses = columns[4].get_text(strip=True)  # 패
                draws = columns[5].get_text(strip=True)  # 무
                win_rate = columns[6].get_text(strip=True)  # 승률
                
                # 추출한 데이터를 딕셔너리로 저장
                rankings.append({
                    '순위': rank,
                    '팀': team,
                    '경기 수': games,
                    '승': wins,
                    '패': losses,
                    '무': draws,
                    '승률': win_rate
                })
            return rankings
        else:
            print('순위 테이블을 찾을 수 없습니다.')
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# 수집한 데이터 출력
rankings = fetch_kbo_rankings()
if rankings:
    for team in rankings:
        print(f"{team['순위']}위: {team['팀']} - 경기 수: {team['경기 수']}, 승: {team['승']}, 패: {team['패']}, 무: {team['무']}, 승률: {team['승률']}")
import requests
from bs4 import BeautifulSoup

def fetch_kbo_rankings():
    try:
        # KBO 웹사이트의 팀 순위 페이지 URL
        url = 'https://www.koreabaseball.com/TeamRank/TeamRank.aspx'
        
        # 웹 페이지에 HTTP 요청 보내기
        response = requests.get(url)
        response.raise_for_status()  # HTTP 요청이 성공적으로 완료되지 않으면 예외 발생
        
        # HTML 콘텐츠 파싱
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 팀 순위 테이블 찾기
        table = soup.find('table', {'class': 'tData'})
        
        # 테이블의 각 행을 탐색하여 데이터 추출
        if table:
            rankings = []
            rows = table.find_all('tr')
            if not rows:
                raise ValueError("테이블에 데이터가 없습니다.")
            
            for row in rows[1:]:  # 첫 번째 행은 헤더이므로 제외
                columns = row.find_all('td')
                if len(columns) < 7:
                    raise ValueError("테이블 구조가 예상과 다릅니다.")
                
                rank = columns[0].get_text(strip=True)  # 순위
                team = columns[1].get_text(strip=True)  # 팀 이름
                games = columns[2].get_text(strip=True)  # 경기 수
                wins = columns[3].get_text(strip=True)  # 승
                losses = columns[4].get_text(strip=True)  # 패
                draws = columns[5].get_text(strip=True)  # 무
                win_rate = columns[6].get_text(strip=True)  # 승률
                
                # 추출한 데이터를 딕셔너리로 저장
                rankings.append({
                    '순위': rank,
                    '팀': team,
                    '경기 수': games,
                    '승': wins,
                    '패': losses,
                    '무': draws,
                    '승률': win_rate
                })
            return rankings
        else:
            print('순위 테이블을 찾을 수 없습니다.')
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# 수집한 데이터 출력
rankings = fetch_kbo_rankings()
if rankings:
    for team in rankings:
        print(f"{team['순위']}위: {team['팀']} - 경기 수: {team['경기 수']}, 승: {team['승']}, 패: {team['패']}, 무: {team['무']}, 승률: {team['승률']}")
        import requests
from bs4 import BeautifulSoup

def fetch_kbo_rankings():
    try:
        # KBO 웹사이트의 팀 순위 페이지 URL
        url = 'https://www.koreabaseball.com/TeamRank/TeamRank.aspx'
        
        # 웹 페이지에 HTTP 요청 보내기
        response = requests.get(url)
        response.raise_for_status()  # HTTP 요청이 성공적으로 완료되지 않으면 예외 발생
        
        # HTML 콘텐츠 파싱
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 팀 순위 테이블 찾기
        table = soup.find('table', {'class': 'tData'})
        
        # 테이블의 각 행을 탐색하여 데이터 추출
        if table:
            rankings = []
            rows = table.find_all('tr')
            if not rows:
                raise ValueError("테이블에 데이터가 없습니다.")
            
            for row in rows[1:]:  # 첫 번째 행은 헤더이므로 제외
                columns = row.find_all('td')
                if len(columns) < 7:
                    raise ValueError("테이블 구조가 예상과 다릅니다.")
                
                rank = columns[0].get_text(strip=True)  # 순위
                team = columns[1].get_text(strip=True)  # 팀 이름
                games = columns[2].get_text(strip=True)  # 경기 수
                wins = columns[3].get_text(strip=True)  # 승
                losses = columns[4].get_text(strip=True)  # 패
                draws = columns[5].get_text(strip=True)  # 무
                win_rate = columns[6].get_text(strip=True)  # 승률
                
                # 추출한 데이터를 딕셔너리로 저장
                rankings.append({
                    '순위': rank,
                    '팀': team,
                    '경기 수': games,
                    '승': wins,
                    '패': losses,
                    '무': draws,
                    '승률': win_rate
                })
            return rankings
        else:
            print('순위 테이블을 찾을 수 없습니다.')
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# 수집한 데이터 출력
rankings = fetch_kbo_rankings()
if rankings:
    for team in rankings:
        print(f"{team['순위']}위: {team['팀']} - 경기 수: {team['경기 수']}, 승: {team['승']}, 패: {team['패']}, 무: {team['무']}, 승률: {team['승률']}")
import requests
from bs4 import BeautifulSoup

def fetch_kbo_rankings():
    try:
        # KBO 웹사이트의 팀 순위 페이지 URL
        url = 'https://www.koreabaseball.com/TeamRank/TeamRank.aspx'
        
        # 웹 페이지에 HTTP 요청 보내기
        response = requests.get(url)
        response.raise_for_status()  # HTTP 요청이 성공적으로 완료되지 않으면 예외 발생
        
        # HTML 콘텐츠 파싱
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 팀 순위 테이블 찾기
        table = soup.find('table', {'class': 'tData'})
        
        # 테이블의 각 행을 탐색하여 데이터 추출
        if table:
            rankings = []
            rows = table.find_all('tr')
            if not rows:
                raise ValueError("테이블에 데이터가 없습니다.")
            
            for row in rows[1:]:  # 첫 번째 행은 헤더이므로 제외
                columns = row.find_all('td')
                if len(columns) < 7:
                    raise ValueError("테이블 구조가 예상과 다릅니다.")
                
                rank = columns[0].get_text(strip=True)  # 순위
                team = columns[1].get_text(strip=True)  # 팀 이름
                games = columns[2].get_text(strip=True)  # 경기 수
                wins = columns[3].get_text(strip=True)  # 승
                losses = columns[4].get_text(strip=True)  # 패
                draws = columns[5].get_text(strip=True)  # 무
                win_rate = columns[6].get_text(strip=True)  # 승률
                
                # 추출한 데이터를 딕셔너리로 저장
                rankings.append({
                    '순위': rank,
                    '팀': team,
                    '경기 수': games,
                    '승': wins,
                    '패': losses,
                    '무': draws,
                    '승률': win_rate
                })
            return rankings
        else:
            print('순위 테이블을 찾을 수 없습니다.')
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# 수집한 데이터 출력
rankings = fetch_kbo_rankings()
if rankings:
    for team in rankings:
        print(f"{team['순위']}위: {team['팀']} - 경기 수: {team['경기 수']}, 승: {team['승']}, 패: {team['패']}, 무: {team['무']}, 승률: {team['승률']}")
import requests
from bs4 import BeautifulSoup

def fetch_kbo_rankings():
    try:
        # KBO 웹사이트의 팀 순위 페이지 URL
        url = 'https://www.koreabaseball.com/TeamRank/TeamRank.aspx'
        
        # 웹 페이지에 HTTP 요청 보내기
        response = requests.get(url)
        response.raise_for_status()  # HTTP 요청이 성공적으로 완료되지 않으면 예외 발생
        
        # HTML 콘텐츠 파싱
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 팀 순위 테이블 찾기
        table = soup.find('table', {'class': 'tData'})
        
        # 테이블의 각 행을 탐색하여 데이터 추출
        if table:
            rankings = []
            rows = table.find_all('tr')
            if not rows:
                raise ValueError("테이블에 데이터가 없습니다.")
            
            for row in rows[1:]:  # 첫 번째 행은 헤더이므로 제외
                columns = row.find_all('td')
                if len(columns) < 7:
                    raise ValueError("테이블 구조가 예상과 다릅니다.")
                
                rank = columns[0].get_text(strip=True)  # 순위
                team = columns[1].get_text(strip=True)  # 팀 이름
                games = columns[2].get_text(strip=True)  # 경기 수
                wins = columns[3].get_text(strip=True)  # 승
                losses = columns[4].get_text(strip=True)  # 패
                draws = columns[5].get_text(strip=True)  # 무
                win_rate = columns[6].get_text(strip=True)  # 승률
                
                # 추출한 데이터를 딕셔너리로 저장
                rankings.append({
                    '순위': rank,
                    '팀': team,
                    '경기 수': games,
                    '승': wins,
                    '패': losses,
                    '무': draws,
                    '승률': win_rate
                })
            return rankings
        else:
            print('순위 테이블을 찾을 수 없습니다.')
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# 수집한 데이터 출력
rankings = fetch_kbo_rankings()
if rankings:
    for team in rankings:
        print(f"{team['순위']}위: {team['팀']} - 경기 수: {team['경기 수']}, 승: {team['승']}, 패: {team['패']}, 무: {team['무']}, 승률: {team['승률']}")