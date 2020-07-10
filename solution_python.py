from enum import Enum

class Event(Enum):
    """
    Used to keep track of history events
    """
    Add = 1
    Subtract = 2

class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        # used to keep a stack trace history of our events
        self.undo_history = []
        self.redo_history = []

    def add(self, num: int):
        self.undo_history.append([Event.Add, num])
        self.value += num


    def subtract(self, num: int):
        self.undo_history.append([Event.Subtract, num])
        self.value -= num

    def __str__(self):
        return f"{self.value} {self.undo_history} {self.redo_history}"


    def _undo(self):
        # helper method for undo and bulk_undo
        if self.undo_history:
            event = self.undo_history.pop()
            if event[0] == Event.Add:
                self.value -= event[1]
            elif event[0] == Event.Subtract:
                self.value += event[1]
            self.redo_history.append(event)
            return True
        return False

    def _redo(self):
        # helper method for redo and bulk_redo
        if self.redo_history:
            event = self.redo_history.pop()
            if event[0] == Event.Add:
                self.value += event[1]
            elif event[0] == Event.Subtract:
                self.value -= event[1]
            self.undo_history.append(event)
            return True
        return False

    def undo(self):
        self._undo()

    def redo(self):
        self._redo()

    def bulk_undo(self, steps: int):
        for step in range(steps):
            if not self._undo():
                return

    def bulk_redo(self, steps: int):
        for step in range(steps):
            if not self._redo():
                return
