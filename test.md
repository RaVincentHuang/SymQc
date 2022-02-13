# The ans of test.qcis

**Init state** is: 
$$
\left[\begin{matrix}a_{0} & a_{1} & a_{2} & a_{3}\end{matrix}\right]
$$

```assembly
1. H	q0
```

$$
\left[\begin{matrix}\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2}\\\frac{\sqrt{2}}{2} & - \frac{\sqrt{2}}{2}\end{matrix}\right]
$$
$$
\left[\begin{matrix}\frac{\sqrt{2} a_{0}}{2} + \frac{\sqrt{2} a_{1}}{2} & \frac{\sqrt{2} a_{0}}{2} - \frac{\sqrt{2} a_{1}}{2} & \frac{\sqrt{2} a_{2}}{2} + \frac{\sqrt{2} a_{3}}{2} & \frac{\sqrt{2} a_{2}}{2} - \frac{\sqrt{2} a_{3}}{2}\end{matrix}\right]
$$
```assembly
3. H	q1
```

$$
\left[\begin{matrix}\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2}\\\frac{\sqrt{2}}{2} & - \frac{\sqrt{2}}{2}\end{matrix}\right]
$$
$$
\left[\begin{matrix}\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} + \frac{\sqrt{2} a_{1}}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} + \frac{\sqrt{2} a_{3}}{2}\right)}{2} & \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} - \frac{\sqrt{2} a_{1}}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} - \frac{\sqrt{2} a_{3}}{2}\right)}{2} & \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} + \frac{\sqrt{2} a_{1}}{2}\right)}{2} - \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} + \frac{\sqrt{2} a_{3}}{2}\right)}{2} & - \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} - \frac{\sqrt{2} a_{1}}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} - \frac{\sqrt{2} a_{3}}{2}\right)}{2}\end{matrix}\right]
$$
```assembly
5. H	q1
```

$$
\left[\begin{matrix}\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2}\\\frac{\sqrt{2}}{2} & - \frac{\sqrt{2}}{2}\end{matrix}\right]
$$
$$
\left[\begin{matrix}\frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} + \frac{\sqrt{2} a_{1}}{2}\right)}{2} - \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} + \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} + \frac{\sqrt{2} a_{1}}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} + \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} & \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} - \frac{\sqrt{2} a_{1}}{2}\right)}{2} - \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} - \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} - \frac{\sqrt{2} a_{1}}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} - \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} & - \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} + \frac{\sqrt{2} a_{1}}{2}\right)}{2} - \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} + \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} + \frac{\sqrt{2} a_{1}}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} + \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} & - \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} - \frac{\sqrt{2} a_{1}}{2}\right)}{2} - \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} - \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} - \frac{\sqrt{2} a_{1}}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} - \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2}\end{matrix}\right]
$$
**Final state** is: 
$$
\left[\begin{matrix}\frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} + \frac{\sqrt{2} a_{1}}{2}\right)}{2} - \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} + \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} + \frac{\sqrt{2} a_{1}}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} + \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} & \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} - \frac{\sqrt{2} a_{1}}{2}\right)}{2} - \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} - \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} - \frac{\sqrt{2} a_{1}}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} - \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} & - \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} + \frac{\sqrt{2} a_{1}}{2}\right)}{2} - \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} + \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} + \frac{\sqrt{2} a_{1}}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} + \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} & - \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} - \frac{\sqrt{2} a_{1}}{2}\right)}{2} - \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} - \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} \left(\frac{\sqrt{2} a_{0}}{2} - \frac{\sqrt{2} a_{1}}{2}\right)}{2} + \frac{\sqrt{2} \left(\frac{\sqrt{2} a_{2}}{2} - \frac{\sqrt{2} a_{3}}{2}\right)}{2}\right)}{2}\end{matrix}\right]
$$

