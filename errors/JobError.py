class JobError(Exception):
    def __init__(self, state, message):
        self.state = state
        self.message = message
        super().__init__(self.message)
        