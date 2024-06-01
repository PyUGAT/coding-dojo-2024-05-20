#  Langton's Ant ⬜🐜⬛

https://en.wikipedia.org/wiki/Langton%27s_ant

## Rules

Squares on a plane are colored variously either black or white. We arbitrarily
identify one square as the "ant". The ant can travel in any of the four
cardinal directions at each step it takes. The "ant" moves according to the
rules below:

* At a white square, turn 90° clockwise, flip the color of the square,
  move forward one unit
* At a black square, turn 90° counter-clockwise, flip the color of the square,
  move forward one unit

## Run test

```console
pytest
ptw .  # to run via file watcher
```
