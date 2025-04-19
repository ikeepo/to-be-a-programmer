# ASCII bytes
`as_types` returns a slice of bytes `&[u8]` representing the string's UTF-8 encoded data.
Rust string must be valid UTF-8, but not ASCII.

## ASCII vs UTF-8
American Standard Code for Information Interchange, a 7-bit encoding standard.

UTF-8, a variable-length Unicode Encoding, backward-compatible with ASCII.
SUpport over 1million Unicode charactors, including (latin, Chineses, etc.).
use 1-4 bytes, 1 for ASCII, 2-4 for others.
Unicode is over 1.4 million code points, not for encoding.
