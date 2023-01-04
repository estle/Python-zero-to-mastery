# string indexes [lesson 034 on hard_drive]
selfish = 'meme meme'
#          012345678

print(3*selfish[0].upper())

print(f'{selfish[8]}\n')

# indexes advanced usage string[start:stop:stepover]
print('[start:stop:stepover]')
print(selfish[0:3])
print(selfish[1:8:3])
print(selfish[:6])
print(f'{selfish[::1]}\n')
# negative indexes and going backwards (reverse)
print(selfish[-1])
print(selfish[::-1])
print(selfish[::-2])
