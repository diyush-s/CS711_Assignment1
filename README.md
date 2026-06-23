# Breaking a Hamming Physical Unclonable Function (PUF) with Linear Models

This repository contains a high-performance machine learning modeling attack on a 32-bit Hamming Physical Unclonable Function (PUF). By projecting the raw challenge bits into a higher-dimensional polynomial feature space, we prove that the non-linear thresholding operations of this hardware architecture can be perfectly linearized and bypassed using standard linear classifiers like Support Vector Machines (`LinearSVC`) and `LogisticRegression`.

This project was developed by team **TinyML** as part of **CS771: Introduction to Machine Learning** at the **Indian Institute of Technology Kanpur**.

---

## Project Overview

A 32-bit Hamming PUF evaluates a secret 32-bit word **s** and a secret threshold **t**. Given a challenge **c**, it computes partial Hamming weights **h_e** and **h_o** (on even and odd bit positions) from the bitwise XOR result **m = c ⊕ s**. The final hardware response is 1 if **h_e × h_o ≥ t**, and 0 otherwise.

By algebraically expanding the product, we map the challenge into a **288-dimensional feature space**. This project demonstrates that without true cryptographic non-linearities, the Hamming PUF remains fundamentally insecure against simple linear classification attacks.

### Performance Summary
* **Peak Test Accuracy:** > 99.7% in a fraction of a second.
* **Optimization Efficiency:** `squared_hinge` loss paired with a primal solver achieves a **6.8x speedup** over dual formulations.
* **Sample Complexity Threshold:** Only ~5,000 training points are needed to reliably cross the 99% accuracy threshold.

---

## Contributors (Team TinyML)

* **Dheeraj Kumar** (Department of Electrical Engineering, IIT Kanpur)
* **Amar Kumar** (Department of Electrical Engineering, IIT Kanpur)
* **Diyush S** (Department of Electrical Engineering, IIT Kanpur)
* **Arushia H** (Department of Mechanical Engineering, IIT Kanpur)
* **Akhil Joseph** (Department of Mechanical Engineering, IIT Kanpur)

---

## References

1. Fan, R.-E. et al. (2008). *LIBLINEAR: A library for large linear classification*. Journal of Machine Learning Research, vol. 9, pp. 1871-1874.
2. Pedregosa, F. et al. (2011). *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, vol. 12, pp. 2825-2830.
3. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
4. Kar, P. (2026). *Lecture Slides for CS771: Introduction to Machine Learning*, Indian Institute of Technology Kanpur.

