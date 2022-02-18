# cse210-04

IMPORTANT:
    Need help figuring out why one of each gem and rock moves with player icon, why score board doesn't stay updated, and also need polishing to complete gameplay (debugging).

Classes are marked with a *.

Data:
    score.txt - just has a file with rock and gem points values

Directing:
    *Director

Casting:
    *cast
    *Actors - Parent
        *rock class - similar to Artifacts in example assignment - Child of Actor
        *gem class - similar to Artifacts in example assignment - Child of Actor
        Score - set in Main

Services:
    *KeyboardService - same as a Player
    *VideoService

Shared:
    *Color
    *Point
