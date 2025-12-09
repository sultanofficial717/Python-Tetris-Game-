# Assets Directory

This directory is reserved for game assets such as:

## Planned Assets

### Images
- `logo.png` - Game logo
- `icon.png` - Window icon
- `background.png` - Menu background
- `tiles/` - Custom block sprites

### Sounds (Future Enhancement)
- `music/`
  - `theme.mp3` - Main game theme
  - `menu.mp3` - Menu music
- `sfx/`
  - `rotate.wav` - Piece rotation sound
  - `move.wav` - Piece movement sound
  - `drop.wav` - Hard drop sound
  - `clear.wav` - Line clear sound
  - `tetris.wav` - Four lines cleared sound
  - `gameover.wav` - Game over sound

### Fonts (Future Enhancement)
- `fonts/`
  - `game_font.ttf` - Custom game font
  - `score_font.ttf` - Score display font

## Adding Assets

To add assets to the game:

1. Place files in appropriate subdirectories
2. Update the asset loading code in `src/config.py`
3. Use relative paths for portability

Example:
```python
# In config.py
ASSET_DIR = Path(__file__).parent.parent / "assets"
SOUND_DIR = ASSET_DIR / "sounds"

# Load sound
drop_sound = pygame.mixer.Sound(SOUND_DIR / "drop.wav")
```

## Asset Guidelines

### Images
- Format: PNG with transparency
- Size: Optimized for web/distribution
- License: Ensure proper licensing

### Sounds
- Format: WAV for SFX, MP3/OGG for music
- Quality: 44.1kHz, 16-bit minimum
- Volume: Normalized to -3dB

### Fonts
- Format: TTF or OTF
- License: Must allow distribution
- Style: Readable at small sizes

## Free Asset Resources

### Graphics
- [OpenGameArt.org](https://opengameart.org/)
- [Kenney.nl](https://kenney.nl/)
- [itch.io](https://itch.io/game-assets/free)

### Sounds
- [freesound.org](https://freesound.org/)
- [OpenGameArt.org - Audio](https://opengameart.org/art-search-advanced?keys=&field_art_type_tid%5B%5D=13)
- [Zapsplat](https://www.zapsplat.com/)

### Fonts
- [Google Fonts](https://fonts.google.com/)
- [DaFont](https://www.dafont.com/)
- [1001 Fonts](https://www.1001fonts.com/)

## Attribution

If you use third-party assets, please add attribution here:

```
- Asset Name: [Name]
  Author: [Author]
  License: [License]
  Source: [URL]
```

## Contributing Assets

When contributing assets:
1. Ensure you have rights to distribute
2. Include license information
3. Optimize file size
4. Update this README
