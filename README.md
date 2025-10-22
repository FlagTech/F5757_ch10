# TaskMaster - 個人任務管理系統

一個簡單且模組化的任務管理應用程式，提供桌面介面和 Web API，讓你輕鬆管理日常任務。

> ⚠️ **重要變更說明**
> 本專案已經過 `/auto-fix` 指令重構，將原本混亂的單一檔案架構重建為清晰的模組化結構。
> 現在 `main.py` 僅作為程式入口點，所有功能都已妥善拆分至獨立模組。

---

## 📋 專案簡介

TaskMaster 是個人任務管理工具，幫助你追蹤和管理日常工作。支援桌面 GUI 操作和 Web API 呼叫。

### 核心功能
- ✅ **任務管理**：新增、檢視、刪除任務
- 🔄 **狀態追蹤**：待辦、進行中、已完成
- 🎯 **優先級設定**：低、中、高三個等級
- 💾 **持久化儲存**：資料保存在本地 SQLite 資料庫

---

## 🏗️ 專案架構（重構後）

經過 `/auto-fix` 指令重構後，專案採用清晰的模組化架構：

```
F5757_ch09/
├── main.py           # 🚪 程式入口點（僅負責路由調度）
├── database.py       # 💾 資料庫管理模組
├── task_gui.py       # 🖥️  桌面 GUI 介面模組
├── api_server.py     # 🌐 Web API 服務模組
├── utils.py          # 🛠️  工具函式模組
├── config.py         # ⚙️  設定檔模組
├── check_db.py       # 🔍 資料庫檢查工具
└── .claude/          # 🤖 Claude Code 自定義指令
    ├── commands/     # 📂 自定義指令存放位置
    │   ├── auto-fix.md      # 自動修復流程指令
    │   ├── pack-zh.md       # 中文互動式提交指令
    │   ├── pack-basic.md    # 基礎提交流程指令
    │   └── pack-direct.md   # 強制指令執行指令
    └── settings.local.json  # Claude 本地設定
```

### 模組說明
- **main.py**：統一入口點，負責命令行參數解析和模式調度
- **database.py**：資料庫連線、CRUD 操作封裝
- **task_gui.py**：Tkinter GUI 視覺化介面
- **api_server.py**：Flask RESTful API 服務
- **utils.py**：共用工具函式
- **config.py**：集中式設定管理

---

## 🚀 快速開始

### 安裝相依套件

```bash
# 進入專案目錄
cd F5757_ch09

# 使用 uv 安裝套件
uv sync

# 或使用 pip
pip install -r requirements.txt
```

### 使用方法

**請參考 `main.py` 的最後部分（第 74-100 行）查看完整的使用說明**

```bash
# 🖥️ 啟動桌面 GUI 介面
python main.py gui

# 🌐 啟動 Web API 服務（瀏覽器訪問 http://127.0.0.1:5000）
python main.py api
# 或
python main.py web

# 💾 執行資料庫備份
python main.py backup

# 🔍 檢查資料庫狀態
python main.py check

# ❓ 顯示完整說明
python main.py help
```

---

## 🤖 Claude Code 自定義指令

本專案整合了 Claude Code 的自定義指令功能，**自定義指令存放於 `.claude/commands/` 目錄**：

### 可用指令

1. **`/auto-fix`** - 自動修復流程
   - 規劃 → 實作 → 逐步提交的完整工作流程
   - **本專案已用此指令重構**，將原本混亂的程式碼重建為模組化架構

2. **`/pack-zh`** - 中文互動式 Git 提交
   - 完整的提交流程，包含分支管理和中文提交訊息

3. **`/pack-basic`** - 基礎提交流程
   - 簡化的自動化提交流程

4. **`/pack-direct`** - 強制指令執行
   - 直接執行提交，跳過互動式流程

### 使用範例
```bash
# 在 Claude Code 中使用
/auto-fix 修復登入表單驗證
/pack-zh .
```

### 自定義指令說明
- 這些指令是 Claude Code 的擴充功能
- 可以依照專案需求自行編寫新的指令檔案
- 指令檔案格式為 Markdown（`.md`）
- 存放於 `.claude/commands/` 目錄下即可自動載入

---

## 🗄️ 資料結構

### 資料庫：tasks.db
SQLite 資料庫，包含 `tasks` 表格：

| 欄位 | 型別 | 說明 |
|------|------|------|
| id | INTEGER PRIMARY KEY | 任務 ID |
| title | TEXT | 任務標題 |
| description | TEXT | 任務描述 |
| priority | TEXT | 優先級（low/medium/high） |
| status | TEXT | 狀態（pending/in_progress/completed） |
| created_at | TEXT/TIMESTAMP | 建立時間 |

---

## 🌐 API 端點

| 方法 | 路徑 | 說明 |
|------|------|------|
| GET | `/api/tasks` 或 `/tasks` | 取得所有任務 |
| POST | `/api/tasks` 或 `/tasks` | 建立新任務 |
| DELETE | `/api/tasks/<id>` | 刪除指定任務 |

### API 回應格式
```json
{
  "success": true,
  "data": [...],
  "message": "操作成功"
}
```

---

## 💻 技術架構

- **語言**：Python 3.11+
- **GUI 框架**：Tkinter
- **Web 框架**：Flask
- **資料庫**：SQLite
- **API 格式**：RESTful JSON

---

## 📝 開發指南

### 系統需求
- Python 3.11 或更高版本
- Flask（Web 模式必需）
- tkinter（GUI 模式，通常為 Python 內建）

### 開發注意事項
- 所有功能已模組化，修改時請找到對應模組
- 資料庫操作請透過 `database.py` 的 `DatabaseManager` 類別
- GUI 相關功能請修改 `task_gui.py`
- API 端點請修改 `api_server.py`
- 新增設定項目請更新 `config.py`

### 參考 main.py 的使用說明
詳細的使用方法和範例請參考 `main.py` 檔案第 74-100 行的 `show_help()` 函式。

---

## 🎯 專案重構成果

透過 `/auto-fix` 指令，本專案已完成以下改進：

✅ 將混亂的單一檔案拆分為清晰的模組
✅ `main.py` 簡化為純入口點（僅 160 行）
✅ 統一的資料庫管理介面
✅ 獨立的 GUI 和 API 模組
✅ 改善的錯誤處理和程式碼可讀性
✅ 便於維護和擴展的架構

### 重構前後對比

| 項目 | 重構前 | 重構後 |
|------|--------|--------|
| 程式碼組織 | 所有功能混在 main.py | 清晰的模組化架構 |
| main.py 行數 | 500+ 行 | 160 行（僅入口點） |
| 維護性 | 困難，功能耦合 | 容易，功能獨立 |
| 可擴展性 | 低，修改影響範圍大 | 高，模組獨立擴展 |
| 程式碼重用 | 困難 | 容易，模組可重用 |

---

## 📄 授權

本專案僅供學習與練習使用。

---

## 🔗 相關連結

- [Python 官方文件](https://docs.python.org/3/)
- [Flask 文件](https://flask.palletsprojects.com/)
- [Tkinter 教學](https://docs.python.org/3/library/tkinter.html)
- [Claude Code 文件](https://docs.claude.com/)
