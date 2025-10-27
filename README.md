# TaskMaster - 個人任務管理系統

一個簡單的任務管理應用程式，展示 Claude Code 自定義指令的實際應用。

> **Ch10 專案成果展示分支 (custom_tk)**
> 本分支展示了 Ch10 完成後的成果，解決了互動式指令在 GitHub Actions 上的問題，並實際應用 `/auto-fix-step` 指令完成 GUI 框架升級。

---

## ⚠️ 重要注意事項

### Fork 本專案後的必要設定

如果你 Fork 了這個專案並想使用 GitHub 上的 Claude Code Workflow，**必須先完成以下設定**：

1. **安裝 Claude GitHub App**
   - 前往 [Claude GitHub App](https://github.com/apps/claude-code) 安裝頁面
   - 將 Claude Code 應用程式安裝到你的 GitHub 帳號
   - 授權存取你 Fork 的專案

2. **為什麼需要安裝？**
   - 本專案的 Workflow 使用 Claude Code 進行自動化任務
   - 沒有安裝 Claude GitHub App，Workflow 將無法呼叫 Claude Code
   - 無法執行 `/auto-fix-step` 等自定義指令

3. **安裝後即可使用**
   - GitHub Actions 中的 Claude Code Workflow 將正常運作
   - 可以透過 Workflow 執行程式碼修改、測試等任務

> 💡 **提示**：詳細安裝步驟請參考文末的「相關連結」章節

---

## 🎯 Ch10 成果總結

### 核心成就
- ✅ **解決 GitHub Actions 互動式指令問題**：創建了 `/auto-fix-step` 指令
- ✅ **實戰驗證**：使用 `/auto-fix-step` 將 Tkinter GUI 升級為 CustomTkinter
- ✅ **逐步執行模式**：適合 CI/CD 環境的分步工作流程
- ✅ **保留互動彈性**：在必要時仍可與使用者互動

### 技術突破

#### 1. `/auto-fix-step` 指令
- **問題**：原本的 `/auto-fix` 指令完全互動式，在 GitHub Actions 中無法運作
- **解決方案**：創建逐步執行版本，每次只執行一個項目，但保留互動能力
- **特色**：
  - 分步執行：每次處理一個任務項目
  - 適合 CI/CD：可在 GitHub Actions 中使用
  - 保留互動：必要時仍可與使用者確認
  - 獨立提交：每步獨立提交，便於追蹤和回溯

#### 2. 實戰案例：GUI 框架升級
- **任務**：將 Tkinter 改為 CustomTkinter
- **方法**：使用 `/auto-fix-step` 逐步完成多個改動
- **成果**：順利完成複雜的框架遷移，展示指令的實用性

### 專案演進歷程
1. **Ch09**：建立本地 Claude Code 自定義指令，實作 `/auto-fix`
2. **Ch10**：解決 GitHub 協作問題，創建 `/auto-fix-step`
3. **custom_tk 分支**：實際應用新指令完成 GUI 升級

---

## 📋 功能特色

- 桌面 GUI 介面 (Tkinter)
- Web API 服務 (Flask)
- SQLite 資料庫
- 任務管理 (新增、檢視、刪除)

---

## 🚀 快速開始

```bash
# 安裝套件
uv sync

# 啟動 GUI
uv run python main.py gui

# 啟動 API (http://127.0.0.1:5000)
uv run python main.py api
# 或
uv run python main.py web

# 🔍 檢查資料庫狀態
uv run python main.py check

# ❓ 顯示完整說明
uv run python main.py help

```

---

## 🤖 Claude Code 自定義指令

本專案的核心特色是整合了 Claude Code 自定義指令：

### 可用指令

- `/auto-fix` - 完整互動式工作流程（適合本地開發）
- **`/auto-fix-step`** - **逐步執行版本（適合 GitHub Actions）**
- `/pack-zh` - 中文互動式 Git 提交流程
- `/commit-rules` - Git 提交訊息規範

### 指令說明

#### `/auto-fix` vs `/auto-fix-step`
| 特性 | `/auto-fix` | `/auto-fix-step` |
|------|-------------|------------------|
| 執行方式 | 一次完成所有任務 | 每次執行一個項目 |
| 適用環境 | 本地開發 | GitHub Actions / CI/CD |
| 互動性 | 完全互動式 | 保留必要互動能力 |
| 提交策略 | 任務完成後提交 | 每步獨立提交 |

### 指令檔案位置

```
.claude/
└── commands/
    ├── auto-fix.md       # 完整自動修復流程
    ├── auto-fix-step.md  # 逐步執行版本（GitHub Actions 專用）
    ├── pack-zh.md        # 中文提交指令
    ├── pack-basic.md     # 基礎提交流程
    ├── pack-direct.md    # 強制執行提交
    └── commit-rules.md   # 提交訊息規範
```

**本分支展示了如何使用 `/auto-fix-step` 在 GitHub 環境中進行複雜的程式碼修改任務**

---

## 🏗️ 專案架構

```
F5757_ch09/
├── main.py          # 程式入口點
├── database.py      # 資料庫管理
├── task_gui.py      # GUI 介面
├── api_server.py    # API 服務
└── .claude/         # Claude Code 自定義指令（Ch10 將整合至 GitHub）
```

---

## 💻 技術棧

- Python 3.11+
- **CustomTkinter** (現代化 GUI，使用 `/auto-fix-step` 從 Tkinter 升級而來)
- Flask (API)
- SQLite (資料庫)
- Claude Code 自定義指令

---

## 📝 授權

本專案僅供學習與練習使用。

---

## 🔗 相關連結

### 技術文件
- [CustomTkinter 官方文件](https://customtkinter.tomschimansky.com/) - 現代化的 Tkinter UI 套件
- [CustomTkinter GitHub](https://github.com/TomSchimansky/CustomTkinter) - 開源專案與範例

### Claude Code 整合
- [Claude GitHub App](https://github.com/apps/claude-code) - 在 GitHub 上安裝 Claude Code 應用程式
- [Claude Code 文件](https://docs.claude.com/en/docs/claude-code) - 官方使用文件
- [Claude Code 自定義指令指南](https://docs.claude.com/en/docs/claude-code/custom-commands) - 如何建立自定義指令
