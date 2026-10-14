# Next Steps for Bikou OS

## Completed
- Core rebranding (Bikou/微光 branding, logos created)
- Privacy hardening (recent files disabled, telemetry settings)
- Repo pushed to GitHub: https://github.com/Aghosh-mv/BikouOS
- Logo assets integrated into deepin-desktop-base

## To Build & Test
1. Build packages - need build environment (pbuilder/debuild or native build)
2. Create rootfs/image - can adapt KorrinOS build scripts or use live-build
3. Test in VM - verify branding, privacy settings work, boots cleanly
4. Strip remaining Deepin references where they affect UX (polkit/dbus names - be careful to not break API)

## Privacy Focus (as requested)
- Remove Chinese privacy concerns while keeping full Deepin experience
- More privacy added: no recent file tracking, hardened defaults
