# identity_vector_model.py

class IdentityVector:
    def __init__(self, emotion, cognition, expression, value, bias):
        self.E = emotion
        self.C = cognition
        self.X = expression
        self.V = value
        self.B = bias

    def as_vector(self):
        return self.E + self.C + self.X + self.V + self.B
