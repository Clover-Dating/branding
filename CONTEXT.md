# Context for Next Session

## Current Task
Creating dark mode icon variants and integrating icons into the Clover app.

## What We Were Doing
1. **Create dark mode (inverted) icons** - Need to color-invert all icons in `branding/icons/pngs/` and name them with `-dark` suffix (e.g., `sun.png` → `sun-dark.png`, `sun@2x.png` → `sun-dark@2x.png`)

2. **Add theme toggle icons to app** - Use `sun@2x.png` for light mode button and `moon-dark@2x.png` (inverted moon) for dark mode button in the Sidebar theme toggle

## Icons Status
- Location: `branding/icons/pngs/`
- Naming: kebab-case, no prefix (e.g., `account.png`, `heart-outline.png`)
- Variants: 1x (12x12), @2x (24x24), @3x (36x36) all created
- 25 icons total, 75 files (before dark variants)

## Icon List
account, clover, developer, edit, heart, heart-outline, hide, home, mailbox, messages, moon, notifications, profile, question, report, search, settings, signout, star, star-alt1, star-alt2, sun, sun-alt1, sun-alt2, visitors

## Command to Create Dark Variants
```bash
cd /Users/gar/Desktop/okgar/branding/icons/pngs
for f in *.png; do
  [[ "$f" == *-dark* ]] && continue
  if [[ "$f" == *@* ]]; then
    base="${f%@*}"
    suffix="@${f#*@}"
  else
    base="${f%.png}"
    suffix=".png"
  fi
  magick "$f" -channel RGB -negate "${base}-dark${suffix}"
done
```

## App Integration Notes
- Sidebar is at `clover-app/src/components/layout/Sidebar.tsx`
- Currently uses Material icons for theme toggle
- Replace with custom pixel art icons (sun/moon)
- Icons need to be copied to `clover-app/assets/`

## Other Notes
- Git repo is inside `/clover-app/`, not the parent okgar directory
- Using PNGs (not SVGs) for pixel art - better compression, native RN support
- SVGs kept in `branding/icons/svgs/` as archival source files
