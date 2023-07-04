from pybaseball import statcast

stats = statcast()

pitchCount = 0

for pitch in stats.balls:
    pitchCount = pitchCount + 1

print(pitchCount)
