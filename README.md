# Clover Branding

Brand assets for the Clover app.

## Icons

Pixel art icons located in `icons/`.

### Icon List

account, clover, developer, edit, heart, heart-outline, hide, home, mailbox, messages, moon, notifications, profile, question, report, search, settings, signout, star, star-alt1, star-alt2, sun, sun-alt1, sun-alt2, visitors

### Sizes

All icons are available in three sizes:
- **1x**: 12x12 pixels (base size)
- **@2x**: 24x24 pixels
- **@3x**: 36x36 pixels

### Naming Convention

`{name}.png` (1x), `{name}@2x.png`, `{name}@3x.png`

### Pixel-Perfect Rendering

For pixel art to render crisp without blur, display at true pixel size:
- 1x icons (12px) → 12x12 points
- 2x icons (24px) → 24x24 points
- 3x icons (36px) → 36x36 points

## Using Icons in React Native / Expo

### Two Approaches

**Approach 1: Explicit Resolution (current, web-focused)**

Copy icons to app with `-2x` naming (Metro can't handle `@` in explicit paths):
```
icons/search@2x.png  →  clover-app/assets/icons/search-2x.png
```

Import explicitly:
```tsx
require('../assets/icons/search-2x.png')
// Display at 24x24 points for pixel-perfect rendering
style={{ width: 24, height: 24 }}
```

**Approach 2: Auto Resolution (recommended for mobile)**

Copy icons with `@2x`/`@3x` naming intact. Import only the base filename:
```tsx
require('../assets/icons/search.png')
```

React Native automatically picks the right resolution based on device pixel density:
- 2x devices → search@2x.png
- 3x devices → search@3x.png

For this to work, all variants must be in the same directory with standard `@2x`/`@3x` suffixes.

### Which Approach to Use?

| Platform | Recommendation |
|----------|----------------|
| Web | Approach 1 - explicit `-2x` files at exact size (24x24 pts) |
| Mobile | Approach 2 - auto resolution, scaling is fine |

**Why the difference?**

Web displays are typically 2x density. Pixel art must be sized exactly right (2x icons at 24x24 points) or it looks blurry. We control this with explicit file references and exact dimensions.

Mobile displays are so high density (3x+) that slight scaling artifacts are invisible. Let React Native handle resolution picking - it's simpler and works fine.

### Dynamic Tinting

Instead of separate light/dark icon files, use `tintColor` to colorize dynamically:

```tsx
<Image
  source={require('../assets/icons/search-2x.png')}
  style={{ width: 24, height: 24, tintColor: textColor }}
/>
```

Works because icons are monochrome on transparent backgrounds. One file, any color.

## Other Assets

- `logo.png` / `logo_dark.png` - App logo
- `logomark.png` / `logomark_dark.png` - Icon-only mark
- `wordmark.png` - Text-only logo
- `favicon.png` - Browser favicon
- `banner.png` - Marketing banner
- `twitter_avatar.png` / `twitter_banner.png` - Social assets
