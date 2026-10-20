#!/usr/bin/env python3
"""按构建产物里的真实锚点 id，自动修正 Markdown 里的锚点链接。
匹配方式：用链接的显示文本去目标页找同名标题，取其 id。"""
import re, io, os, glob

DIST = '/Users/fuheng/WorkBuddy/2026-10-18-23-21-04/fuulea-wiki/docs/.vitepress/dist'
DOCS = '/Users/fuheng/WorkBuddy/2026-10-18-23-21-04/fuulea-wiki/docs'
NUM = re.compile(r'^\d+(?:\.\d+)*\s+')

# 1. 目标页 -> {标题纯文本: id}
page_ids = {}
for f in sorted(glob.glob(os.path.join(DIST, '**', '*.html'), recursive=True)):
    rel = os.path.relpath(f, DIST)
    if rel.startswith('node_modules') or '/node_modules/' in rel:
        continue
    html = io.open(f, encoding='utf-8').read()
    url = '/' if rel == 'index.html' else '/' + rel[:-5]
    if url == '/teacher/index':
        url = '/teacher/'
    m = {}
    for hid, text in re.findall(r'<h[23] id="([^"]+)"[^>]*>(.*?)<a class="header-anchor"', html, re.S):
        clean = re.sub(r'<[^>]+>', '', text).strip()
        clean = NUM.sub('', clean).strip()
        if clean:
            m.setdefault(clean, hid)
    page_ids[url] = m
print('已索引页面:', sorted(page_ids))

# 2. 扫 Markdown 里的 [文本](路径#锚点) 与 [文本](#锚点)
LINK = re.compile(r'\[([^\]]+)\]\((/[^)#]*)?(#[^)]+)\)')
fixed, missed = [], []

for root, _, files in os.walk(DOCS):
    if 'public' in root or '.vitepress' in root:
        continue
    for fn in files:
        if not fn.endswith('.md'):
            continue
        path = os.path.join(root, fn)
        src = io.open(path, encoding='utf-8').read()
        out, n = src, 0

        def repl(mo):
            global n
            text, target, frag = mo.group(1), mo.group(2) or '', mo.group(3)
            if target:
                key = target if target != '/teacher/index' else '/teacher/'
                key = key.rstrip('/') if key != '/' else key
                key = key + '/' if key in ('/teacher',) else key
                # 归一化：/teacher -> /teacher/
                if key == '/teacher':
                    key = '/teacher/'
                elif key.endswith('.html'):
                    key = key[:-5]
            else:
                # 同页锚点：按当前文件推 url
                rel = os.path.relpath(path, DOCS)[:-3]
                key = '/' if rel == 'index' else '/' + rel
                if key == '/teacher/index':
                    key = '/teacher/'
            ids = page_ids.get(key)
            if not ids:
                missed.append((path, text, key))
                return mo.group(0)
            want = NUM.sub('', text).strip()
            new_id = ids.get(want)
            if not new_id:
                # 显示文本可能带额外说明，做一次包含匹配
                cand = [v for k, v in ids.items() if want in k or k in want]
                if len(cand) == 1:
                    new_id = cand[0]
            if not new_id:
                missed.append((path, text, key))
                return mo.group(0)
            new = '[%s](%s#%s)' % (text, target, new_id)
            if new != mo.group(0):
                fixed.append((os.path.relpath(path, DOCS), mo.group(0), new))
            return new

        out = LINK.sub(repl, src)
        if out != src:
            io.open(path, 'w', encoding='utf-8').write(out)

print('修正 %d 处:' % len(fixed))
for f, a, b in fixed:
    print('  [%s]\n     %s\n  -> %s' % (f, a, b))
if missed:
    print('未能匹配 %d 处（需人工确认）:' % len(missed))
    for m in missed:
        print('  ', m)
else:
    print('全部匹配成功')
