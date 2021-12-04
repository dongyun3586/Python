x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]

W = 2.0
b = 0.5

h = []

for v in x_data:
    h.append(W*v+b)

# hypothesis = W * x_data + b
print(h)