import numpy as np

study_hours = np.array([40, 30, 20, 0, 10])
IQ = np.array([110, 120, 100, 90, 80])
test_score = np.array([100, 90, 80, 70, 60])

study_hours = (study_hours - np.mean(study_hours)) / np.std(study_hours)
IQ = (IQ - np.mean(IQ)) / np.std(IQ)

X = np.column_stack((np.ones(len(study_hours)), study_hours, IQ))
y = test_score

theta = np.zeros(X.shape[1])

def hypothesis(X, theta):
    return np.dot(X, theta)

def cost_function(X, y, theta):
    m = len(y)
    return np.sum((hypothesis(X, theta) - y) ** 2) / (2 * m)

def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)
    theta_history = [list(theta)]
    partial_derivatives_history = []
    for i in range(iterations):
        h = hypothesis(X, theta)
        gradient = np.dot(X.T, (h - y)) / m
        theta -= alpha * gradient
        theta_history.append(list(theta))
        
        # Compute partial derivatives (gradients) for this iteration
        partial_derivatives = np.dot(X.T, (h - y)) / m
        partial_derivatives_history.append(list(partial_derivatives))
    return theta_history, partial_derivatives_history

alpha = 0.01
iterations = 4
theta_history, partial_derivatives_history = gradient_descent(X, y, theta, alpha, iterations)

for i, (theta_values, partials) in enumerate(zip(theta_history, partial_derivatives_history)):
    print(f"Iteration {i}:")
    print(f"Thetas: {theta_values}")
    print(f"Partial Derivatives: {partials}")
    print()
