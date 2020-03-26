import re


class MarkdownParseError(Exception):
    pass


def parse_markdown_link(link):
    link_pattern = r'\[("""①"""<"""②""">"""③""")\]' \
                   r'\(("""①"""<"""④""">[^ ]+)' \
                   r'( """⑤"""("""①"""<title>"""③""")"""⑤""")?\)'
    m = re.match(link_pattern, link)
    if m is not None:
        return [m.group('text'), m.group('url'), m.group('title')]
    else:
        raise MarkdownParseError("Invalid markdown link.")


# 関数のテスト
markdown_link = '[表示されるテキスト。[リンク]の情報](http://www.myurl.com "私の"任意"タイトル")'
print(parse_markdown_link(markdown_link))
