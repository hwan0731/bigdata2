import random
import time

songs = ["a노래", "b노래", "c노래", "d노래"]
print(songs)
print(songs[0])
print(songs[1])
print(songs[2])
print(songs[3])

for song in songs: 
    print(song)

print("AI야 노래 한곡만 추천해줘")
print("""
알겠습니다.
제가 열심히 분석해서 
고객님께 노래를 한곡 
추천합니다
      """)
#여기서 AI가 돌아야죠 
ai_song = random.choice(songs)
dd = ["두", "두", "두", "두둥"]
for d in dd:
    print(d)
    time.sleep(1)

print(f"두두두두두두두둥 제가 추천한곡은 {ai_song}입니다.")

# 리스트를 쓰는 이유 
song1 = "a노래"
song2 = "b노래"
song3 = "c노래"

print(song1)
print(song2)
print(song3)

import time

# Simulated list of 100 song titles from the Melon chart
melon_chart_top_100 = [
    "Song 1", "Song 2", "Song 3", "Song 4", "Song 5", 
    "Song 6", "Song 7", "Song 8", "Song 9", "Song 10",
    # ... continue this list up to 100 songs
    "Song 91", "Song 92", "Song 93", "Song 94", "Song 95",
    "Song 96", "Song 97", "Song 98", "Song 99", "예뻤어"
]

print("AI에게 노래 한 곡을 추천받아보세요!") 
print("""
알겠습니다. 
제가 열심히 분석해서 
고객님께 노래를 한 곡 
추천합니다
      """)

# Simulate a suspenseful pause
dd = ["두", "두", "두", "두둥"]
for d in dd:
    print(d)
    time.sleep(1)

# Directly recommend the song "예뻤어"
recommended_song = "예뻤어"
print(f"제가 추천하는 곡은 '{recommended_song}'입니다!")


