# products
Seafood product catalog — https://wai080912.github.io/products/

## 分工
- **Muse**：照片（`images/`）和网页 `index.html`，照原来的做法直接改。
- **products.json**：给其他 app（生产 app 等）读取的产品清单，**不用手动改**。
  每次 `index.html` 有改动，GitHub 会自动从网页重新生成它（`.github/workflows/sync-products.yml`）。

## products.json 每一项
`code` 料号、`name` 名称、`category` 分类、`packing` 包装、`img` 正面图、`back` 背面图（可能没有）。

不要放价格、供应商、客户资料（这个网页是公开的）。
