"""Backup and recovery system for To-Do List application."""

import json
import os
from pathlib import Path
from datetime import datetime
import shutil

SAVES_DIR = Path(__file__).resolve().parent / "To_Do_Saves"
BACKUP_DIR = SAVES_DIR / "backups"
RECOVERY_FILE = SAVES_DIR / ".recovery"


def ensure_dirs():
    """Create necessary directories."""
    SAVES_DIR.mkdir(exist_ok=True)
    BACKUP_DIR.mkdir(exist_ok=True)


def create_backup(save_file):
    """Create backup of save file before loading."""
    ensure_dirs()
    try:
        if save_file.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = BACKUP_DIR / f"backup_{timestamp}_{save_file.name}"
            shutil.copy2(save_file, backup_file)
            print(f"✓ Backup created: {backup_file}")
            return backup_file
    except Exception as e:
        print(f"✗ Backup error: {e}")
    return None


def auto_backup_on_save(data):
    """Create automatic backup when saving."""
    ensure_dirs()
    try:
        # Create timestamped auto-save for recovery
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        auto_backup = BACKUP_DIR / f"autosave_{timestamp}.json"
        
        with open(auto_backup, 'w') as f:
            json.dump(data, f, indent=2)
        
        return auto_backup
    except Exception as e:
        print(f"✗ Auto-backup error: {e}")
    return None


def detect_corruption(save_file):
    """Detect corrupted save files."""
    try:
        with open(save_file, 'r') as f:
            data = json.load(f)
        
        # Validate structure
        if not isinstance(data, dict):
            return True, "File is not a JSON object"
        
        if "pending_tasks" not in data or "completed_tasks" not in data:
            return True, "Missing required task lists"
        
        if not isinstance(data["pending_tasks"], list):
            return True, "Pending tasks is not a list"
        
        if not isinstance(data["completed_tasks"], list):
            return True, "Completed tasks is not a list"
        
        return False, "File is valid"
    
    except json.JSONDecodeError as e:
        return True, f"JSON corruption: {e}"
    except Exception as e:
        return True, f"Unexpected error: {e}"


def recover_from_backup():
    """Recover latest valid backup."""
    ensure_dirs()
    
    backups = sorted(BACKUP_DIR.glob("*.json"), reverse=True)
    
    for backup_file in backups:
        corrupted, msg = detect_corruption(backup_file)
        if not corrupted:
            print(f"✓ Recovery: Using backup from {backup_file.name}")
            try:
                with open(backup_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"✗ Recovery failed: {e}")
                continue
    
    print("✗ No valid backups found, starting fresh")
    return {"pending_tasks": [], "completed_tasks": [], "saved_at": datetime.now().isoformat()}


def list_backups():
    """List all available backups."""
    ensure_dirs()
    
    backups = sorted(BACKUP_DIR.glob("*.json"), reverse=True)
    
    if not backups:
        print("No backups available.")
        return []
    
    print(f"\n{'#':<3} | {'Type':<10} | {'Timestamp':<19} | {'File Size':<10} | {'File Name':<40}")
    print("-" * 90)
    
    for i, backup in enumerate(backups, 1):
        try:
            size = backup.stat().st_size
            is_autosave = "autosave" in backup.name
            backup_type = "AUTO" if is_autosave else "MANUAL"
            
            with open(backup, 'r') as f:
                data = json.load(f)
            timestamp = data.get('saved_at', 'unknown')[:19]
            
            size_str = f"{size} bytes"
            print(f"{i:<3} | {backup_type:<10} | {timestamp:<19} | {size_str:<10} | {backup.name:<40}")
        except Exception as e:
            print(f"{i:<3} | ERROR    | {'unknown':<19} | {'?':<10} | {backup.name:<40}")
    
    return backups


def restore_backup(backup_filename):
    """Restore from specific backup."""
    ensure_dirs()
    
    backup_file = BACKUP_DIR / backup_filename
    
    if not backup_file.exists():
        print(f"✗ Backup not found: {backup_filename}")
        return None
    
    corrupted, msg = detect_corruption(backup_file)
    if corrupted:
        print(f"✗ Backup is corrupted: {msg}")
        return None
    
    try:
        with open(backup_file, 'r') as f:
            data = json.load(f)
        print(f"✓ Restored from: {backup_filename}")
        print(f"  Pending: {len(data.get('pending_tasks', []))} | Completed: {len(data.get('completed_tasks', []))}")
        return data
    except Exception as e:
        print(f"✗ Restore failed: {e}")
        return None


def cleanup_old_backups(keep_count=20):
    """Remove old backups, keeping only the most recent N."""
    ensure_dirs()
    
    backups = sorted(BACKUP_DIR.glob("*.json"), reverse=True)
    
    if len(backups) > keep_count:
        to_delete = backups[keep_count:]
        for backup in to_delete:
            try:
                backup.unlink()
                print(f"✓ Deleted old backup: {backup.name}")
            except Exception as e:
                print(f"✗ Failed to delete {backup.name}: {e}")
        
        return len(to_delete)
    
    return 0
