import re


def clean_titles(html_input):
    title_pattern = r'<p .*class=".*"""①""".*"[^>]*>"""②"""</p>'
    return re.sub(title_pattern, "<h1>"""③"""</h1>", html_input)


# 関数のテスト
old_html = '<p class="title title-section">My beautiful HTML code</p>'
new_html = clean_titles(old_html)
print(f"Old HTML: {old_html}")
print(f"New HTML: {new_html}")