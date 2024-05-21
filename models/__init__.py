#!/usr/bin/python3
"""Initializes the package"""
from models.engine.file_storage import FileStorage
""" Create an instance of FileStorage and assign it to the variable storage"""
storage = FileStorage()
""" Call the reload method on the storage variable """
storage.reload()
