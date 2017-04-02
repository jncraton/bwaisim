import os

# importing AIBIN seems to change dirs, so get the path now
file = os.path.abspath('aiscript.bin')

import AIBIN
aibin = AIBIN.AIBIN()
aibin.load_file(file)

class Town:
  def __init__(self, first_town=False, mineral_patches=9, minerals_per_patch=1500, geysers=1, gas_per_geyser=5000):
    self.first_town = first_town
    self.owned = []
    self.minerals_remaining = mineral_patches * minerals_per_patch
    self.gas_remaining = geysers * gas_per_geyser

class Thread:
  def __init__(self, player, town=None, pc=0):
    self.player = player
    self.pc = pc # Program Counter
    self.town = town

  def do_tick(self):
  
    while True:
      command = self.player.commands[self.pc]
      self.pc += 1
      if hasattr(Thread, command['name']):
        getattr(Thread, command['name'])(self, *command['parameters'])
      else:
        print('unknown command: %s' % command)
        break

  def start_town(self):
    self.town = Town(len(player.towns) == 0)
    player.towns.append(self.town)

  def build(self, count, unit, priority):
    self.player.build_queue.append({
      'count': count,
      'unit': unit,
      'priority': priority,
      'town': self.town
    })
    player.do_build()

class Player:
  def __init__(self, commands):
    self.commands = commands
    self.towns = []
    self.threads = [Thread(self)]
    self.minerals = 50
    self.gas = 0
    self.tick = 0
    self.build_queue = []

    for command in self.commands:
      if command['name'] == 'build':
        self.race = command['parameters'][1]['name'].lower().split(' ')[0]

  def do_tick(self):
    for thread in self.threads:
      thread.do_tick()

    self.tick += 1

  def do_build(self):
    """ 
    Sorts the build queue begins building what is possible

    Resource and tech checks are currently not implemented   
    """
    self.build_queue = sorted(self.build_queue, key=lambda q: q['priority'])
    for item in self.build_queue:
      for i in range(0, item['count']['raw']):
        item['town'].owned.append(item['unit'])

player = Player(aibin.export_commands('TMCx'))
player.do_tick()