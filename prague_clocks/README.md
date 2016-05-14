# Motivation
A Prague Clock defines a pattern (or rhythm) of breaks by which to chime the hour such that large numbers like 16 and 17 are easily distinguished.


Excerpted from the paper cited as python dict at top of source code (`./prague_clocks.py`).

# Theorem 1
_For every natural number m there exists a unique intact Prague Clock with modulus m._

## Construction 
### (with step labels added)

In conclusion, we can obtain the unique intact Prague Clock of modulus _m_ by 

(1) reducing the first _m_ triangular numbers, 0,1,3,...,1/2 _m_ (_m_ - 1) (mod _m_), 
adjoining _m_ itself, 

(2) and then sorting and taking their differences as the period sequence.

# Theorem 4
_An intact Prague Clock is primitive if and only if its modulus is odd._
