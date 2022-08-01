import json

data = """
{
    "lastBuildDate": "Mon, 01 Aug 2022 22:13:34 +0900",
    "total": 9341,
    "start": 1,
    "display": 10,
    "items": [
        {
            "title": "누리꾼들이 한 목소리로 말하는 &apos;이상한 변호사 <b>우영우</b>&apos;의 성공 요인",
            "originallink": "https://www.wikitree.co.kr/articles/772065",
            "link": "https://www.wikitree.co.kr/articles/772065",
            "description": "드라마 &apos;이상한 변호사 <b>우영우</b>(이하 &apos;<b>우영우</b>&apos;)&apos;가 화제 몰이 중이다. &apos;<b>우영우</b>&apos;의 인기 비결은 복합적이다. 그중 하나는 간결한 스토리 구성이다. 매회 <b>우영우</b> 변호사가 새로운 사건을 맡게 되고, 새로운 관점과 독특한... ",
            "pubDate": "Mon, 01 Aug 2022 21:56:00 +0900"
        },
        {
            "title": "J리그 <b>우영우</b> 세레모니 화제 &quot;우 to the 영 to the 우&quot;",
            "originallink": "http://www.ggilbo.com/news/articleView.html?idxno=926128",
            "link": "http://www.ggilbo.com/news/articleView.html?idxno=926128",
            "description": "J리그 <b>우영우</b> 세레모니 화제 &quot;우 to the 영 to the 우&quot; 사진=온라인 커뮤니티 J리그에 등장한 <b>우영우</b> 세레모니가 화제를 모으고 있다. 지난달 31일 일본 시즈오카시 시미즈구의 IAI 스타디움 니혼다이라에서는 시미즈... ",
            "pubDate": "Mon, 01 Aug 2022 21:56:00 +0900"
        },
        {
            "title": "&quot;만 5세 초교 등교, 사회적 합의기구서 결정해야&quot;",
            "originallink": "https://www.idaegu.co.kr/news/articleView.html?idxno=390289",
            "link": "https://www.idaegu.co.kr/news/articleView.html?idxno=390289",
            "description": "사교육자 등 이해 관계자들이 모두 모여 사회적 합의를 해나가는 지혜를 발휘해야 한다&quot;고 밝혔다. 그는 &quot;&apos;이상한 변호사 <b>우영우</b>&apos;가 말한 대로, 연령에만 &apos;초점을 맞추면 문제를 풀 수 없다. 핵심을 봐야 한다&apos;&quot;고 덧붙였다.",
            "pubDate": "Mon, 01 Aug 2022 21:44:00 +0900"
        },
        {
            "title": "드라마 &apos;이상한 변호사 <b>우영우</b>&apos;의 실제 모델, 이 사람입니다 (사진)",
            "originallink": "https://www.wikitree.co.kr/articles/775051",
            "link": "https://www.wikitree.co.kr/articles/775051",
            "description": "ENA 드라마 &apos;이상한 변호사 <b>우영우</b>&apos;의 주인공 <b>우영우</b>의 실제 모델로 알려진 동물학자 템플 그랜딘이 주목받고 있다.   세계적 동물학자 템플 그랜딘은 현재 미국 콜로라도 주립대에서 교수로 재직 중이다. 그는 자폐... ",
            "pubDate": "Mon, 01 Aug 2022 20:56:00 +0900"
        },
        {
            "title": "<b>우영우</b>♥이준호 데이트 장면, 드라마 방영 전 이미 공개했었다 (+영상)",
            "originallink": "https://www.wikitree.co.kr/articles/776892",
            "link": "https://www.wikitree.co.kr/articles/776892",
            "description": "&apos;이상한 변호사 <b>우영우</b>&apos; 방영 전 공개된 예고편에 <b>우영우</b>-이준호의 데이트가 일부 담겼다. 지난달 28일 방송된 ENA 수목드라마 &apos;이상한 변호사 <b>우영우</b>&apos;에서는 <b>우영우</b>(박은빈)와 이준호(강태오)가 본격적으로 사귀는 장면이... ",
            "pubDate": "Mon, 01 Aug 2022 20:32:00 +0900"
        },
        {
            "title": "KT, 9년여 만에 시총 10조원 탈환…&quot;5G 끌고 디지코 밀고“",
            "originallink": "http://www.g-enews.com/ko-kr/news/article/news_all/20220801202312822006941316ce_1/article.html",
            "link": "http://www.g-enews.com/ko-kr/news/article/news_all/20220801202312822006941316ce_1/article.html",
            "description": "최근에는 미디어콘텐츠 자회사 KT스튜디오지니가 투자한 &apos;이상한 변호사 <b>우영우</b>&apos;가 선전하면서 미디어·콘텐츠 사업에서도 두각을 나타내고 있다. 또 온라인동영상서비스(OTT) 시즌을 CJ ENM의 티빙에... ",
            "pubDate": "Mon, 01 Aug 2022 20:28:00 +0900"
        },
        {
            "title": "기적의 숨은 주역은 감정적인 태도",
            "originallink": "http://www.kihoilbo.co.kr/news/articleView.html?idxno=990492",
            "link": "http://www.kihoilbo.co.kr/news/articleView.html?idxno=990492",
            "description": "최근 인기를 끄는 드라마 &apos;이상한 변호사 <b>우영우</b>&apos;에서도 감정적인 태도가 놀라운 성과를 끌어낸 에피소드가 등장한다. 자폐를 가져 타인에게 쉽사리 공감하지 못하는 변호사 &apos;<b>우영우</b>&apos;는 동료 변호사 &apos;최수연&apos;과 함께... ",
            "pubDate": "Mon, 01 Aug 2022 20:26:00 +0900"
        },
        {
            "title": "[메아리]드라마처럼 일한다면?",
            "originallink": "http://sjbnews.com/news/news.php?number=752960",
            "link": "http://sjbnews.com/news/news.php?number=752960",
            "description": "‘<b>우영우</b>’도 그렇고 ‘비밀의 숲’에서도 그랬다. ‘슬의생’과 ‘낭만닥터’에 의사들은 며칠을 날을 새면서 환자를 돌보고 수술을 한다. 드라마에 경찰은 집에 들어가는 모습을 보지를 못했다. 매일 잠복하며 범인... ",
            "pubDate": "Mon, 01 Aug 2022 20:16:00 +0900"
        },
        {
            "title": "유튜브에서 사라진 &apos;<b>우영우</b>&apos;?…ENA, 정말 억울한 상황 처했다 (+해명)",
            "originallink": "https://www.wikitree.co.kr/articles/776880",
            "link": "https://www.wikitree.co.kr/articles/776880",
            "description": "ENA 수목드라마 &apos;이상한 변호사 <b>우영우</b>&apos;의 유튜브 클립 영상이 삭제됐다가 재업로드 됐다는 주장에 ENA 측이 입장을 밝혔다. 최근 온라인 커뮤니티에서는 ENA 유튜브 채널에 올라와 있던 &apos;<b>우영우</b>&apos;의 클립 영상이 모두... ",
            "pubDate": "Mon, 01 Aug 2022 20:06:00 +0900"
        },
        {
            "title": "KT, 9년여 만 시총 10조 회복…‘디지코’ 전략 통했다",
            "originallink": "http://www.segyebiz.com/newsView/20220801523697?OutUrl=naver",
            "link": "http://www.segyebiz.com/newsView/20220801523697?OutUrl=naver",
            "description": "최근에는 미디어콘텐츠 자회사 KT스튜디오지니가 투자한 &apos;이상한 변호사 <b>우영우</b>&apos;가 선전하면서 미디어·콘텐츠 사업에서도 두각을 나타내고 있다. 또 온라인동영상서비스(OTT) 시즌을 CJ ENM의 티빙에... ",
            "pubDate": "Mon, 01 Aug 2022 20:04:00 +0900"
        }
    ]
}
"""

data = json.loads(data)
print(data['lastBuildDate'])
print(data['items'][0])

for i, v in enumerate(data['items']):
  print(i, v['title'], v['link'])