class Meeting_Manager(object):

    def __init__(self):
        self.schedule_time = {}
        self.available_time = ["10-10:45", "11-11:45", "12-12:45"]

    def time_view(self):
        print(self.available_time)

    def schedule(self, time, new_name):
        if time in self.available_time:
            self.schedule_time[time] = new_name
            self.available_time.remove(time)

        else:
            print("Please enter the proper time which is available {}".format(self.available_time))

    def show_scheduled(self):
        print(self.schedule_time)
