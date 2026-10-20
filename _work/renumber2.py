#!/usr/bin/env python3
"""把章节页标题序号从 1.1/1.1.1 改成纯数字：
   h2 -> N 标题（页内 1..N）
   h3 -> M 标题（在每个 h2 下重新从 1 开始）
   跳过代码块。"""
import re, io

FILES = {
    '/Users/fuheng/WorkBuddy/2026-10-18-23-21-04/fuulea-wiki/docs/teacher/task-publish.md': None,
    '/Users/fuheng/WorkBuddy/2026-10-18-23-21-04/fuulea-wiki/docs/teacher/teaching-scenes.md': None,
    '/Users/fuheng/WorkBuddy/2026-10-18-23-21-04/fuulea-wiki/docs/teacher/advanced.md': None,
}

HEAD = re.compile(r'^(#{2,3})\s+(.+?)\s*$')
# 去掉已有序号前缀，如 "1.4 " / "1.4.1 "
OLD_NUM = re.compile(r'^\d+(?:\.\d+)+\s+')


def strip_num(title):
    return OLD_NUM.sub('', title).strip()


def renumber(path):
    lines = io.open(path, encoding='utf-8').read().split('\n')
    out, in_fence = [], False
    sec = sub = 0
    changed = []
    for ln in lines:
        if ln.lstrip().startswith('```'):
            in_fence = not in_fence
            out.append(ln)
            continue
        if not in_fence:
            m = HEAD.match(ln)
            if m:
                depth, title = m.group(1), strip_num(m.group(2))
                if len(depth) == 2:
                    sec += 1
                    sub = 0
                    new = '%s %d %s' % (depth, sec, title)
                else:
                    sub += 1
                    new = '%s %d %s' % (depth, sub, title)
                changed.append((ln.strip(), new.strip()))
                out.append(new)
                continue
        out.append(ln)
    io.open(path, 'w', encoding='utf-8').write('\n'.join(out))
    print('==', path.split('/')[-1])
    for a, b in changed:
        print('   ', a, '->', b)
    return len(changed)


total = 0
for p in FILES:
    total += renumber(p)
print('total:', total)
