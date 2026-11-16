# Nymphéas Studio Lookbook

完整靜態網站備份，包含頁面、圖片、字體、影片及目前的排版設定。無須安裝套件或執行 build。

## 專案結構

```text
dist/
  index.html             封面與信封
  introduction.html      翻頁 Lookbook
  assets/                所有網站使用的圖片、字體、影片及翻頁程式
  page-editor.js         排版調整功能
.github/workflows/       手動發布至 GitHub Pages
.openai/hosting.json     原 Sites 專案的部署設定（保留作備份）
NYMPHEAS_COLOURS.md      品牌色彩筆記
ASSET_MANIFEST.sha256    媒體與頁面檔案校驗碼
```

未使用的素材也保留在 `dist/assets/`，以便日後修改設計。`dist/assets/page-flip.LICENSE.txt` 是翻頁程式的授權聲明。請自行確認其他媒體及字體的對外使用權限。

## 在本機預覽

先把完整 ZIP 解壓到一個全新資料夾。在 WSL / VS Code Terminal 的專案根目錄執行 `python3 start-preview.py`，它會先檢查所有網站檔案，完整才啟動預覽。然後開啟 `http://localhost:8000/`。不要將這份完整包和舊的分包混合，也不要只複製 HTML；所有 `dist/assets/`、CSS 和 JavaScript 都必須一起保留。

這份完整包已包括本機 Cormorant Garamond、Montserrat 和 Whimsy 字體；前兩者的 OFL 授權亦附於 assets。開場牛油紙、信封、抽信紙、翻頁程式、頁面動畫、圖片放大及影片均包含在 dist，無需 Google Fonts 網路連線。

排版工具平時隱藏；需要調整時開啟 `http://localhost:8000/introduction.html?edit=1`。工具儲存的修改只在當前瀏覽器的 localStorage；按「複製排版資料」取得 JSON，再把確定的數值寫入原始檔後重新部署。

## 備份到自己的 GitHub

1. 在 GitHub 建立一個新的空白 repository，建議先選 **Private**，不要勾選自動建立 README。
2. 解壓單一完整 ZIP 到全新資料夾；進入包含本 README、`start-preview.py` 與 `dist/` 的資料夾。
3. 在該資料夾執行（將尖括號部分換成你的資料）：

```bash
git init -b main
git add .
git commit -m "Back up Nympheas Studio lookbook"
git remote add origin https://github.com/<YOUR-USERNAME>/<REPOSITORY>.git
git push -u origin main
```

請上傳解壓後的檔案及資料夾，**不要只把 ZIP 本身當成網站原始碼上傳**。GitHub repository 是原始碼備份，僅建立 repository 不會公開網站。可在專案根目錄執行 `sha256sum -c ASSET_MANIFEST.sha256`，確認所有網站檔案完整。

## 準備好後發布 GitHub Pages

到 repository 的 **Settings → Pages → Build and deployment → Source** 選 **GitHub Actions**。然後到 **Actions → Deploy Lookbook to GitHub Pages → Run workflow** 手動發布。工作流程使用 `dist/` 作為網站根目錄，沒有自動 push 發布觸發器。發布網址會顯示在該次 workflow 的結果中，通常是 `https://<YOUR-USERNAME>.github.io/<REPOSITORY>/`。

GitHub Pages 的公開網站可以讓持有網址的人觀看，即使 repository 是 private 也要把網站內容視為公開。GitHub Free 的 Pages 通常要求 public repository；實際可用性以你的帳戶方案與 GitHub 設定為準。

## 分享

- **分享備份／原始碼：** Public repository 可直接分享 GitHub 網址；Private repository 可在 **Settings → Collaborators** 邀請指定帳戶。
- **分享網站：** 完成 GitHub Pages 發布後分享 Pages 網址。目前原 Sites 網址的存取權限是只有擁有人；直接傳給別人未必能打開。可在 Sites 設定邀請訪客或將網站改為公開。

原 Sites 發布地址：`https://nympheas-studio-lookbook.largepretzel16.chatgpt.site/`。此備份不包含 Git 歷史或登入憑證；`.openai/hosting.json` 內是原 Sites 專案識別與靜態目錄設定。
