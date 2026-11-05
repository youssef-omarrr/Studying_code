All three are variations of residual connections, designed to improve information flow and gradient propagation in deep neural networks.

## 1. Normal residual block

[ResNet-50 for Image Classification | MindSpore 2.0.0-alpha Tutorials | MindSpore](https://images.openai.com/static-rsc-4/U6trckL4Akw402UsVRRy4HfIddQYbNDgq-0329cL900Rb8o_Lw6ycib077QdGAzWrGcAtnWRYnbBXo2VpEnYEfY9-Y7UGoAv8piEJGZYHr-PxOnez-Qdiy3Z3XSm1auZ-tfQdTPPG63ompv2o48DQYbHGwCN7ojI3RvpMSQpKKM?purpose=inline)

The standard residual block learns a residual function instead of directly learning the entire transformation.

\\[ y = F(x) + x \\]

- \\(x\\): Original input.
- \\(F(x)\\): Output of convolutional layers (usually Conv + BN + Activation).
- Addition: Combines the original input with the learned features.

Why?

- Helps prevent vanishing gradients.
- Makes deeper networks easier to train.
- Allows information to bypass convolutional layers.

## 2. Gated residual block

[Gated Residual Networks: A Modern Secret Weapon for Tabular Deep Learning | by Abish Pius | Writing in the World of Artificial Intelligence | Medium](https://images.openai.com/static-rsc-4/m13PK7T-l1uTsZW6_rUFoGciSRvwAZMrV5_AURBF4daZmp-b5Az7BzYcoWQNPnIVTK-JfG44f5oiXMSU1_p-wXZOryZfjA7Ddkr0ggG2bgPl1A_IqsoT3Yz28hlUDp3SEQBRPMf_cxMTGMTHlcRYQFadfS2MACL2cEagiVPDXxs?purpose=inline)

Instead of always adding the input directly, it learns a gate that controls how much information passes through each path.

A simplified formulation:

\\[ y = g(x)\odot F(x) + (1-g(x))\odot x \\]

Where:

- \\(g(x)=\sigma(W_gx+b_g)\\)
- \\(\sigma\\): Sigmoid activation, producing values between 0 and 1.
- \\(\odot\\): Element-wise multiplication.

Why?

The network learns whether to:

- Favor newly extracted features.
- Preserve the original input.
- Combine both.

Unlike a normal residual block, the skip connection is no longer an unconditional addition.

## 3. Manifold / Hyper connections

[DeepSeek Just Fixed the “Input” Problem in Deep Learning | by Saqib Qamar | Jan, 2026 | Medium](https://images.openai.com/static-rsc-4/zpR1KiklJMNIyvFC-GRu67JmeybwiHcI99sv6-Wsq8IJKMpV0CxPb5V510TlqQ9w68N2TuxjjN_q_rGGBoykI6D0gATrNf8DxtI8tfQdQt8hA5RZABlBBUybVA3-r48y-BjHL-qlfXt44N4dt89YCUXZU_caGEAMvhmCEtG-kjY?purpose=inline)

Hyper-connections generalize the traditional single residual connection into multiple interconnected streams.

Instead of having just one skip connection, they allow information to flow through multiple paths, with learnable mixing coefficients.

A simplified conceptual formulation:

\\[ y_i = \sum_j \alpha\_{ij}F_j(x_j) \\]

Where:

- \\(x_j\\): Different feature streams.
- \\(F_j\\): Transformations applied to those streams.
- \\(\alpha\_{ij}\\): Learnable mixing coefficients.

Why?

- Allows richer information exchange.
- Provides more flexible feature propagation.
- Can improve representation capacity.
- Generalizes the simple identity skip connection.

Note: Hyper-connections are a broader family, and specific architectures such as Manifold-Constrained Hyper-Connections (mHC) impose constraints on the mixing operations to improve training stability.

## 4. Main differences

| Property       | Normal residual | Gated residual | Hyper-connections |
| -------------- | --------------- | -------------- | ----------------- |
| Skip paths     | One             | One (gated)    | Multiple          |
| Feature mixing | Addition        | Learned gate   | Learned mixing    |
| Learnable skip | No              | Yes            | Yes               |
| Complexity     | Low             | Medium         | Higher            |
| Flexibility    | Low             | Medium         | High              |


One important distinction: Hyper-connections are not simply gated residual blocks with more gates. They change the structure of information flow itself.

## 5. Attention Residuals (AttnRes)
Attention Residuals (AttnRes) are an alternative to standard residual connections. Instead of simply adding the outputs of previous layers, they use attention to decide how much information to retrieve from each previous layer.

### 1. Normal residual connections

In a traditional deep network, residual connections repeatedly add the previous representation:

\\[ x_l = x\_{l-1} + F_l(x\_{l-1}) \\]

The problem is that information from earlier layers gets accumulated through repeated additions. This can lead to uncontrolled growth and make it difficult to selectively retrieve earlier features.

### 2. Attention residuals

Instead of adding only the immediately preceding representation, attention residuals use attention over previous layer outputs.

A simplified formulation:

\\[ x_l = \sum\_{i=0}^{l-1} \alpha\_{li} h_i \\]

Where:

- \\(h_i\\): Output from an earlier layer.
- \\(\alpha\_{li}\\): Attention weight assigned to that layer.
- The weights determine how much information each previous layer contributes.

The network learns which previous representations are useful for the current layer.

[Attention Residuals: Teaching transformers to choose which layers matter](https://images.openai.com/static-rsc-4/DiaAiFnMS2vpWTqLCUxaUk0uItoiFvZbAHjUmdTq6xBvpqLmc4rjQ-7WrTPAMWFo6c1bT8vxLVLhkrALkH8R4kfyKuF42FJRRagtmYNPHWfopkc9BHmxXIXT_BxXEyJmUwai7BpaTCeL7U7_lQ24GutHs2LjqRyR0_7Opnf3NA8?purpose=inline)

### 3. Main differences

| Property                        | Normal residual | Attention residual             |
| ------------------------------- | --------------- | ------------------------------ |
| Information source              | Previous layer  | Multiple previous layers       |
| Feature mixing                  | Addition        | Attention-weighted combination |
| Learnable weights               | No              | Yes                            |
| Selective information retrieval | No              | Yes                            |
| Complexity                      | Low             | Higher                         |

### 4. How does it compare to Hyper-connections?

This is an important distinction:

- Residual connections: Direct addition of the previous representation.
- Attention residuals: Attention-based selection and combination of previous layer representations.
- Hyper-connections: Multiple residual streams with learnable information mixing.

Attention residuals focus on which previous layer information to retrieve, while hyper-connections focus on how information flows between multiple streams.