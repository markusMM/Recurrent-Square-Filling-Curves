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

### 12x12 Map


#### Peano-hilbert
```python
[[106 107 110 108 112 114 116 117 138 139 142 140]
 [104 105 111 109 113 115 118 119 136 137 143 141]
 [ 97  99 102 103 120 121 127 125 129 131 134 135]
 [ 96  98 100 101 122 123 126 124 128 130 132 133]
 [ 92  94  91  90  69  68  66  64  60  62  59  58]
 [ 93  95  89  88  71  70  67  65  61  63  57  56]
 [ 87  86  83  81  77  79  73  72  55  54  51  49]
 [ 85  84  82  80  76  78  75  74  53  52  50  48]
 [ 10  11  14  12  16  18  20  21  42  43  46  44]
 [  8   9  15  13  17  19  22  23  40  41  47  45]
 [  1   3   6   7  24  25  31  29  33  35  38  39]
 [  0   2   4   5  26  27  30  28  32  34  36  37]]
```

![alt text](https://github.com/markusMM/Recurrent-Square-Filling-Curves/raw/master/plot/12x12_PeanoHilbert.png "12x12 Peano-Hilbert")


#### Hilbert-Peano
```python
[[ 47  48  49  58  59  60  83  84  85  94  95  96]
 [ 46  51  50  57  56  61  82  87  86  93  92  97]
 [ 45  52  53  54  55  62  81  88  89  90  91  98]
 [ 44  43  42  65  64  63  80  79  78 101 100  99]
 [ 37  38  41  66  69  70  73  74  77 102 105 106]
 [ 36  39  40  67  68  71  72  75  76 103 104 107]
 [ 35  34  27  26  25  24 119 118 117 116 109 108]
 [ 32  33  28  19  20  23 120 123 124 115 110 111]
 [ 31  30  29  18  21  22 121 122 125 114 113 112]
 [  4   5   6  17  14  13 130 129 126 137 138 139]
 [  3   2   7  16  15  12 131 128 127 136 141 140]
 [  0   1   8   9  10  11 132 133 134 135 142 143]]
```

![alt text](https://github.com/markusMM/Recurrent-Square-Filling-Curves/raw/master/plot/12x12_HilbertPeano.png "12x12 Hilbert-Peano")


## Notes
*1: WARNING: This type of mappings is rare for deep learning image recognition tasks and does probably not work on pretrained networks, since they are most of the time either convolutional and/or in some kind of sense trained on a simple stack reshape of the input images.