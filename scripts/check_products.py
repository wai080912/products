"""产品网站体检：图片缺失、产品数对不上、重复编号。有问题就列出来，没问题打印 OK。"""
import json, os, re
page = open("index.html", encoding="utf-8").read()
cards = re.findall(r'<article class="card"([^>]*)>', page)
products = json.load(open("products.json", encoding="utf-8"))
problems = []
if len(cards) != len(products):
    problems.append(f"网页有 {len(cards)} 个产品，products.json 有 {len(products)} 个（同步没跟上）")
codes = [p["code"] for p in products]
dup = sorted({c for c in codes if codes.count(c) > 1})
if dup:
    problems.append("编号重复：" + ", ".join(dup))
for p in products:
    for key in ("img", "back"):
        path = p.get(key, "").split("?")[0]
        if path and not os.path.exists(path):
            problems.append(f"{p['code']} {p['name']}：{'背面' if key == 'back' else ''}图片不见了")
used = {p.get(k, "").split("?")[0] for p in products for k in ("img", "back")}
unused = [f for f in sorted(os.listdir("images")) if "images/" + f not in used]
print("\n".join(problems) if problems else f"OK {len(products)} 个产品，图片齐全")
if unused:
    print(f"（另有 {len(unused)} 张图没用到：{', '.join(unused[:5])}{' …' if len(unused) > 5 else ''}）")
