import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Load the image
image = cv2.imread('input.jpg')  # Replace with your image path
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB

# Step 2: Preprocess the image for clustering
pixel_values = image.reshape((-1, 3))  # Flatten the 2D image into a 1D array of RGB pixels
pixel_values = np.float32(pixel_values)  # Convert to float32 for KMeans

# Step 3: Apply K-Means clustering
K = 8  # Number of colors you want in the output image
kmeans = KMeans(n_clusters=K, random_state=42)
kmeans.fit(pixel_values)

# Step 4: Replace each pixel color with the nearest cluster centroid
centers = np.uint8(kmeans.cluster_centers_)  # Convert centroids back to 8-bit RGB
labels = kmeans.labels_  # Labels for each pixel
quantized_image = centers[labels.flatten()]  # Replace pixel colors with centroid colors
quantized_image = quantized_image.reshape(image.shape)  # Reshape to original image shape

# Step 5: Display and save the quantized image
plt.imshow(quantized_image)
plt.axis('off')
plt.show()

# Optional: Save the quantized image
cv2.imwrite('quantized_image.jpg', cv2.cvtColor(quantized_image, cv2.COLOR_RGB2BGR))
