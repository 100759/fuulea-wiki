#!/usr/bin/env python3
"""给三个章节页的 h2/h3 标题加序号（h2 -> N.x，h3 -> N.x.y），跳过代码块。"""
import re, sys, io

FILES = {
    '/Users/fuheng/WorkBuddy/2026-10-18-23-21-04/fuulea-wiki/docs/teacher/task-publish.md': 1,
    '/Users/fuheng/WorkBuddy/2026-10-18-23-21-04/fuulea-wiki/docs/teacher/teaching-scenes.md': 2,
    '/Users/fuheng/WorkBuddy/2026-10-18-23-21-04/fuulea-wiki/docs/teacher/advanced.md': 3,
}

HEAD = re.compile(r'^(#{2,3})\s+(.+?)\s*$')

def renumber(path, chapter):
    lines = io.open(path, encoding='utf-8').read().split('\n')
    out = []
    in_fence = False
    sec = 0
    sub = 0
    changed = []
    for ln in lines:
        if ln.lstrip().startswith('```'):
            in_fence = not in_fence
            out.append(ln)
            continue
        if not in_fence:
            m = HEAD.match(ln)
            if m:
                depth, title = m.group(1), m.group(2)
                if len(depth) == 2:
                    sec += 1
                    sub = 0
                    new = '%s %d.%d %s' % (depth, chapter, sec, title)
                else:
                    sub += 1
                    new = '%s %d.%d.%d %s' % (depth, chapter, sec, sub, title)
                changed.append((ln.strip(), new.strip()))
                out.append(new)
                continue
        out.append(ln)
    io.open(path, 'w', encoding='utf-8').write('\n'.join(out))
    print('==', path.split('/')[-1], 'chapter', chapter)
    for a, b in changed:
        print('   ', a, '->', b)
    return len(changed)

total = 0
for p, ch in FILES.items():
    total += renumber(p, ch)
print('total headings renumbered:', total)
