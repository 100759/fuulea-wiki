#!/usr/bin/env python3
"""章节页标题编号最终版（右侧目录口径）：
   一级标题（##）-> 1、2、3…（页内递增）
   二级标题（###）-> <父序号>.<n>，如 4.1、4.2（在每个 ## 下重新从 1 开始）
   跳过代码块。"""
import re, io

FILES = [
    '/Users/fuheng/WorkBuddy/2026-10-18-23-21-04/fuulea-wiki/docs/teacher/task-publish.md',
    '/Users/fuheng/WorkBuddy/2026-10-18-23-21-04/fuulea-wiki/docs/teacher/teaching-scenes.md',
    '/Users/fuheng/WorkBuddy/2026-10-18-23-21-04/fuulea-wiki/docs/teacher/advanced.md',
]

HEAD = re.compile(r'^(#{2,3})\s+(.+?)\s*$')
# 去掉已有序号前缀：支持 "4 " / "4.1 " / "1.4.1 "
OLD_NUM = re.compile(r'^\d+(?:\.\d+)*\s+')


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
                depth, title = m.group(1), OLD_NUM.sub('', m.group(2)).strip()
                if len(depth) == 2:
                    sec += 1
                    sub = 0
                    new = '%s %d %s' % (depth, sec, title)
                else:
                    sub += 1
                    new = '%s %d.%d %s' % (depth, sec, sub, title)
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
