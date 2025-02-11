# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:03:51 2025

@author: phorn
"""

import turtle
import time
from collections import deque

CELL_SIZE = 40  # ขนาดของแต่ละช่องในเขาวงกต

class Pos:
    def __init__(self, y, x):
        self.y = y
        self.x = x

class Maze:
    def __init__(self):
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", "E"],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", " ", " ", "X"],
            ["X", "P", "X", "X", "X", "X", "X"],
        ]
        self.ply = Pos(5, 1)  
        self.end = Pos(2, 6)  
        
        # ตั้งค่าหน้าจอ turtle
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("white")
        self.screen.tracer(0)

        # เตรียมตัวเต่าแทนผู้เล่น
        self.player = turtle.Turtle()
        self.player.shape("turtle")  # เปลี่ยนเป็นรูปร่างเต่า
        self.player.color("purple")
        self.player.penup()
        self.player.speed(1)  # ปรับความเร็วของเต่า

        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()

        # วาดเขาวงกต
        self.draw_maze()

    def draw_maze(self):
        """ฟังก์ชันวาดเขาวงกต"""
        self.t.penup()
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                screen_x = x * CELL_SIZE - 120
                screen_y = 120 - y * CELL_SIZE
                if self.maze[y][x] == "X":
                    self.draw_cell(screen_x, screen_y, "black")
                elif self.maze[y][x] == "E":
                    self.draw_cell(screen_x, screen_y, "red")

        # วางตัวละครผู้เล่น
        self.move_player(self.ply.x, self.ply.y, 0)

    def draw_cell(self, x, y, color):
        """วาดช่องของเขาวงกต"""
        self.t.goto(x, y)
        self.t.pendown()
        self.t.fillcolor(color)
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(CELL_SIZE)
            self.t.right(90)
        self.t.end_fill()
        self.t.penup()

    def move_player(self, x, y, angle):
        """ย้ายตัวละครผู้เล่นไปตำแหน่งใหม่และหมุนหัวตามทิศทาง"""
        self.player.setheading(angle)  # หมุนหัวเต่าให้ตรงกับทิศทาง
        screen_x = x * CELL_SIZE - 100
        screen_y = 100 - y * CELL_SIZE
        self.player.goto(screen_x, screen_y)

    def move(self, next_move):
        """เคลื่อนที่ตัวละคร"""
        direction_angle = {
            (-1, 0): 90,   # ขึ้น
            (1, 0): 270,   # ลง
            (0, -1): 180,  # ซ้าย
            (0, 1): 0      # ขวา
        }

        dy = next_move.y - self.ply.y
        dx = next_move.x - self.ply.x

        if self.maze[next_move.y][next_move.x] in [" ", "E"]:
            self.ply = next_move
            angle = direction_angle.get((dy, dx), 0)
            self.move_player(self.ply.x, self.ply.y, angle)
            self.screen.update()
            time.sleep(0.3)

            if self.ply.y == self.end.y and self.ply.x == self.end.x:
                print("> You Won <")
                return True
        return False

    def auto_solve(self):
        """ใช้ BFS หาทางออกและแสดงการเคลื่อนที่"""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(self.ply, [])])
        visited = {(self.ply.y, self.ply.x)}

        while queue:
            current_pos, path = queue.popleft()
            for dy, dx in directions:
                new_y, new_x = current_pos.y + dy, current_pos.x + dx
                if (0 <= new_y < len(self.maze) and 0 <= new_x < len(self.maze[0]) 
                        and (new_y, new_x) not in visited and self.maze[new_y][new_x] in [" ", "E"]):
                    
                    new_pos = Pos(new_y, new_x)
                    queue.append((new_pos, path + [new_pos]))
                    visited.add((new_y, new_x))

                    if new_y == self.end.y and new_x == self.end.x:
                        for move in path + [new_pos]:
                            if self.move(move):
                                return

if __name__ == '__main__':
    game = Maze()
    time.sleep(1)
    game.auto_solve()
    turtle.done()