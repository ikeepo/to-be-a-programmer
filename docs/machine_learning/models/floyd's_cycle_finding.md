# [Floyd's Cycle-Finding Algorithm]()
> [1](https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/) [2](https://medium.com/@zephyr.ventum/floyds-tortoise-and-hare-cycle-finding-algorithm-my-over-explanation-5631c5ce71d7)
Hare-Tortoise algorithm.
The Key is the *relative speed* and the *circular nature* of a cycle.
Because the faster is relatively faster one step, which means it catch up one step by one iteration, so it must can catch up the slow one.
Step ahead 3 or 4 still work, modulo gives the remainder after dividing one number by another.
A modulo is a way to "loop back" to the start of the cycle, it's like a clock.

## the relative speed ensures the fast pointer's position modulo eventually matches the slow pointer's position.
Two item meet when their positions modulo are equal.
`t`: slow steps, `t` round,
`kt`: fast steps

slow step 1, fast step k, relative speed k-1, after t round, it's `(k-1) t`
$t mod C = kt mod C$ means $(k-1)t = m C$
if `gcd(k-1,C)=1` `(k-1)t` hit most C iterations, otherwise it would miss some , but still hit `mC`;

Two points:
- fast pointer gain positive slow one
- C is finit
so, it must can gain a C multiple after some round.

Another key point is modulo.
