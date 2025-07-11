# Chapter 2 – Implementing Perceptrons and Backpropagation from Scratch

This chapter focuses on understanding how perceptrons and multilayer perceptrons (MLPs) work, along with key concepts like activation functions, forward propagation, loss functions, and backpropagation.

---

## 🧠 Key Concepts

- Structure of a single-layer perceptron and multilayer perceptron
- Role and types of activation functions (sigmoid, ReLU, tanh, etc.)
- Forward propagation of input through weighted connections
- Loss function: Mean Squared Error (MSE)
- Gradient-based optimization using backpropagation
- Updating weights using chain rule and derivatives

---

## 🧪 My Implementation: MLP for OR Gate

To solidify the theory, I implemented a basic 2-layer MLP using only NumPy, trained to model the logical OR gate.  
The model consists of:
- Input layer: 2 neurons  
- Hidden layer: 4 neurons with sigmoid activation  
- Output layer: 1 neuron with sigmoid activation

### 🔁 Training Logic

- **Loss function**: Mean Squared Error (MSE)  
- **Activation**: Sigmoid (with manual derivative)  
- **Epochs**: 5000  
- **Learning rate**: 0.1  
- **Optimizer**: Manual gradient descent (no library used)

---

## 🧮 Code Overview

```python
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [1], [1], [1]]

# Feedforward: X → Hidden Layer (Sigmoid) → Output Layer (Sigmoid)
# Backpropagation: Compute loss gradient → Update weights manually
