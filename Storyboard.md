# Storyboard — Linear Transformations (M3 Internal Assessment)

**Student:** Ayush Sharma &nbsp;|&nbsp; **Student ID:** `E25B070912`

## One-Sentence Learning Objective
> *"By the end of this video, the viewer will be able to interpret any $2 \times 2$ matrix as a linear transformation on $\mathbb{R}^2$ — predicting where vectors land, how grids deform, and how the determinant encodes area scaling and orientation."*

---

## 6-Scene Storyboard Structure

| Scene | Duration & Timestamp | Purpose | Visual, Narration & Math Plan |
|---|---|---|---|
| **1. Hook / Context** | `00:00.0 – 00:41.9` (`41.9s`) | Spark curiosity and motivate why linear transformations matter. | **Visuals:** Opening frame (Title, Concept, Student Name & ID); real-world applications card (Graphics, Robotics, Data Science) paired with a 2D shape undergoing shear and $30^\circ$ rotation; central guiding question; full-grid teaser with $A = \begin{bmatrix}1.5 & 0.8\\ -0.3 & 1.2\end{bmatrix}$.<br>**Narration:** Connects arithmetic matrix multiplication to real spatial motion. |
| **2. Concept Introduction** | `00:41.9 – 01:43.8` (`61.9s`) | Define the concept, notation, and learning objective. | **Visuals:** Learning objective card; notation legend ($\mathbb{R}^2, \mathbf{u}, \mathbf{v}, c, \hat{\imath}, \hat{\jmath}$); Additivity $T(\mathbf{u}+\mathbf{v})=T(\mathbf{u})+T(\mathbf{v})$ & Homogeneity $T(c\mathbf{u})=cT(\mathbf{u})$ with live parallelogram & scaled-vector animation; Linear vs. Nonlinear grid contrast; derivation of $A\mathbf{x} = xT(\hat{\imath}) + yT(\hat{\jmath})$. |
| **3. Visual Intuition** | `01:43.8 – 02:43.6` (`59.8s`) | Build geometric intuition before heavy calculation. | **Visuals:** Split-screen plane with ghost reference grid, $\hat{\imath}$ (green), $\hat{\jmath}$ (red), $\mathbf{v}=(1,1)$ (gold), unit square, and orientation arc. Demonstrates 4 canonical maps: $90^\circ$ CCW rotation, $2\times$ horizontal stretch, horizontal shear, and $y$-axis reflection. |
| **4. Worked Example** | `02:43.6 – 03:39.7` (`56.1s`) | Demonstrate why and how matrix multiplication works step-by-step. | **Visuals:** Split-screen worked example for $A = \begin{bmatrix}2&1\\1&3\end{bmatrix}$ and $\mathbf{v} = \begin{bmatrix}2\\1\end{bmatrix}$: Step 1 ($T(\hat{\imath})=(2,1)$), Step 2 ($T(\hat{\jmath})=(1,3)$), Step 3 ($A\mathbf{v} = 2\begin{bmatrix}2\\1\end{bmatrix}+1\begin{bmatrix}1\\3\end{bmatrix}=\begin{bmatrix}5\\5\end{bmatrix}$), live grid deformation, tip-to-tail path, and length/angle verification ($\sqrt{5} \to 5\sqrt{2}$). |
| **5. Interpretation** | `03:39.7 – 04:24.4` (`44.7s`) | Connect algebra ($\det$) back to area, orientation, and invertibility. | **Visuals:** Three geometric regimes of $\det(M) = ad - bc$: (1) $\det(A) = +5$ scales unit square area $1 \to 5$ keeping CCW orientation; (2) $\det(B) = -2$ for $B=\begin{bmatrix}-1&1\\0&2\end{bmatrix}$ doubles area and flips orientation CW; (3) $\det(C) = 0$ for $C=\begin{bmatrix}2&1\\4&2\end{bmatrix}$ collapses $\mathbb{R}^2$ onto $y=2x$. |
| **6. Summary & Credits** | `04:24.4 – 04:59.6` (`35.2s`) | Reinforce takeaways and provide citations & disclosures. | **Visuals:** Three numbered summary cards; Closing Frame listing references (3Blue1Brown, Gilbert Strang, Manim CE v0.22), voice-over/music policy note, and AI tool disclosure. |

---

## Independent Mathematical Verification

1. **Basis Vector Images ($A = \begin{bmatrix}2&1\\1&3\end{bmatrix}$):**
   - $A\hat{\imath} = \begin{bmatrix}2&1\\1&3\end{bmatrix}\begin{bmatrix}1\\0\end{bmatrix} = \begin{bmatrix}2\\1\end{bmatrix}$ (Column 1).
   - $A\hat{\jmath} = \begin{bmatrix}2&1\\1&3\end{bmatrix}\begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}1\\3\end{bmatrix}$ (Column 2).
2. **Vector Mapping ($\mathbf{v} = \begin{bmatrix}2\\1\end{bmatrix}$):**
   - Row-dot product: $\begin{bmatrix}2(2)+1(1)\\ 1(2)+3(1)\end{bmatrix} = \begin{bmatrix}5\\5\end{bmatrix}$.
   - Column linear combination: $2\begin{bmatrix}2\\1\end{bmatrix} + 1\begin{bmatrix}1\\3\end{bmatrix} = \begin{bmatrix}4\\2\end{bmatrix} + \begin{bmatrix}1\\3\end{bmatrix} = \begin{bmatrix}5\\5\end{bmatrix}$.
   - Norms & angles: $\|\mathbf{v}\| = \sqrt{2^2+1^2} = \sqrt{5} \approx 2.24$ ($\theta \approx 26.57^\circ$); $\|A\mathbf{v}\| = \sqrt{5^2+5^2} = 5\sqrt{2} \approx 7.07$ ($\theta = 45^\circ$).
3. **Determinants & Areas:**
   - $\det(A) = (2)(3) - (1)(1) = 5$ (Area of parallelogram spanned by $(2,1)$ and $(1,3)$ is $|2\cdot 3 - 1\cdot 1| = 5$, positive $\implies$ CCW preserved).
   - $\det(B) = (-1)(2) - (1)(0) = -2$ ($|\det(B)| = 2$, negative $\implies$ orientation reversed to CW).
   - $\det(C) = (2)(2) - (1)(4) = 0$ (Column 1 $= 2 \times$ Column 2; all outputs lie on $y = 2x$, singular / non-invertible).
