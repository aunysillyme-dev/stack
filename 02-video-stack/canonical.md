# Video stack: core tools and workflows

Curated by @aunysillyme · Reviewed 2026-11-18

Source: https://aunysillyme.dev/stack/video/

## Core tools (13)

- **[ChatGPT Images](https://chatgpt.com/):** GPT Image for detailed scenes, character reference sheets, infographics and thumbnails.
- **[Grok Imagine](https://grok.com/imagine):** Cinematic and surreal images, character visuals, storyboards and short animated clips.
- **[Adobe Firefly](https://firefly.adobe.com/):** An image and video studio where I generate, edit and animate. My preferred documented music-video route uses Google Veo 3.1 Fast in Firefly.
- **[Google Flow](https://flow.google.com/):** Another workspace for Google video models. I have tested it for music-video shots.
- **[Fuser](https://app.fuser.studio/):** A node-based creative canvas. I have experimented with image nodes and a Kling node for character animation.
- **[Midjourney](https://www.midjourney.com/):** Image creation and visual exploration. An archive of earlier work is useful for studying palette, light, texture and composition.
- **[CapCut / Firefly editor](https://www.capcut.com/):** Arrange the selected clips, add the finished audio, trim and export.
- **[HyperFrames](https://github.com/heygen-com/hyperframes):** My default programmatic video toolkit for building editable scenes, motion graphics, explainers and videos from HTML, assets and a timeline.
- **[Tesseract](https://github.com/mirage-hq/Tesseract):** An agent-assisted editing toolkit for cuts, editable motion graphics, 3D and shot-by-shot color work. It builds an editable .tsrct project; it is not an image-to-video generator.
- **[Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan):** Open-source image upscaling. I have used it to enlarge selected album art before preparing the final dimensions.
- **[FFmpeg](https://ffmpeg.org/):** Open-source media toolkit for assembling, scaling, color adjustment, encoding and checking the finished file.
- **[ElevenLabs](https://elevenlabs.io/):** Voiceover, transcription and sound effects when a project calls for them. The workspace also exposes creative image and video routes.
- **[Remotion](https://www.remotion.dev/):** Reference material for animation techniques and templates that can be rebuilt in HyperFrames; check the applicable license before reuse.

## Workflows (5)

### Video production from brief to delivery

Source: https://aunysillyme.dev/stack/video/#pipeline

1. Start with the idea and purpose. Write what the video is about, who it is for, what the viewer should understand or feel, and where it will be watched. Decide the format, approximate duration, aspect ratio, deadline and available budget.
2. Collect the inputs. Gather the song or script, source footage, approved reference images, character details, brand assets and any examples. Keep the original files. For an explainer, verify claims and collect the real screen captures or demonstrations.
3. Develop the concept. Choose the story, visual world, emotional direction, color palette, typography and camera language. Decide what should be literal, symbolic or shown with graphics. Create a short brief a collaborator or agent can follow.
4. Write and time the structure. Make a scene-by-scene storyboard with the message or lyric, visual, action, sound and estimated time. For music, map the actual vocal phrases and musical changes; listen to verify automated timing. For explainers, structure a hook, explanation, demonstration and close.
5. Produce the ingredients. Generate or gather stills, characters, B-roll, screenshots, footage, narration, music and sound effects. Make character reference sheets where useful. Label each asset by scene and keep the prompt, model and reference together.
6. Test a small sample. Finish one representative still and one short motion test. Check the composition, character, real movement, aspect ratio and estimated cost before generating a batch. Regenerate or change tools when the result misses.
7. Make the clips and graphics. Animate selected stills with any suitable image-to-video model. For diagrams, titles, screenshots or real footage, use editable motion graphics or an editor instead. Choose the model based on the shot, available controls, quality and cost.
8. Build the edit. Place shots on a timeline, match them to the music or narration, and trim for pacing. In HyperFrames, build editable scenes and transitions; in Tesseract, cut footage and add editable layers; Firefly or CapCut can also handle an edit. Avoid a generic effect on every cut.
9. Finish picture and sound. Correct white balance, unwanted color casts, contrast and shot-to-shot consistency while preserving intentional light and natural skin. Upscale only when needed. Mix dialogue, music and effects so the important sound stays clear.
10. Review, revise and deliver. Watch and listen through the export. Check timing, character and anatomy, motion, text legibility, captions if requested, color, audio sync, duration and dimensions. Revise weak shots, make the needed orientation versions and thumbnail, and save the editable project, assets and final exports.

### Create a still image

Source: https://aunysillyme.dev/stack/video/#image

1. Define the idea. What are you making, for whom, and what should the viewer see or understand? Note the story or message and the feeling it should carry.
2. Build the visual direction. Choose a subject, setting, palette, lighting, composition and texture that support that feeling.
3. Set the shape. Choose square for cover art, landscape for a video frame or thumbnail, or portrait for a vertical post.
4. Generate and refine. Make a few options. Check the face, hands, objects, color and composition; edit or regenerate what does not fit.
5. Keep your ingredients. Save the final image, prompt, references and settings together so you can return to the look.

### Keep a character consistent

Source: https://aunysillyme.dev/stack/video/#character

1. Create a reference sheet. In GPT Image, describe the character’s defining features, wardrobe, personality and world. Ask for front, side, three-quarter and back views, plus expressions and poses.
2. Choose a clean reference. Check that the views look like the same character. If the sheet is busy, save a clear individual image too.
3. Make and animate a scene. Use the reference to create a scene still, then upload that still to an image-to-video tool such as Grok Imagine, Veo through Firefly or Flow, Kling in Fuser, or another suitable model. Describe the action and camera movement.
4. Review the whole shot. Watch for changes to the face, clothes and anatomy. Keep the original reference and repeat the key details when generating another shot.

### Animate stills to a finished song

Source: https://aunysillyme.dev/stack/video/#music

1. Plan to the track. Listen to the finished song, identify its sections and make a shot list tied to the story, lyrics and musical changes.
2. Generate fresh stills. Mix character shots with environments and details. Keep identity, wardrobe, palette and story consistent.
3. Compose for the format. Make separate landscape and portrait visuals when both are needed. For one Flatline production run, I used 15 stills per orientation. Choose the amount your story and edit need.
4. Animate each still. In Firefly, choose an available image-to-video model, upload the matching still and describe plausible subject and environmental movement. I prefer Veo 3.1 Fast for this route.
5. Inspect and select. Check multiple moments for actual motion, facial drift, distorted hands, flicker and unwanted changes. Regenerate weak clips.
6. Edit to the music. Arrange and trim the clips to the track and lyrics. Vary shot types, use the mastered audio and check sync, color, playback and dimensions before export.

### Build a lyric-led storyboard

Source: https://aunysillyme.dev/stack/video/#storyboard

1. Share the brief. Provide the title, genre, mood, palette, album art and lyrics. Ask for an image for each lyric line.
2. Fill the gaps. Ask for additional images in the same style, without text, for intros, instrumental sections and outros.
3. Animate the selections. Generate clips from the images. Specify subject or environmental motion when the result needs more direction.
4. Cut to the actual track. Export to CapCut, arrange the clips in order and trim them to the lyrics and music. For strict continuity, use the character-reference workflow and review each shot closely.
