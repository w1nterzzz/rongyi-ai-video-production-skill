# Setup

## Initialization state

{{INITIALIZATION_STATE}}

The starter itself includes no video-generation code, Remotion components, third-party APIs, credentials, personal likeness data, or unnecessary dependencies.

## Before Phase 1 implementation

1. Confirm Git is initialized and review `.gitignore` before adding media.
2. Install an active Node.js LTS release and FFmpeg on the development machine.
3. Add Remotion only when beginning the Phase 1 implementation; lock dependency versions.
4. Keep credentials in local environment variables and provide only a redacted `.env.example` if configuration documentation is needed.
5. Use small, rights-cleared test media for the first end-to-end validation.

## First verification target

Build one minimal vertical-video job using human-recorded footage. Prove FFmpeg normalization, Remotion composition, final MP4 delivery, and a repeatable render command before adding subtitles or any avatar provider.
