import numpy as np

import matplotlib.pyplot as plt

a = np.arange(12).reshape(3,4)

b = a > 4

print(b)

print(a[b])

a[b] = 0
print(a)

def mandelbrot(h,w,maxit=20):
    #Returns image of the Mandelbrot fractal of size(h,w)
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime==maxit)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime

plt.imshow((mandelbrot(400,400)))
plt.show()

a = np.array([2,3,4,5])
b = np.array([8,5,4])
c = np.array([5,4,6,8,3])
ax,bx,cx = np.ix_(a,b,c)

print(ax)

print(bx)

print(cx)

print(ax.shape,bx.shape,cx.shape)

result = ax+bx*cx

print(result)

print(result[3,2,4])
print(a[3]+b[2]*c[4])

