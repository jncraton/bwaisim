import os

# importing AIBIN seems to change dirs, so get the path now
file = os.path.abspath('aiscript.bin')

import AIBIN
aibin = AIBIN.AIBIN()
aibin.load_file(file)

class Town:
  def __init__(self, mineral_patches=9, minerals_per_patch=1500, geysers=1, gas_per_geyser=5000):
    self.owned = []
    self.minerals_remaining = mineral_patches * minerals_per_patch
    self.gas_remaining = geysers * gas_per_geyser

class Thread:
  def __init__(self, player, pc=0):
    self.player = player
    self.pc = pc

  def do_tick(self):
    print(self.player.commands[self.pc])

class Player:
  def __init__(self, commands):
    self.commands = commands
    self.threads = [Thread(self)]
    self.minerals = 50
    self.gas = 0
    self.tick = 0

    for command in self.commands:
      if command['name'] == 'build':
        self.race = command['parameters'][1]['name'].lower().split(' ')[0]

    town = Town()
    if self.race == 'terran':
      town.owns = ['terran scv', 'terran scv', 'terran scv', 'terran scv', 'terran command center']

    self.towns = [town]

  def do_tick(self):
    for thread in self.threads:
      thread.do_tick()

    self.tick += 1

player = Player(aibin.export_commands('TMCx'))
player.do_tick()