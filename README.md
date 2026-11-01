# AĞLA FENERBAHÇEM AĞLA

Output: **artifacts/video.mp4**

A 180-second silent, reference-based photographic animatic, with Turkish satirical intertitles, twelve 15-second chapters and 36 edited shots. The story follows renewed hope, transfers, disappointment, repeated management changes, the two choruses, and the final return of hope. Original reference photography, gentle camera pushes, rain graphics, navy/gold grading, authentic crest composites and fades are used throughout.

## Format and audio

- 1920 × 1080, 16:9, 24 fps; 4,320 video frames.
- H.264 / yuv420p, MP4 with fast-start metadata.
- AAC stereo, 48 kHz, digital silence. No Suno song or other audio was supplied or accessible in the task workspace. Silence is intentional, for subsequent song synchronization.
- Chapter/chorus placement follows the supplied storyboard, not an unheard recording.
- Actual encoding measurements and checks are in `production/verification.json`.

## Material limitations — this is an animatic

The available video tools expose ffmpeg editing/encoding and media probing, with **no generative-video model**. This deliverable therefore does **not** fulfill the requested photorealistic dramatic performance: it has no moving/crying supporters, crowd performances, player entrances, missed goals, coach/president changes, moving flags, actual transfer presentations, empty-stadium ending, or animated tear. These actions are represented in Turkish text, not falsely presented as generated footage. The one person pictured is the model in the supplied original merchandise photograph, not an identified player or a newly generated supporter.

The real stadium exterior photograph is reused, with photographic pan/zoom and grading rather than invented architecture. The night/rain look is a graphic treatment of the supplied daylight aerial, not newly filmed nighttime footage. The supplied stadium interior could not be loaded; no interior reference compliance is claimed. The original 780 × 470 exterior is enlarged for the 1080p canvas, so its detail is limited. Camera motion also moves the designed text/cards; it is a photographic editorial treatment, not independent character movement. The requested final isolated seated fan is not depicted.

## Reference access and use

All URLs below were attempted before the edit. The three successful images were downloaded and visually inspected at full available resolution using the image tool. Original bytes are in `references/`.

1. **Jersey — loaded, inspected, used.**
   https://0990b9.a-cdn.akinoncloud.com/products/2026/06/06/12839099/71065baf-6818-49a8-af93-23a3a007d74b.jpg
   The source model/jersey photo is composited without recreating its stripes, adidas mark, circular chest crest or white Otokoç panel. Only the connected white studio background was removed. The supplied image is treated as the requested 2026/27 design; the merchandise page could not independently verify the season.
2. **Original crest — loaded, inspected, used.**
   https://www.footylogos.com/dls/logo/rgba-v1/fenerbahce.png
   Original circular PNG is directly composited into graphic banners. Its typography, colors and 1907 date are retained; no substitute badge was drawn.
3. **Real stadium exterior — loaded, inspected, used.**
   https://i0.wp.com/fenerbahcefootball.com/wp-content/uploads/2024/01/saracoglu-headline.webp?resize=780%2C470&ssl=1
   Every stadium backdrop derives from this exact aerial, preserving its actual roof and surrounding Kadıköy streets.
4. **Stadium interior — unavailable, not used.**
   https://w0.peakpx.com/wallpaper/922/331/HD-wallpaper-fenerbahce-sukru-saracoglu-stadyumu-fenerbahce-sk-football-stadium-istanbul-turkey-football-fenerbahce-stadium.jpg
   Python and curl attempts failed with DNS/name resolution errors for w0.peakpx.com.
5. **Merchandise page — unavailable.**
   https://fenerium.com/fenerbahce-2026-27-cubuklu-forma-p-at013egp014sr
   Returned HTTP 403 Forbidden. The separately supplied jersey image was accessible.

No unrelated club imagery, invented badges, or invented stadium renderings were introduced. This is a satirical sequence rather than a factual report of any particular season's results or contracts. The 36-shot manifest is `production/storyboard.json`.

## Offline rebuild

Run `python3 production/render.py` from the repository. It uses the delivered card images and installed ffmpeg/libx264; no network, Python packages or fonts are needed to encode. Intermediate segments are created in a system temporary directory and cleaned automatically. The output is written to `artifacts/video.mp4`. `production/cards/` contains the final composited production assets, not scratch files.

## Source bundle repair

The 36 production JPEGs were recompressed at their original resolution to reduce the source bundle below 8 MiB. Original reference downloads and all production assets are retained. The existing MP4 is preserved byte for byte, avoiding another lossy video encode; an offline rebuild uses the smaller JPEGs and may differ slightly in compression detail. The delivered source files total approximately 6.4 MiB, excluding the separately uploaded MP4. The compressed cards were checked visually and the preserved MP4 was checked with `production/verify.py`.
