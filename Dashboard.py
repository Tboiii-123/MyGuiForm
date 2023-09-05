from tkinter import *
import sqlite3
from tkinter import messagebox

a=sqlite3.connect('Dashboard.db')   
a.commit()