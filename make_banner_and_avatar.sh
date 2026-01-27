#!/bin/bash
# Generate Twitter assets from source images

cd "$(dirname "$0")"

# Twitter banner: 1500x500
# Scale banner.png 15x, crop centered
magick banner.png -filter point -resize 1500% -gravity center -crop 1500x500+0+0 +repage twitter_banner.png
echo "Created twitter_banner.png (1500x500)"

# Twitter avatar: 400x400
# Calculate minimum scale factor so both dimensions >= 400px
read width height <<< $(magick identify -format "%w %h" avatar.png)
scale_w=$(( (400 + width - 1) / width ))  # ceil(400/width)
scale_h=$(( (400 + height - 1) / height ))  # ceil(400/height)
scale=$(( scale_w > scale_h ? scale_w : scale_h ))  # max
percent=$(( scale * 100 ))

magick avatar.png -filter point -resize ${percent}% -gravity center -crop 400x400+0+0 +repage twitter_avatar.png
magick avatar.png -filter point -resize ${percent}% \
  -gravity center -crop 400x420+0+0 +repage \
  -gravity north -crop 400x400+0+0 +repage \
  twitter_avatar.png

echo "Created twitter_avatar.png (400x400) - scaled ${scale}x"
