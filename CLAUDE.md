# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

請用中文撰寫相關文件
回應都請使用中文

## 專案概述

TaskMaster 是一個任務管理應用程式，包含：
- Tkinter GUI 介面
- Flask API 伺服器
- SQLite 資料庫儲存

### 安裝相依套件
```bash
# 使用 uv 安裝套件
uv sync

# 或使用 pip
pip install -r requirements.txt
```

## 常用指令

### 執行應用程式
```bash
# 執行 GUI 介面
uv run python main.py gui

# 執行 API 伺服器 (port 5000)
uv run python main.py api

# 執行獨立 API 伺服器 (port 8080)
uv run python api_server.py
```

### 資料庫操作
```bash
# 檢查資料庫
python check_db.py
```

## 程式碼架構

### 核心檔案
- `main.py` - 主程式，包含 GUI、資料庫操作和 Flask API（整合式架構）
- `api_server.py` - 獨立的 Flask API 伺服器（port 8080）
- `database.py` - 資料庫管理類別
- `task_gui.py` - GUI 相關程式碼
- `utils.py` - 工具函式
- `config.py` - 設定檔

### 資料庫結構
SQLite 資料庫 `tasks.db`，包含 `tasks` 表格：
- id (INTEGER PRIMARY KEY)
- title (TEXT)
- description (TEXT)
- priority (TEXT) - 預設 'low'
- status (TEXT) - 預設 'pending'
- created_at (TEXT/TIMESTAMP)

### API 端點
- GET `/api/tasks` 或 `/tasks` - 取得所有任務
- POST `/api/tasks` 或 `/tasks` - 建立新任務
- DELETE `/api/tasks/<id>` - 刪除任務

## 已知問題與技術債

1. 程式碼組織混亂 - `main.py` 包含太多功能
2. 有兩個不同的 API 伺服器實作（port 5000 和 8080）
3. 資料庫連線管理不一致
4. 缺乏完整的錯誤處理
5. API 回應格式不一致
6. 測試覆蓋率不足
7. 硬編碼的設定值（如 API key、資料庫路徑）

## 開發注意事項

- 修改資料庫操作時，注意有多個不同的實作方式
- GUI 和 API 功能混在同一檔案中，修改時要小心影響範圍
- 使用 Python 3.11.8 開發

## Git 工作流程與指令規範

### 🚨 重要：必須嚴格遵守的指令規範

#### 提交流程規範
- **一律使用 `/pack-zh` 指令進行提交**
- 禁止直接使用 `git add` 和 `git commit` 指令
- `/pack-zh` 指令會處理完整的提交流程

#### 自動修復流程規範
- **當用戶要求修復功能、Bug、檔案問題時，一律使用 `/auto-fix` 指令**
- 適用情境包括但不限於：
  - 修復程式碼 Bug
  - 修復功能問題
  - 修復檔案錯誤
  - 實作新功能
  - 重構程式碼
  - 任何需要修改檔案的任務
- 範例觸發詞彙：「修復」、「修改」、「實作」、「加入」、「更新」、「重構」
- `/auto-fix` 會執行完整的規劃→實作→測試→提交流程
