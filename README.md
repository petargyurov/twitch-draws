# Chat Makes Art

### 🔴 Go to [ChatMakesArt](https://www.twitch.tv/chatmakesart) on Twitch to play!


ChatMakesArt is an interactive experiment where users can create collaborative
art. Users can color pixels on a N-by-N grid, (usually 1000x1000), by specifying
coordinates and a color.

## How It Works
1. Go to the Twitch channel and follow
2. To draw on the grid, use the command `!draw X Y C` where:
```
X = x-axis coordinate
Y = y-axis coordinate
C = color
```

Example: `!draw 500 600 #6441A5`

### Valid Colors
You can specify any valid hex color code (e.g.: `#6441A5`) or a simple 
color name (e.g.: `red`). For a full spec of the simple color names, see [here](http://www.science.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png).

### Rules
1. Commands not preceded by `!` are ignored
2. Commands with invalid arguments are ignored
3. Coordinates are clamped to the grid's max and min values; i.e.: you cannot draw outside the grid
4. Coordinates are clamped to each "pixel". For example, the giving the command 
`!draw 123 456 red` on an `1000x1000` grid will color the pixel at `(120, 450)`. 


### Future Goals
- give user more ways to draw (paths, shapes, brushes, etc.)
    - integrate with Twitch "points"?
- track drawing stats per user
- different modes
    - team modes ("red" vs "blue")
- Chat Makes Music