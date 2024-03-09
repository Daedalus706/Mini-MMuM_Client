from .trigger import TRIGGER

class Effect:
    def __init__(self, name:str, rounds_active:int, reduce_countdown_triggers:list[TRIGGER], cleansable:bool) -> None:
        self.name:str = name
        self.rounds_active:int = rounds_active
        self.reduce_countdown_triggers:TRIGGER = reduce_countdown_triggers

        self.cleansable = cleansable

        self.countdown:int = rounds_active
        
        self.remove = False

    def do_trigger(self, trigger:TRIGGER):
        if self.remove:
            return
        
        if trigger == self.reduce_countdown_trigger:
            self.countdown -= 1