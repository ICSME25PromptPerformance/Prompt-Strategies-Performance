class MetricsCalculator:
    def __init__(self):
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0

    def update(self, predicted_labels, true_labels):
        for pred, true in zip(predicted_labels, true_labels):
            if pred == 1 and true == 1:
                self.true_positives += 1
            elif pred == 1 and true == 0:
                self.false_positives += 1
            elif pred == 0 and true == 1:
                self.false_negatives += 1
            elif pred == 0 and true == 0:
                self.true_negatives += 1

    def precision(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        if self.true_positives + self.false_positives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_positives)

    def recall(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        if self.true_positives + self.false_negatives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_negatives)

    def f1_score(self, predicted_labels, true_labels):
        precision = self.precision(predicted_labels, true_labels)
        recall = self.recall(predicted_labels, true_labels)
        if precision + recall == 0:
            return 0.0
        return 2 * (precision * recall) / (precision + recall)

    def accuracy(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        total = self.true_positives + self.false_positives + self.false_negatives + self.true_negatives
        if total == 0:
            return 0.0
        return (self.true_positives + self.true_negatives) / total