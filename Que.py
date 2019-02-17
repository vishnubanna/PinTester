class Que:

    def __init__(self, length = "void"):
        if length == "void":
            self.length = 10000
        else:
            self.length = length
        self.list = []

    def put(self, term):
        if len(self.list) >= 0:
            self.list = self.list + [0]
            for i in range(len(self.list)-1, -1 , -1):
                self.list[i] = self.list[i - 1]
            self.list[0] = term
        else:
            print("que is full")

    def get(self):
        try:
            if len(self.list) >= 0:
                queue = []
                value = self.list[len(self.list)-1]
                for i in range(0, len(self.list) - 1):
                    queue.append(self.list[i])
                self.list = queue
                return value
        except:
            return

    #called = False

    def get_noremove(self):
        global called
        called = True
        return self.list[len(self.list)-1]

        # find a way to make sure that if task_done is not called after the function will five an error

    def task_done(self):

        #if called == True:
        called = False
        queue = []
        self.list[len(self.list) - 1] = 0
        for i in range(0, len(self.list) - 1):
            queue.append(self.list[i])
        self.list = queue
        # edit so that that value is false if a task is not finished, and as a result the values are not
        return False
        '''
        elif len(self.list) == 0:
            print("queue is empty")
            return False
        elif called == False:
            print("you need to call get_noremove to call this function")
            return False
        '''

    def tasks_done(self):
        if len(self.list) == 0:
            return False
        else:
            return True

    def lister(self):
        print(self.list)
        return self.list

    def has_values(self):
        test = 0
        check = self.list + [0]
        if len(check) > 1:
            return True
        else:
            return False
