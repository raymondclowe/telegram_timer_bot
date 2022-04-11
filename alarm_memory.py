import json
import time

# define the memory class
class AlarmMemory:
    def __init__(self):
        self.memory_filename = "alarm-memory.json"
        self.alarms = {}
        
        self.load_memory()

    def load_memory(self):
        try:
            with open(self.memory_filename, 'r') as f:
                self.alarms = json.load(f)
        except:
            pass

    def save_memory(self):
        with open(self.memory_filename, 'w') as f:
            json.dump(self.alarms, f)

    def add_alarm(self, user_id, alarmtime):
        # does an alarm for this time already exist
        if alarmtime in self.alarms:
            # append this user id to the list of user ids for this time
            self.alarms[alarmtime].append(user_id)
        else:
            # create a new alarm
            self.alarms[alarmtime] = {'user_ids' : [user_id]}
    
    def due_alarms(self, current_time):
    
        # return all alarms that are due
        due_alarms = []
        for alarmtime in self.alarms:
            if alarmtime <= current_time:
                due_alarms.append(self.alarms[alarmtime])
        return due_alarms
    
    
    def delete_alarm_by_time(self, current_time):
        # delete alarms for this time or before
        new_alarmtimes = {}
        for alarmtime in self.alarms:
            if alarmtime > current_time:
                new_alarmtimes.append(self.alarms[alarmtime]    )
        self.alarms = new_alarmtimes
    
    def delete_alarm_by_user(self, user_id):
        # delete alarms for this user
        for alarmtime in self.alarms:
            if user_id in self.alarms[alarmtime]:
                self.alarms[alarmtime].remove(user_id)
                if len(self.alarms[alarmtime]) == 0:
                    del self.alarms[alarmtime]