# Recurrent-Square-Filling-Curves
Recurrent functions which use the Hilbert, Peano and Z curves to fill squares of many $2^m x 2^m$ dimensionalities. Those funtions do mainly output a 2D map of the output curve. It is meant to be a more efficient symmetric mapping of 2D images into 1D lin spaces. *1

## Content
In this repo are two recursive funtions:

### Recursive Hilbert-Peano Function
 
it can break down from any dxd square which is not a multiple of a prime number
it has an asymetric 3x3 base in case of a hulbert structure before.

### Recursive Peano-Hilbert Function
 
it can break down from any d*d square which is not a multiple of a prime number
it has a reverse z-curve for any 2^m * 2^m blocks inside 3^n * 3^n blocks.
 
This is the Peano-Hilbert version of the Hilbert-Peano function I have imple-
mented before. 
 
Here, we are using a symetric z-base when breaking from a peano curve. 
Now, we have a completely centered solution for square 2D space filling curves.

Although, 3D versions. form other authors, using convenient bit representations
do exist.

## Map Examples


## Notes
*1: WARNING: This type of mappings is rare for deep learning image recognition tasks and does probably not work on pretrained networks, since they are most of the time either convolutional and/or in some kind of sense trained on a simple stack reshape of the input images.