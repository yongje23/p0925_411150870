# Python SQLite 學生管理系統 (Student Management System)

這是一個使用 Python 和 SQLite 開發的學生管理系統專案，滿足作業要求包含 .db 文件和 .py 文件。

## 專案文件結構

```
project/
├── database_setup.py      # 資料庫初始化腳本
├── student_management.py  # 主要應用程式
└── student_database.db    # SQLite 資料庫文件 (執行後生成)
```

## 功能特色

### 1. 資料庫設計
- **students** 表：儲存學生基本資訊
  - id (主鍵)
  - name (姓名)
  - age (年齡)
  - email (電子郵件，唯一)
  - major (科系)  
  - gpa (GPA成績)

- **courses** 表：儲存課程資訊
  - course_id (主鍵)
  - course_name (課程名稱)
  - instructor (授課教師)
  - credits (學分數)
  - semester (學期)

- **enrollments** 表：儲存選課記錄
  - enrollment_id (主鍵)
  - student_id (外鍵)
  - course_id (外鍵)
  - grade (成績)
  - enrollment_date (選課日期)

### 2. 核心功能
- 新增學生
- 查詢所有學生
- 根據學號查詢特定學生
- 更新學生GPA
- 根據科系查詢學生
- 查詢課程選課名單
- 查詢學生選課記錄

## 使用方法

### 步驟一：建立資料庫
```bash
python database_setup.py
```
這會創建 `student_database.db` 文件並插入範例資料。

### 步驟二：執行主程式
```bash
python student_management.py
```
這會執行各種資料庫操作的示範。

## 範例資料

### 學生資料
- 張小明 (Computer Science, GPA: 3.8)
- 李小華 (Mathematics, GPA: 3.6)
- 王小美 (Physics, GPA: 3.9)
- 陳小強 (Engineering, GPA: 3.5)
- 林小芳 (Biology, GPA: 3.7)

### 課程資料
- Python Programming (Prof. Smith)
- Database Systems (Prof. Johnson)
- Data Structures (Prof. Brown)
- Web Development (Prof. Davis)
- Machine Learning (Prof. Wilson)

## 技術特點

1. **參數化查詢**：防止 SQL 注入攻擊
2. **錯誤處理**：完整的異常處理機制
3. **物件導向設計**：使用類別封裝功能
4. **資料庫關聯**：正確使用外鍵關聯
5. **中文支援**：支援中文字符儲存和顯示

## 作業要求符合度

✅ 包含 .db 文件 (student_database.db)  
✅ 包含 1-2 個 .py 文件 (database_setup.py, student_management.py)  
✅ 使用 Python, SQL, SQLite 技術  
✅ 完整的資料庫操作 (CRUD)  
✅ 可直接執行的程式碼  

## 執行環境需求

- Python 3.x
- sqlite3 模組 (Python 內建)

## GitHub 連結參考

可參考類似專案結構：
- https://github.com/zaoa3345678-arch/aaron-lesson_sql.git

## YouTube 學習資源

搜尋關鍵字：python, sql, sqlite