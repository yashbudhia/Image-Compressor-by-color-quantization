# Image-Compressor-by-color-quantization
Reduce the number of colors in an image to simplify it (similar to a posterize effect) and reduce file size. Experiment with clustering algorithms like K-means to limit colors to a specified number.  

# Tools
OpenCV and scikit-learn for color clustering. 

#Observations 

- (when k = 8)

- Initial image
  
  ![knight_flowers_pink](https://github.com/user-attachments/assets/94f7f75a-a3ba-4218-953b-0db17df604f4)

  - size = 196.5 KiB
  - Lots of colors are present
 
- After compression
  
![quantized_image](https://github.com/user-attachments/assets/85b709ba-0c80-4f0d-a947-3d5102ffff15)

 - size = 322 KiB
 - Colors like green and yellow got replaced by nearest colors (pink) But somehow image size has been increased

  

