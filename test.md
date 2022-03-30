# The ans of test.qcis

**Init state** is: 
$$
\left(\alpha_{Q1} \ket{0_{Q1}} + \beta_{Q1} \ket{1_{Q1}}\right) \left(\alpha_{Q2} \ket{0_{Q2}} + \beta_{Q2} \ket{1_{Q2}}\right)
$$

```assembly
1. H	Q1
```

$$
\left[\begin{matrix}\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2}\\\frac{\sqrt{2}}{2} & - \frac{\sqrt{2}}{2}\end{matrix}\right]
$$
$$
\left(\alpha_{Q2} \ket{0_{Q2}} + \beta_{Q2} \ket{1_{Q2}}\right) \left(\ket{0_{Q1}} \left(\frac{\sqrt{2} \alpha_{Q1}}{2} + \frac{\sqrt{2} \beta_{Q1}}{2}\right) + \ket{1_{Q1}} \left(\frac{\sqrt{2} \alpha_{Q1}}{2} - \frac{\sqrt{2} \beta_{Q1}}{2}\right)\right)
$$
```assembly
2. CNOT	Q1	Q2
```

$$
\left[\begin{matrix}0 & 1\\1 & 0\end{matrix}\right]
$$
$$
\alpha_{Q2} \ket{0_{Q1}0_{Q2}} \left(\frac{\sqrt{2} \alpha_{Q1}}{2} + \frac{\sqrt{2} \beta_{Q1}}{2}\right) + \alpha_{Q2} \ket{0_{Q1}1_{Q2}} \left(\frac{\sqrt{2} \alpha_{Q1}}{2} - \frac{\sqrt{2} \beta_{Q1}}{2}\right) + \beta_{Q2} \ket{1_{Q1}0_{Q2}} \left(\frac{\sqrt{2} \alpha_{Q1}}{2} - \frac{\sqrt{2} \beta_{Q1}}{2}\right) + \beta_{Q2} \ket{1_{Q1}1_{Q2}} \left(\frac{\sqrt{2} \alpha_{Q1}}{2} + \frac{\sqrt{2} \beta_{Q1}}{2}\right)
$$
```assembly
3. M	Q1
```

$$
\left[\begin{matrix}0 & 0\\0 & 1\end{matrix}\right]
$$
$$
\ket{0_{Q1}} \sqrt{\frac{\alpha_{Q2}^{2} + \beta_{Q2}^{2}}{\alpha_{Q2}^{2}}} \left(\alpha_{Q2} \ket{0_{Q2}} \left(\frac{\sqrt{2} \alpha_{Q1}}{2} + \frac{\sqrt{2} \beta_{Q1}}{2}\right) + \alpha_{Q2} \ket{1_{Q2}} \left(\frac{\sqrt{2} \alpha_{Q1}}{2} - \frac{\sqrt{2} \beta_{Q1}}{2}\right)\right)
$$
```assembly
4. M	Q2
```

$$
\left[\begin{matrix}0 & 0\\0 & 1\end{matrix}\right]
$$
$$
\sqrt{2} \alpha_{Q2} \ket{0_{Q1}} \ket{1_{Q2}} \sqrt{\frac{\left(\alpha_{Q1}^{2} + \beta_{Q1}^{2}\right) \left(\alpha_{Q2}^{2} + \beta_{Q2}^{2}\right)}{\alpha_{Q2}^{2} \left(\alpha_{Q1} - \beta_{Q1}\right)^{2}}} \left(\frac{\sqrt{2} \alpha_{Q1}}{2} - \frac{\sqrt{2} \beta_{Q1}}{2}\right)
$$
**Final state** is: 
$$
\sqrt{2} \alpha_{Q2} \ket{0_{Q1}} \ket{1_{Q2}} \sqrt{\frac{\left(\alpha_{Q1}^{2} + \beta_{Q1}^{2}\right) \left(\alpha_{Q2}^{2} + \beta_{Q2}^{2}\right)}{\alpha_{Q2}^{2} \left(\alpha_{Q1} - \beta_{Q1}\right)^{2}}} \left(\frac{\sqrt{2} \alpha_{Q1}}{2} - \frac{\sqrt{2} \beta_{Q1}}{2}\right)
$$

