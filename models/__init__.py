#!/usr/bin/python3
"""
    Module that initiaties an instance for an application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
