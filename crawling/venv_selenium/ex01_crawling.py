import requests
res = requests.get("https://naver.com")
print("res: ", res.status_code)
res.raise_for_status()              # 문제가 발생하면 종료됨.

print(len(res.text))

# 파일로 저장
with open('crawledPage1.html', 'w', encoding='utf8') as f:
    f.write(res.text)