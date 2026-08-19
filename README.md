# 📝 To-Do List Application (Tkinter)

A simple, clean, and fully functional desktop To-Do List application built using Python and Tkinter. This project focuses on clarity, ease of use, and complete task management — making it a great beginner-friendly yet feature-rich productivity tool.

---

## 🚀 Features

### ✅ Task Management
- **Add new tasks** — Simple input field and button to quickly add items
- **Delete selected tasks** — Remove individual tasks from either tab
- **Mark tasks as completed** — Move tasks from pending to completed
- **Clear all tasks** — Bulk delete (with confirmation) to start fresh
- **Task persistence** — All tasks survive app restarts via JSON save/load

### 🗂️ Two-Tab Layout
- **Pending Tasks** — View all incomplete items at a glance
- **Completed Tasks** — Separate tab to review finished work
- Clear visual separation helps users track progress and stay motivated

### 💾 Smart Save & Load System
- **Auto-save to JSON** — Tasks saved with automatic timestamp and numbering
- **Load any session** — Restore previous To-Do lists by selecting saved files
- **Preserves both sections** — Completed tasks stay marked when reloaded
- **Auto-creates save directory** — `To_Do_Saves/` folder created automatically

### 🎨 User Experience
- Clean Tkinter GUI with intuitive layout
- Color-coded buttons (add, delete, clear, mark complete)
- Responsive design that works on Windows, Mac, and Linux
- No external dependencies — just Python built-ins

---

## 🔧 Technologies Used

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.x |
| **GUI Framework** | Tkinter (built-in) |
| **Data Storage** | JSON files |
| **Utilities** | OS, Datetime (built-in) |

**Why Tkinter?** — Included in Python by default, cross-platform, lightweight, perfect for learning GUI development.

---

## 📦 Installation & Quick Start

### Requirements
- Python 3.6+ (built-in Tkinter, JSON, OS modules)
- No external packages needed

### Run the App
```bash
# Clone the repository
git clone https://github.com/Sanjay-AI-ML/To-Do-List.git
cd To-Do-List

# Run (no install required!)
python todo_app.py
```

The GUI window opens immediately. The `To_Do_Saves/` directory is created automatically on first save.

---

## 🎮 How to Use

### Adding a Task
1. Type your task in the **"Enter a task..."** input field
2. Click **"Add Task"** or press Enter
3. Task appears in the "Pending Tasks" tab

### Marking Tasks as Complete
1. Select a task from the "Pending Tasks" list
2. Click **"Mark as Completed"**
3. Task moves to "Completed Tasks" tab
4. Can still delete from there if needed

### Deleting Tasks
1. Select a task from either tab
2. Click **"Delete Task"**
3. Task is permanently removed

### Clearing All Tasks
1. Click **"Clear All Tasks"**
2. Confirm the dialog (prevents accidental loss)
3. All tasks deleted

### Saving Your Session
1. Click **"Save Tasks"** button
2. Automatically saves to `To_Do_Saves/tasks_YYYYMMDD_HHMMSS.json`
3. File includes timestamp for easy tracking

### Loading a Previous Session
1. Click **"Load Tasks"**
2. Select a previously saved JSON file
3. All tasks (pending + completed) restored

---

## 🗂️ Project Structure

```
To-Do-List/
├── README.md             # Documentation (this file)
├── todo_app.py           # Main GUI application
└── To_Do_Saves/          # Auto-created on first save
    ├── tasks_20260819_103045.json
    ├── tasks_20260819_154320.json
    └── ...
```

### File Format: `tasks_YYYYMMDD_HHMMSS.json`
```json
{
  "pending_tasks": [
    "Buy groceries",
    "Finish project report",
    "Call mom"
  ],
  "completed_tasks": [
    "Review emails",
    "Team standup meeting"
  ],
  "saved_at": "2026-08-19 15:43:20"
}
```

---

## 🧠 Code Architecture

### `todo_app.py`
```python
class TodoApp:
    def __init__(self, root):
        # Initialize GUI components
        # Create two tabs (pending/completed)
        # Set up buttons and listboxes
    
    def add_task(self):
        # Validate input, add to pending list
    
    def mark_completed(self):
        # Move selected task from pending to completed
    
    def delete_task(self):
        # Remove task from current tab
    
    def save_tasks(self):
        # Serialize to JSON with timestamp
    
    def load_tasks(self):
        # Deserialize from JSON, restore both tabs
```

