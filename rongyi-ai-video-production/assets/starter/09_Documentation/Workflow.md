# Production Workflow

## Content preparation

1. Create a stable production ID.
2. Develop the idea, research, draft, and scene plan in `01_Content/Creative_Script_Lab/<production-id>/`.
3. Review the content and deliberately promote the approved words to `01_Content/Scripts/<production-id>/script.md`.
4. Record visual treatment, presenter behavior, and observable acceptance criteria in the matching Creative Brief.
5. Create and validate `06_Automation/Jobs/<production-id>/job.json` before any external generation or rendering.

## Human presenter

Camera recording -> green-screen source -> FFmpeg inspection and chroma key -> normalized presenter.

## AI digital twin

Approved Script -> provider generation -> acquired source -> provider-independent normalization -> normalized presenter.

## Shared post-production

Normalized presenter -> Remotion brand composition -> FFmpeg delivery conformance -> technical QA -> human creative review when required -> final output.

If a requirement depends on a real physical action, such as holding a marker and writing on glass, capture or generate that action in the presenter source. A post-production handwriting animation is not an equivalent substitute.
