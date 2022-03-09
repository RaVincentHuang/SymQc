# The ans of test.qcis

**Init state** is: 
$$
\left(\alpha_{Q1} \ket{0_{Q1}} + \beta_{Q1} \ket{1_{Q1}}\right) \left(\alpha_{Q2} \ket{0_{Q2}} + \beta_{Q2} \ket{1_{Q2}}\right)
$$

```assembly
1. CNOT	Q1	Q2
```

$$
\left[\begin{matrix}0 & 1\\1 & 0\end{matrix}\right]
$$
$$
\alpha_{Q1} \alpha_{Q2} \ket{0_{Q1}0_{Q2}} + \alpha_{Q1} \beta_{Q2} \ket{1_{Q1}1_{Q2}} + \alpha_{Q2} \beta_{Q1} \ket{1_{Q1}0_{Q2}} + \beta_{Q1} \beta_{Q2} \ket{0_{Q1}1_{Q2}}
$$
```assembly
2. CNOT	Q1	Q2
```

$$
\left[\begin{matrix}0 & 1\\1 & 0\end{matrix}\right]
$$
$$
\alpha_{Q1} \alpha_{Q2} \ket{0_{Q1}0_{Q2}} + \alpha_{Q1} \beta_{Q2} \ket{0_{Q1}1_{Q2}} + \alpha_{Q2} \beta_{Q1} \ket{1_{Q1}0_{Q2}} + \beta_{Q1} \beta_{Q2} \ket{1_{Q1}1_{Q2}}
$$
**Final state** is: 
$$
\alpha_{Q1} \alpha_{Q2} \ket{0_{Q1}0_{Q2}} + \alpha_{Q1} \beta_{Q2} \ket{0_{Q1}1_{Q2}} + \alpha_{Q2} \beta_{Q1} \ket{1_{Q1}0_{Q2}} + \beta_{Q1} \beta_{Q2} \ket{1_{Q1}1_{Q2}}
$$

