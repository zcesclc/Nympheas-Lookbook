# Nymphéas Studio — 色彩規範

版本：2026-11-14 · v1

此文件是後續網站、lookbook 及生成素材的色彩依據。新增頁面時載入 `dist/palette.css`，不要每次重新選色。

## 核心色票

| 色彩 | HEX | CSS token | 用途 |
| --- | --- | --- | --- |
| 暖米白 · Warm Ivory | `#F3E7CE` | `--nym-ivory` | 信封、信紙、內頁紙面共同基底；帶柔和黃色，不偏冷灰或粉白 |
| 淺米白 · Light Ivory | `#FAF3E5` | `--nym-ivory-light` | 紙面亮部、小面積介面底色 |
| 復古紫 · Vintage Violet | `#705575` | `--nym-purple` | 主文字、加粗邊框、連結 |
| 淡紫 · Soft Violet | `#A58AA8` | `--nym-purple-soft` | 次要框線、分隔線 |
| 睡蓮粉 · Water-lily Pink | `#B78F9D` | `--nym-pink` | 小面積強調、標記 |
| 睡蓮翠綠 · Lily Green | `#527B70` | `--nym-green` | 少量植物色、章節提示；柔和藍綠調，不用螢光綠 |
| 水影藍 · Water Blue | `#777F9A` | `--nym-blue` | 極少量輔助色 |
| 深紫墨 · Plum Ink | `#514259` | `--nym-ink` | 小字或需要更高對比的文字 |

## 選色依據

基準背景：`dist/assets/water-lilies-purple.jpg`。

對圖片進行 10 色量化後，主要顏色包括 `#615D6E`、`#686776`、`#7C6C75`、`#525568`、`#85747C`、`#343845`、`#8E7B82`、`#3E4454`、`#484A5C`、`#9B888C`。

上表是以睡蓮畫面的色相、灰度與已有紫色文字為依據，經設計調整後的統一配色；不是宣稱每個 HEX 都直接取自單一像素。暖米白是封面紙材的共同目標色，粉色及翠綠則是與背景協調的輔助色。

## 使用規則

- 以暖米白為主、紫色作文字與邊框，粉色與翠綠作少量點綴，藍色最少。
- 不含睡蓮照片的平面，可從米白 70%、紫色 20%、粉色與翠綠合計 8%、藍色 2% 開始調整；這是構圖指引，不是強制像素比例。
- 同一頁優先只用一種點綴色。正文用復古紫或深紫墨；粉色、翠綠及淡紫不作米白底的小字正文。
- 不引入紅、橙、棕或金色作新的品牌色。材料中自然的柔和明暗可以保留。
- 信封與信紙都以 `#F3E7CE` 為紙材／布料底色目標；實際紋理像素會隨纖維、透明度、陰影及底圖變化，不要求每個像素相同。

## 材質與風格記錄

Tactile digital collage：真實紙張纖維、布料觸感，配合有電子圖形感的清晰邊框。信紙不用花卉、額外植物裝飾或過量花紋。紫色邊框稍粗、構圖留白。標題使用用戶的 Whimsy 字體。

首頁信紙比原先更橫向：寬度為信封容器的 88%，左右各留 6%。邀請文字為 “you're invited to Nymphéas Studio”。抽信動畫為 0.5 秒，之後進入簡介／目錄頁。後續 lookbook 內頁繼續提供拖動和縮放元素的排版功能。

## 生成素材時附加的配色要求

> Warm ivory #F3E7CE tactile paper or fabric, vintage violet #705575 graphic borders and typography, restrained water-lily pink #B78F9D and lily green #527B70 accents, minimal water blue #777F9A. Keep the palette muted and coherent. Real material texture with clean digital graphic borders. No flowers, no extra ornaments, no gold, no bright colors.
