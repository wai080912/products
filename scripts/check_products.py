"""产品网站体检：网页有没有在读 products.json、图片缺失、重复编号。有问题就列出来，没问题打印 OK。"""
import json, os
page = open("index.html", encoding="utf-8").read()
products = json.load(open("products.json", encoding="utf-8"))
problems = []
# 网页从 products.json 画卡片（2026-10-13 起）。13/10 18:47 传上来一份旧的 index.html，
# 卡片又写死在页面里：线上少了 4 个货、LF-SMX0002C 多一张坏卡，到 15/10 才发现。这一条抓的就是这个。
if "products.json" not in page or '<article class="card"' in page:
    problems.append("index.html 没在读 products.json（可能被旧版盖掉了），products.json 新加的货不会出现")
codes = [p["code"] for p in products]
dup = sorted({c for c in codes if codes.count(c) > 1})
if dup:
    problems.append("编号重复：" + ", ".join(dup))
for p in products:
    for key, label in (("img", ""), ("back", "背面"), ("third", "第三张")):
        path = p.get(key, "").split("?")[0]
        if path and not os.path.exists(path):
            problems.append(f"{p['code']} {p['name']}：{label}图片不见了")
used = {p.get(k, "").split("?")[0] for p in products for k in ("img", "back", "third")}
unused = [f for f in sorted(os.listdir("images")) if "images/" + f not in used and f not in page]
print("\n".join(problems) if problems else f"OK {len(products)} 个产品，图片齐全")
if unused:
    print(f"（另有 {len(unused)} 张图没用到：{', '.join(unused[:5])}{' …' if len(unused) > 5 else ''}）")
