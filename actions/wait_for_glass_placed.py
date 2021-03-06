"""Waits for the glas to be placed on the caddy"""

from time import sleep

from actions.action import Action

class WaitForGlassPlaced(Action):
    def __call__(self, robot):
      sleep(.1)
      self.initial = robot.load_cell.recent_summary(secs=.1)
      sleep(.1)
      while True:
        self.summary = robot.load_cell.recent_summary(secs=.1)
        if self.summary.mean > self.initial.mean + self.initial.stddev * 3:
          return
