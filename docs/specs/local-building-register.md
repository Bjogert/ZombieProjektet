# Local building register and measurement pilot

Getaboda has no footprints in the checked OSM snapshot. A bounded Microsoft
Global ML Building Footprints sample supplies candidate outlines under
CDLA-Permissive-2.0. Detection is not proof of residential use or exact wall size.

Maintain a small local register before fitting a house. Accept a frozen polygon
FeatureCollection and explicit source metadata: provider, release, URL, hash,
license, attribution, source CRS and a bounded metric selection. No network I/O
in the registration command; no raw geometry in console output.

Allocate persistent UUIDs once, retain release-specific provider aliases, copy
the frozen source, and derive metric area and minimum rotated rectangle dimensions.
Record rectangle occupancy and long-axis bearing separately from source geometry.
Unknown facade, roof, use and height remain unknown. Keep design choices in a
separate file. Never infer a residential identity from size alone.

Acceptance:
- A known 6 by 10 metre rectangle measures 60 square metres; axis order and
  rotation are covered by independent synthetic fixtures.
- Reject invalid/empty/3D geometry, duplicate IDs, wrong hashes, out-of-selection
  features and unregistered source changes before writing output.
- Repeating a frozen import preserves IDs, observations and design choices.
- A changed snapshot requires explicit reconciliation, never silent rematching
  or loss of corrections. This pilot deliberately does not implement reconciliation.
- Stage first creation atomically; a failed validation leaves no partial register.
- Keep authoritative source and register under ignored `local-data/`, with a
  separate local backup. Commit only code, tests and non-geometric evidence.

Check the actual Getaboda sample locally and report aggregate coverage/quality.
The register is a preparation step, not game export, a verified address inventory,
or a completed real-house/playtest gate. Source-specific license text accompanies
local data. Public release and detailed private interiors remain separate reviews.
