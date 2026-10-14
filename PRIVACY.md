# Bikou OS Privacy Plan

Goals:
1. Remove/minimize telemetry, analytics, data reporting
2. Remove or disable Deepin cloud services (if present)
3. No automatic data upload without explicit user consent
4. Strip China-specific tracking/privacy concerns while preserving functionality
5. Keep local-first design

Areas to investigate:
- dde-daemon: check for telemetry, crash reporting, usage stats
- dde-control-center: sync/cloud settings, accounts
- startdde: session services, auto-reporting
- deepin-desktop-schemas: default settings (privacy related gsettings)
- deepin-system-settings, dde-api, various services

Rebrand: Bikou (微光 / びこう) - "Glimmer/Faint Light"
