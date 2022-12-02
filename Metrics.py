from sklearn.metrics import accuracy_score, f1_score


def report(acc, f1):
    return f"Accuracy: {acc:.4f} F1 Score: {[round(score,4) for score in f1]}"

def eval(model, x_tr, x_te, y_tr, y_te):
    yh = model.predict(x_tr)
    print("Training Result: ", report(accuracy_score(y_tr, yh), f1_score(y_tr, yh, average=None)))

    yh = model.predict(x_te)
    print("Testing  Result: ", report(accuracy_score(y_te, yh), f1_score(y_te, yh, average=None)))