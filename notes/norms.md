The main difference is which dimension they normalize over and how they calculate the normalization statistics.

## 1. BatchNorm (Batch Normalization)

Normalizes features using statistics calculated across the batch dimension.

\\[ y = \gamma \frac{x-\mu_B}{\sqrt{\sigma_B^2+\epsilon}}+\beta \\]

- Calculates mean and variance across the batch.
- Maintains running mean and variance for inference.
- Commonly used in CNNs.

Intuition: Normalizes each channel using statistics collected from different samples in the batch.

## 2. LayerNorm (Layer Normalization)

Normalizes features across the feature dimension of each individual sample.

\\[ y = \gamma \frac{x-\mu_L}{\sqrt{\sigma_L^2+\epsilon}}+\beta \\]

- Each sample is normalized independently.
- Does not depend on other samples in the batch.
- Commonly used in Transformers.

Intuition: Normalizes all features belonging to one sample independently of other samples.

## 3. RMSNorm

Similar to LayerNorm, but doesn't subtract the mean.

\\[ y = \gamma \frac{x}{\sqrt{\frac{1}{d}\sum\_{i=1}^{d}x_i^2+\epsilon}} \\]

- Normalizes using root mean square.
- No mean subtraction.
- Usually computationally cheaper than LayerNorm.
- Commonly used in modern LLMs.

## 4. Side-by-side comparison

| Property              | BatchNorm    | LayerNorm       | RMSNorm         |
| --------------------- | ------------ | --------------- | --------------- |
| Normalization         | Across batch | Across features | Across features |
| Subtracts mean        | Yes          | Yes             | No              |
| Uses variance         | Yes          | Yes             | No              |
| Learnable scale       | Yes          | Yes             | Yes             |
| Learnable bias        | Yes          | Yes             | Usually no      |
| Depends on batch size | Yes          | No              | No              |
| Common use            | CNNs         | Transformers    | LLMs            |

## 5. Visual intuition

Imagine an input tensor with shape:

\\[ (B,C,H,W) \\]

- BatchNorm2d: For each channel, calculates statistics across \\(B,H,W\\).
- LayerNorm: Typically normalizes across the specified trailing dimensions, such as \\(C,H,W\\), independently for each sample.
- RMSNorm: Same general idea as LayerNorm, but uses RMS instead of mean and variance.

My recommendation for your CNN experiments:

- Start with BatchNorm2d as your baseline.
- Experiment with GroupNorm or LayerNorm for alternative normalization behavior.
- Try RMSNorm as an additional experiment.

One important consideration: LayerNorm and RMSNorm need careful dimension handling in CNNs, since their normalized dimensions depend on how you define the input shape.