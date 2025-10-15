'''
"Design and Implement a Decoder Class for Multi-Way Tree-Based Encoding" The class should include an __init__ method
that initializes the decoder with the root of a multi-way tree. The root consists of 26 alphabetic nodes (A–Z),
while all other nodes are represented as *. Each non-root node maintains a list of child nodes indexed from 0, 1, 2, ….
Starting from the root, each alphabetic node is assigned a unique numeric code (e.g., a → 123).

The decode method should map an input sequence of indices (e.g., 01)
into the corresponding character sequence (e.g., abc).

root (*)
 ├── child(0) → *
 │     ├── child(0) → 'a'
 │     └── child(1) → 'b'
 └── child(1) → *
       ├── child(0) → 'c'
       └── child(1) → 'd'

00	root → child(0) → child(0) → 'a'	"a"
01	root → child(0) → child(1) → 'b'	"b"
10	root → child(1) → child(0) → 'c'	"c"
11	root → child(1) → child(1) → 'd'	"d"

'''