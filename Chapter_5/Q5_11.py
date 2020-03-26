import re
import urllib.request

# wikiページ内容をダウンロードする
right_part = urllib.parse.quote("第二次世界大戦")  # 文字化けを避ける
url = "https://ja.wikipedia.org/wiki/" + right_part
html = urllib.request.urlopen(url).read()
html = html.decode('utf-8')  # decodeしないと日本語を読めない

year_pattern = r"("""①""""""②""")"""③"""{"""④"""}年"
matches = re.findall(year_pattern, html)

year_counts = dict((year, matches."""⑤"""(year)) for year in """⑥"""(matches))

for year in sorted("""⑦""", key="""⑦""".get, reverse=True):
    print(year, year_counts[year])
