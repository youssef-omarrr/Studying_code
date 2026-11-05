Both are widely used in modern deep learning architectures, especially Transformers and LLMs.

## 1. RMSNorm (Root Mean Square Normalization)

[LayerNorm Limitations and RMSNorm Advantages | Dhwanit Agarwal, PhD posted on the topic | LinkedIn](https://images.openai.com/static-rsc-4/uhuxgoRi03ZXh0EjeX-LIvLDabBEV42I__DkxoX-NP6FPGbUhFlMRiQUig1csLdr-Pn83CSmaOUA2Gq2Qlw-c53I7eoigK896ux1ez_EafVtXmKWG4CdND7fM4M4kCSJDGZA-_M_m19iUddYCjjKPXfs0w4Iyje61eqZan-Iugg?purpose=inline)

RMSNorm is a normalization technique similar to LayerNorm, but simpler and computationally cheaper.

It normalizes activations using their root mean square, without subtracting the mean.

\\[ \text{RMSNorm}(x)= \frac{x}{\sqrt{\frac{1}{d}\sum\_{i=1}^{d}x_i^2+\epsilon}} \odot \gamma \\]

Where:

- \\(d\\): Number of features.
- \\(\epsilon\\): Small value for numerical stability.
- \\(\gamma\\): Learnable scaling parameter.

Difference from LayerNorm:

| LayerNorm                     | RMSNorm               |
| ----------------------------- | --------------------- |
| Subtracts mean                | Doesn't subtract mean |
| Divides by standard deviation | Divides by RMS        |
| Scale + bias (typically)      | Usually scale only    |
| More computation              | Less computation      |

Why use it? More computationally efficient normalization while maintaining stable training.

## 2. MoE (Mixture of Experts)

[Tutorials/mixture-of-experts/MoE-Paper-Review.ipynb at main · clint-kristopher-morris/Tutorials · GitHub](https://images.openai.com/static-rsc-4/AUshijfpsoVLw_WkhA_ieIRcVv3hOao8MIya8QPwQkvvxdJmZ1B3ZguTNP9VSA-K6b7i0Uu3P5XVonca78WpUjsEPJZLlkN6lBDxO7StnFKwR1luwRHUKL6r1fXeWruHrBttNMe2kfilQs4RAfeBNd3kJMyYw8sz2MD7qD_g0JY?purpose=inline)

MoE is an architecture where instead of using one large neural network for every input, you have multiple smaller networks called experts.

A router decides which experts should process each input.

For example, imagine having 4 experts:

- Expert 1: Learns one type of pattern.
- Expert 2: Learns another type of pattern.
- Expert 3: Learns another type of pattern.
- Expert 4: Learns another type of pattern.

The router selects the most relevant experts.

The output can be represented as:

\\[ y = \sum\_{i\in TopK}g_i(x)E_i(x) \\]

Where:

- \\(E_i(x)\\): Output of expert \\(i\\).
- \\(g_i(x)\\): Router's weight for that expert.
- TopK: Only the K highest-scoring experts are activated.

Why use it?

- Increases model capacity without activating the entire model for every input.
- Allows experts to specialize in different patterns.
- Reduces computation compared with a dense model of equivalent total parameter count.

## 3. Main differences

| RMSNorm                        | MoE                              |
| ------------------------------ | -------------------------------- |
| Normalization technique        | Model architecture               |
| Stabilizes activations         | Distributes computation          |
| Reduces normalization overhead | Enables sparse expert activation |
| Used inside network layers     | Often replaces FFN layers        |

For your CNN experiments:

- RMSNorm: Worth experimenting with as an alternative to BatchNorm.
- MoE: Interesting if you want to experiment with multiple specialized feature-processing branches and a learned router.

One important point: MoE doesn't automatically make a model better. Expert specialization and load balancing are important, otherwise some experts may receive most of the training traffic while others barely learn.