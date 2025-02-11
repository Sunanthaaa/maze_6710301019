# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:38:59 2025

@author: sununtha
"""

import os
import time
# import keyboard 
from collections import deque
import turtle

screen = turtle.Screen()

class pos:
    def __init__(self, y, x):
        self.y = y
        self.x = x

class maze:
    def __init__(self):
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", " "],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", " ", " ", "X"],
            ["X", " ", "X", "X", "X", "X", "X"],
        ]
        self.ply = pos(5, 1)# ตำแหน่งเริ่มต้น
        self.end = pos(2, 6)# จุดสิ้นสุด
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"

    def isInBound(self, y, x):
        """ตรวจสอบว่าตำแหน่งอยู่ในขอบเขต"""
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            return True
        else:
            return False
        
    def print_maze(self):
         """แสดงผลเขาวงกต"""
         os.system("cls" if os.name == "nt" else "clear")  # รองรับทุกระบบปฏิบัติการ
         for row in self.maze:
             print(" ".join(row))
         print("\n[W] ขึ้น  [S] ลง  [A] ซ้าย  [D] ขวา  [Q] ออกจากเกม")    
         
    def move(self, next_move):
        if self.isInBound(next_move.y, next_move.x):
            if self.maze[next_move.y][next_move.x] in [" ", "E"]:
                self.maze[self.ply.y][self.ply.x] = " "
                self.ply = next_move
                self.maze[self.ply.y][self.ply.x] = "P"
                self.print_maze()
                time.sleep(0.3)

    def auto_solve(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # ขึ้น, ลง, ซ้าย, ขวา
        queue = deque()
        queue.append((self.ply, []))  # ตำแหน่งปัจจุบันเส้นทาง
        visited = set()
        visited.add((self.ply.y, self.ply.x))

        while queue:
            current_pos, path = queue.popleft()

            if current_pos.y == self.end.y and current_pos.x == self.end.x:
                for move in path:
                    self.move(move)
                print("> You Won <")
                return

            for dy, dx in directions:
                new_y, new_x = current_pos.y + dy, current_pos.x + dx
                if self.isInBound(new_y, new_x) and (new_y, new_x) not in visited:
                    if self.maze[new_y][new_x] in [" ", "E"]:
                        queue.append((pos(new_y, new_x), path + [pos(new_y, new_x)]))
                        visited.add((new_y, new_x))

if __name__ == '__main__':
    m = maze()
    m.print_maze() 
    time.sleep(1)
    m.auto_solve() 
    
# กดเดินทีละตัว
#     def is_in_bound(self, y, x):
#         """ตรวจสอบว่าตำแหน่งอยู่ในขอบเขต"""
#         return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])

#     def print_maze(self):
#         """แสดงผลเขาวงกต"""
#         os.system("cls" if os.name == "nt" else "clear")  # รองรับทุกระบบปฏิบัติการ
#         for row in self.maze:
#             print(" ".join(row))
#         print("\n[W] ขึ้น  [S] ลง  [A] ซ้าย  [D] ขวา  [Q] ออกจากเกม")

#     def move(self, dy, dx):
#         """ย้ายตัวละครไปยังตำแหน่งใหม่"""
#         next_pos = pos(self.ply.y + dy, self.ply.x + dx)

#         if self.is_in_bound(next_pos.y, next_pos.x):
#             next_cell = self.maze[next_pos.y][next_pos.x]

#             if next_cell == " " or next_cell == "E":
#                 self.maze[self.ply.y][self.ply.x] = " "  # ลบตำแหน่งเดิม
#                 self.maze[next_pos.y][next_pos.x] = "P"  # ย้ายตำแหน่งใหม่
#                 self.ply = next_pos  # อัปเดตตำแหน่งผู้เล่น

#                 if next_cell == "E":
#                     self.print_end()
#                     return False  # จบเกม
#         return True

#     def print_end(self):
#         """แสดงข้อความเมื่อถึงจุดสิ้นสุด"""
#         os.system("cls" if os.name == "nt" else "clear")
#         print("\n\n>>>>> Congratulation!!! You reached the end! <<<<<\n")
#         input("กด Enter เพื่อออก...")  # รอให้กดปุ่มก่อนออก
        
# class pos:
#     def __init__(self, y, x) -> None:
#         self.y = None
#         self.x = None
    
#     def __init__(self, y, x) -> None:
#         self.y = y
#         self.x = x

# if __name__ == '__main__':
#     m = maze()
#     m.print_maze()

#     while True:
#         move = input("Move (W/A/S/D): ").strip().lower()
#         if move == "q":
#             print("Quit Program")
#             break
#         if move == "w" and not m.move(-1, 0): break  # ขึ้น
#         if move == "s" and not m.move(1, 0): break  # ลง
#         if move == "a" and not m.move(0, -1): break  # ซ้าย
#         if move == "d" and not m.move(0, 1): break  # ขวา
#         m.print_maze()
