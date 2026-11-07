"""Constants for the EON Energiemonitor integration (V2)."""

DOMAIN = "eon-energiemonitor"

CONF_REGION_CODE = "region_code"
CONF_SCOPE = "scope"
CONF_ALIAS = "alias"

API_BASE_URL = "https://api-energiemonitor.eon.com/"
DASHBOARD_BASE_URL = "https://energiemonitor.bayernwerk.de/"
REQUEST_TIMEOUT_S = 30
# Cloudflare blocks plain Python TLS; Chrome impersonation passes (see V2).
BROWSER_IMPERSONATE = "chrome"

DEFAULT_SCAN_INTERVAL = 15

ISSUE_REGION_NOT_FOUND = "region_not_found"
ISSUE_UPDATE_FAILED = "update_failed"
ISSUE_SCOPE_REGION_NOT_FOUND = "scope_region_not_found"
ISSUE_SCOPE_UPDATE_FAILED = "scope_update_failed"

# Metrics exposed as energy / percentage sensors (entity suffix / unique_id).
ENERGY_METRICS = (
    "autarky",
    "secondaryInFeed",
    "energyMix",
    "bio",
    "solar",
    "wind",
    "water",
    "others",
    "domestic",
    "public",
    "industrial",
    "renewable_generation_share",
    "dominant_source",
    "generation_total",
    "consumption_total",
    "feed_in_renewables",
    "co2_savings_today",
)

PERCENTAGE_METRICS = frozenset(
    {"autarky", "energyMix", "renewable_generation_share", "dominant_source"}
)

RESERVED_ALIASES = frozenset(
    {
        "status",
        "region",
        "autarky",
        "secondaryinfeed",
        "energymix",
        "bio",
        "solar",
        "wind",
        "water",
        "others",
        "domestic",
        "public",
        "industrial",
        "renewable_generation_share",
        "dominant_source",
        "generation_total",
        "consumption_total",
        "feed_in_renewables",
        "co2_savings_today",
    }
)

ERROR_MESSAGES = {
    "region_not_found": "Region not found",
    "network": "Network error",
    "timeout": "Timeout",
    "invalid_response": "Invalid API response",
    "parse": "Failed to parse data",
    "not_configured": "Not configured",
    "challenge": "Cloudflare challenge",
}
