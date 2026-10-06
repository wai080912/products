# products
Seafood product catalog — https://wai080912.github.io/products/

## 分工
- **Muse**：`images/` 里的照片 + `products.json` 里的产品资料
- **Claude**：`index.html`（网页的样子和功能）

## 加一个产品（只改 products.json，不用碰 index.html）
1. 照片放进 `images/`，用料号命名，例如 `images/SMX0071020.webp`（背面：`SMX0071020-back.webp`）
2. 在 `products.json` 里加一项：

```json
{
  "code": "SMX0071020",
  "name": "NZ King Salmon Square Cut Portion",
  "category": "Salmon",
  "packing": "60ea x 150 g",
  "img": "images/SMX0071020.webp",
  "back": "images/SMX0071020-back.webp"
}
```

- `back`、`keywords`（额外搜索词）可以不写
- `img` 不写的话，默认用 `images/料号.webp`
- 换了照片想让大家马上看到新图：在路径后面加 `?v=2`（每换一次加 1）
- 分类按钮会按 `category` 自动生成
- 不要放价格、供应商、客户资料（这个网页是公开的）
