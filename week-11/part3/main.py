import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """
    Calculate the number of iterations for the Mandelbrot set.
    
    Parameters:
    - c: Complex number to test.
    - max_iter: Maximum iterations before deciding if the number escapes.
    
    Returns:
    - Iteration count before escape or max_iter if not escaping.
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    return n

def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    """
    Generate the Mandelbrot set for a specified range and resolution.
    
    Parameters:
    - width, height: Resolution of the output image.
    - x_min, x_max, y_min, y_max: Bounds of the complex plane.
    - max_iter: Maximum number of iterations.
    
    Returns:
    - A 2D array with iteration counts for each point.
    """
    real = np.linspace(x_min, x_max, width)
    print(real,'react')
    imag = np.linspace(y_min, y_max, height)
    print(imag,'imag')
    mandelbrot_image = np.empty((height, width))
    
    for i in range(height):
        for j in range(width):
            c = complex(real[j], imag[i])
            mandelbrot_image[i, j] = mandelbrot(c, max_iter)
    return mandelbrot_image

# Parameters
width, height = 800, 800
x_min, x_max = 0.35,0.375
y_min, y_max = 0.325,0.375
max_iter = 100

# Generate the Mandelbrot set
mandelbrot_image = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)


# Plot the Mandelbrot set
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_image, extent=[x_min, x_max, y_min, y_max], cmap='hot')
plt.colorbar(label='Iterations to Escape')
plt.title('Mandelbrot Set')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()