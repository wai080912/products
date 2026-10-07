"""从 index.html 的产品卡片生成 products.json（给其他 app 读取用）。"""
import html, json, re

page = open("index.html", encoding="utf-8").read()
try:
    old = {p["code"]: p for p in json.load(open("products.json", encoding="utf-8"))}
except FileNotFoundError:
    old = {}

products = []
for attrs in re.findall(r'<article class="card"([^>]*)>', page):
    d = {k: html.unescape(v) for k, v in re.findall(r'data-([a-z]+)="([^"]*)"', attrs)}
    p = {"code": d["code"], "name": d["name"], "category": d["cat"], "packing": d["spec"], "img": d["img"]}
    if d.get("back"):
        p["back"] = d["back"]
    if "keywords" in old.get(p["code"], {}):
        p["keywords"] = old[p["code"]]["keywords"]
    products.append(p)

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(len(products), "products")
