#!/usr/bin/env python3
"""全站链接 + 锚点校验：既查跨页 `/path#anchor`，也查同页 `#anchor`。"""
import re, glob, sys, urllib.parse, os

DIST = '/Users/fuheng/WorkBuddy/2026-10-18-23-21-04/fuulea-wiki/docs/.vitepress/dist'
os.chdir(DIST)

# 1. 收集每个页面的 id 集合
pages = {}   # url path -> set(ids)
filemap = {} # url path -> html 文件相对路径
for f in glob.glob('**/*.html', recursive=True):
    html = open(f, encoding='utf-8').read()
    key = '/' if f == 'index.html' else '/' + f[:-5]
    if key == '/teacher/index':
        key = '/teacher/'
    pages[key] = set(re.findall(r'id="([^"]+)"', html))
    filemap[key] = f

bad = []
for path in sorted(pages):
    html = open(filemap[path], encoding='utf-8').read()
    # 跨页：href="/path#anchor" ；同页：href="#anchor"
    for target, anchor in re.findall(r'href="(/[^"#]*)?(#[^"]+)"', html):
        anchor = anchor[1:]
        target = target if target else path
        if target in pages:
            real = urllib.parse.unquote(anchor)
            if real not in pages[target]:
                bad.append((path, target + '#' + real))
        else:
            # 目标页不存在（assets/images 等静态资源除外）
            if not re.match(r'^/(assets|images|favicon|vp-icons|hashmap|sitemap)', target):
                bad.append((path, target + ' (页面不存在)'))

print('检查页面数:', len(pages))
if bad:
    print('发现问题 %d 处:' % len(bad))
    for src, tgt in sorted(set(bad)):
        print('   [%s] -> %s' % (src, tgt))
    sys.exit(1)
print('OK：所有页内/跨页锚点均有效')
