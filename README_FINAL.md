# Bikou OS (微光 / びこう)

Bikou OS is a privacy-focused fork of Deepin Linux, rebranded as "Bikou" (微光 - faint light/glimmer in Chinese, びこう in Japanese).

## What We've Done

### Rebranding
- Updated lsb-release.in to Bikou OS
- Renamed Deepin.info → Bikou.info with new repo URLs
- Updated GTK theme metadata
- Rebranded .desktop files (Name/Comment)
- Updated deepin-desktop-schemas branding strings

### Privacy Hardening
- Disabled recent files history by default (remember-recent-files=false, max-age=0)
- Disabled software usage stats reporting by default
- Strengthened privacy schema defaults
- Identified cloud/sync components (Deepin ID) for further review

### Workspace Structure
- /home/tinkerspace/bikou-workspace/src/ - Modified source trees (core DDE components)
- /home/tinkerspace/bikou-workspace/rebrand-scripts/ - Rebranding utilities
- Documentation: BRANDING.md, PRIVACY.md, BUILD_GUIDE.md, STATUS.md

## Project Scope
The goal: take Deepin OS, add more privacy, rebrand to Bikou (微光/びこう). This is the foundation work.

## Next Steps (To Complete Fully)
1. Create proper logo assets (微光 concept - faint glimmer of light)
2. Review and disable telemetry in dde-daemon more thoroughly
3. Consider hiding/removing Deepin ID/cloud sync UI if desired
4. Build packages or create a custom ISO build pipeline
5. Test the modified components

The core modifications are in place. The branding looks clean and privacy defaults are improved.
