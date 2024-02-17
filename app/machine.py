class Machine:

    def __init__(self, df):
        pass

    def __call__(self, feature_basis):
        pass

    def save(self, filepath):
        pass

    @staticmethod
    def open(filepath):
        pass

def info(self, df):
        output = (
            f"Model Used: {self.name} ",
            f"Timestamp: {df['Timestamp'][0]}"
        )
        return "<br>".join(output)
