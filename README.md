# products
Seafood product catalog — https://wai080912.github.io/products/

## 只有一份产品清单：products.json
- 网页 `index.html` 打开时读 `products.json`，自己画出卡片和分类按钮。
  **加货、改名、换图：只改 `products.json`，图片放进 `images/`**，`index.html` 不用动。
- 生产 app 读的也是这一份，所以网页和 app 永远一样。
- 料号重复的，网页只显示第一笔；没有 `code` 或 `img` 的不显示。
- 换了图片，要把 `img` / `back` 后面的 `?v=N` 加一，不然手机会一直显示旧图。

## products.json 每一项
`code` 料号、`name` 名称、`category` 分类（分类按钮照这个自动出）、`packing` 包装、
`img` 正面图、`back` 背面图（可能没有）、`keywords` 额外的搜索字（可能没有）。

不要放价格、供应商、客户资料（这个网页是公开的）。

2026-10-13 起是这个做法。以前是从 `index.html` 自动重建 `products.json`，那条自动同步已经关掉。
