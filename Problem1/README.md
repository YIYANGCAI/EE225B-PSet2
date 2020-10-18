# Berkeley Photo's light adjustment
The code is written in matlab because it is simpler when considering matrix calculations

# Algorithms
I have read different papers studying the light-inbalanced image processing. Briefly speaking, I use an esembled algorithm. I processed the gray image for three times, using three types of different algorithms, and then merge three outputs into one, using a weight calculation algorithm.

# Use
Run the main.m in matlab and then program will display the original and processed images
processed images will also be saved in the same direction.

# Advantages
My algorithm only process the area where the light is dim, it has slight influence on the normal area.