data =  open("Day10/test_input.txt", "r").read().split("\n")

# Part One

curr = 1
signal_strength = 20
cycle = 0
sum_signals = 0

for line in data:
    if line[:4] == "addx":
        for i in range(2):
            cycle += 1
            if cycle == signal_strength:
                sum_signals += curr *signal_strength         
                signal_strength += 40
        curr += int(line[5:])
    else:
        cycle += 1
        if cycle == signal_strength:
                sum_signals += curr *signal_strength            
                signal_strength += 40
                           
print(sum_signals)

def choose_char(i, x):
  if x == i or x+1 == i or x+2 == i: return '#'
  return '.'


# Part 2 - not my solution

from textwrap import wrap

cycles = []

with open('Day10/input.txt', 'r') as f:
  for line in f:
    if 'noop' in line:
      cycles.append(0)
    elif 'addx' in line:
      _, v = line.strip().split()
      cycles.extend([0, int(v)])
    else:
      print('instruction not implemented')

def choose_char(i, x):
  if x == i or x+1 == i or x+2 == i: return '#'
  return '.'

strengths = []
x = 1
crt = ''

for i, v in enumerate(cycles, start=1):
  crt += choose_char(i%40, x)
  if i in [20, 60, 100, 140, 180, 220]:
    strengths.append(i*x)
  x += v

for row in (wrap(crt, width=40)):
  print(row)