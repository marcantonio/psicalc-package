from psicalc import normalized_mutual_info_score as nmi
#from psicalc.nmi import mutual_info_score as nmi
import numpy as np
from decimal import Decimal, getcontext
#from sklearn.metrics import mutual_info_score

# (17, 81): 0.7187984457259526
# (81, 17): 0.7187984457259525
#a = np.array([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0, 11, 11, 11, 0, 9, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0, 11, 11, 11, 11, 18, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0, 0])
#b = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0])

# (128, 127): 1.0
# (127, 128): 0.0
a = np.array([17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 8, 17, 17, 8, 17, 17, 17, 7, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 0])
b = np.array([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 12, 3, 3, 12, 3, 3, 3, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0])

# a = [1, 2, 3, 2, 1]
# b = [1, 2, 3, 1, 1]

x = nmi(a, b)
y = nmi(b, a)

print(x)
print(y)

#print(mutual_info_score(a, b))
#print(mutual_info_score(b, a))

getcontext().prec = 30


def mutual_info(true, pred):
    classes = np.unique(true)
    clusters = np.unique(pred)

    contingency_matrix = np.zeros((len(classes), len(clusters)))

    for i, class_label in enumerate(classes):
        for j, cluster_label in enumerate(clusters):
            contingency_matrix[i, j] = np.sum((true == class_label) & (pred == cluster_label))

    samples = len(true)
    jp = contingency_matrix / samples

    marginal_prob_true = np.sum(jp, axis=1)
    marginal_prob_pred = np.sum(jp, axis=0)

    mi = 0
    for i in range(len(classes)):
        for j in range(len(clusters)):
            if jp[i, j] > 0:
                mi += jp[i, j] * np.log2(jp[i, j] / (marginal_prob_true[i] * marginal_prob_pred[j]))


def mutual_info_prec(true, pred):
    classes = np.unique(true)
    clusters = np.unique(pred)

    contingency_matrix = np.zeros((len(classes), len(clusters)), dtype=object)

    for i, class_label in enumerate(classes):
        for j, cluster_label in enumerate(clusters):
            contingency_matrix[i, j] = Decimal(int(np.sum((true == class_label) & (pred == cluster_label))))

    samples = Decimal(len(true))
    jp = contingency_matrix / samples

    marginal_prob_true = np.sum(jp, axis=1)
    marginal_prob_pred = np.sum(jp, axis=0)

    mi = Decimal(0)
    log2 = Decimal(2).ln()
    for i in range(len(classes)):
        for j in range(len(clusters)):
            if jp[i, j] > 0:
                mi += jp[i, j] * (jp[i, j].ln() - (marginal_prob_true[i] * marginal_prob_pred[j]).ln()) / log2


# mutual_info(a, b)
# mutual_info(b, a)
# mutual_info_prec(a, b)
# mutual_info_prec(b, a)
