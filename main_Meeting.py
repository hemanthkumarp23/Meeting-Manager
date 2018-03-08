from module_Meeting import Meeting_Manager

myMeeting = Meeting_Manager()

while(True):

    y = eval(input("Choose the below option: \n 1. Want to see the available time \n 2. Want to schedule a meeting \n 3. Want to see the scheduled meeting\n"))

    if y == 1:
        myMeeting.time_view()

    elif y == 2:
        x = input("Please enter the time to meet: ")
        y = input("Please enter your name: ")
        myMeeting.schedule(x, y)

    elif y == 3:
        myMeeting.show_scheduled()

    else:
        break
