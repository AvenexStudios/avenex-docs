# Troubleshooting

## The overlay is missing
Check that the Avenex client and CSP Lua apps are enabled. Confirm with your
administrator that the server permits the relevant overlay. Rejoin after
updating the client. The time monitor is hidden when the total is zero.

## Points or time look wrong
Check saved values, not unsaved selections. New settings do not recalculate
old incidents. Time from the incident ladder and track cuts accumulates;
serving a pit penalty does not clear it.

## The cut counter stopped
At the configured limit it freezes until the corresponding DT/Stop & Go is
served. A throttle time penalty does not reset the cut counter.

## The report looks old
Reload the report and confirm you opened the latest file rather than an
archived copy. Wait for race results to finalize. Compare total time and
completed laps, not an individual lap.

## Admin works but joining fails
The admin's HTTP service and the game's connection use different ports.
Ask the server administrator to check the configured HTTP/TCP/UDP ports and
the address used in the invitation.

## Need help?
Send your application version, session, selected rule and a description or
screenshot to your league administrator. Never include an admin token,
password or private configuration file in a public report.
