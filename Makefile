.PHONY: help rebrand scan-privacy

help:
	@echo "Bikou OS (微光 / びこう) - Deepin fork"
	@echo ""
	@echo "Targets:"
	@echo "  rebrand      - Apply rebranding to source"
	@echo "  scan-privacy - Scan for privacy concerns"
	@echo "  status       - Show rebrand status"

rebrand:
	@echo "Rebranding core files..."
	@python3 rebrand-scripts/rebrand.py 2>/dev/null || echo "Create rebrand.py first"

scan-privacy:
	@echo "Scanning for privacy/telemetry..."
	@grep -rn "telemetry\|analytics\|usageReport\|crashreport\|report.*server\|upload.*data" src | head -30
