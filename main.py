import turtle 
import math
import random

win=turtle.Screen()
win.bgcolor("black")

def a1():
  akki=turtle.Turtle()
  akki.color('white')
  akki.speed(0)
  #rotate=int(360)

  def dcircle(t, size):
    for i in range(10):
      t.circle(size)
      size=size-4
  def dspecial(t, size, repeat):
    for i in range(repeat):
      dcircle(t, size)
      t.right(360/repeat)
      
  dspecial(akki,100,10)


def a2():
  akki=turtle.Turtle()
  akki.color('yellow')
  akki.speed(0)
  #rotate=int(360)

  def dcircle(t, size):
    for i in range(10):
      t.circle(size)
      size=size-6
  def dspecial(t, size, repeat):
    for i in range(repeat):
      dcircle(t, size)
      t.right(360/repeat)
      
  dspecial(akki,100,10)


def a3():
  akki=turtle.Turtle()
  akki.color('blue')
  akki.speed(0)
  #rotate=int(360)

  def dcircle(t, size):
    for i in range(10):
      t.circle(size)
      size=size-5
  def dspecial(t, size, repeat):
    for i in range(repeat):
      dcircle(t, size)
      t.right(360/repeat)
      
  dspecial(akki,100,10)

def a4():
  akki=turtle.Turtle()
  akki.color('orange')
  akki.speed(0)
  #rotate=int(360)

  def dcircle(t, size):
    for i in range(10):
      t.circle(size)
      size=size-18
  def dspecial(t, size, repeat):
    for i in range(repeat):
      dcircle(t, size)
      t.right(360/repeat)
      
  dspecial(akki,100,10)

def a5():
  akki=turtle.Turtle()
  akki.color('pink')
  akki.speed(0)
  #rotate=int(360)

  def dcircle(t, size):
    for i in range(10):
      t.circle(size)
      size=size-20
  def dspecial(t, size, repeat):
    for i in range(repeat):
      dcircle(t, size)
      t.right(360/repeat)
      
  dspecial(akki,100,10)


a=[a1,a2,a3,a4,a5]
for i in range(len(a)):
  a[i]()