**Design Pattern:** MVC-inspired with clear separation of UI (Tkinter widgets) and logic (task operations).

---

## 💡 Key Features Explained

### Why Two Tabs?
- **Psychology**: Seeing completed tasks builds motivation
- **Clarity**: Separates "what I need to do" from "what I did"
- **Workflow**: Keeps the pending list focused and actionable

### Why Auto-Timestamped Files?
- Never overwrite accidentally (each save is unique)
- Easy to track when you saved (history preserved)
- Can revert to older sessions if needed

### Why JSON Over Database?
- **Simple** — Just text files, no server setup
- **Portable** — Copy `To_Do_Saves/` anywhere
- **Inspectable** — Edit files directly if needed
- **Scalable** — Works fine for personal use (database overkill)

---

## 🚀 Usage Examples

### Daily Workflow
```
Morning:
  1. Run app: python todo_app.py
  2. Load yesterday's session
  3. Review completed tasks (motivating!)
  4. Add new tasks for today
  5. Work through them

Evening:
  6. Mark done tasks as completed
  7. Save session
  8. Close app
```

### Load a Backup
```
Had a bad day and want to restore yesterday's state?
  1. Click "Load Tasks"
  2. Select tasks_20260818_173000.json
  3. Everything restored
```

---

## 🎓 Educational Value

This project is excellent for learning:
- ✅ **GUI Development** — Tkinter widgets (Label, Button, Listbox, Entry)
- ✅ **Event-Driven Programming** — Buttons trigger callback functions
- ✅ **File I/O** — JSON save/load operations
- ✅ **Data Structures** — Lists, dictionaries, object properties
- ✅ **Clean Code** — Modular functions, clear naming
- ✅ **Layout Management** — Tkinter Grid and Frame systems
- ✅ **Error Handling** — File not found, invalid input handling

---

## 🔒 Security & Reliability

- ✅ **File Safety** — Timestamped filenames prevent overwrites
- ✅ **Validation** — Empty task check prevents adding blank items
- ✅ **Confirmation** — "Clear All" asks before deleting
- ✅ **Exception Handling** — Graceful errors for missing/corrupt files
- ✅ **Cross-Platform** — Works on Windows, macOS, Linux

---

## 🐛 Troubleshooting

### App won't start
```bash
# Verify Python is installed
python --version  # Should be 3.6+

# Tkinter is usually included. If missing:
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS (via Homebrew)
brew install python-tk

# Then run
python todo_app.py
```

### Tkinter import error
```bash
# Make sure Tkinter is installed (see above)
# Then restart terminal and try again
```

### Can't find saved file
- Check `To_Do_Saves/` folder exists in the same directory as `todo_app.py`
- If missing, click "Save Tasks" to recreate it

### Tasks disappeared
- Did you forget to save before closing? Always click "Save Tasks" first!
- Check recent files in `To_Do_Saves/` folder

---

## 🎨 Customization Ideas

Want to extend the app? Try:

- 🎯 **Priority Levels** — Add High/Medium/Low tags
- 🎯 **Due Dates** — Calendar picker for deadlines
- 🎯 **Categories** — Organize tasks by work/personal/health
- 🎯 **Dark Mode** — Toggle between light/dark themes
- 🎯 **Task Notes** — Click to add details to each task
- 🎯 **Search** — Find tasks by keyword
- 🎯 **Undo/Redo** — Navigate edit history
- 🎯 **Drag & Reorder** — Rearrange task priority
- 🎯 **Sound Notifications** — Alert when task marked complete
- 🎯 **Cloud Sync** — Save to Google Drive or Dropbox

---

## 📈 Future Enhancements

- Multi-user profiles (different To-Do lists per person)
- Recurring tasks (daily, weekly, monthly)
- Reminders/notifications
- Integration with calendar apps
- Export to PDF or CSV
- Mobile app companion
- Web-based version (Flask + SQLite)

---

## 📄 License

MIT — Free to use and modify. See LICENSE file.

---

## 👤 Author

Built by [@Sanjay-AI-ML](https://github.com/Sanjay-AI-ML)

Questions, feedback, or feature requests? Open an issue on GitHub!

Enjoy your more organized life! ✨
